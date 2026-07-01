from __future__ import annotations

import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import torch
import torch.nn as nn
from torch.distributions.normal import Normal
from tqdm import tqdm

import gymnasium as gym

plt.rcParams["figure.figsize"] = (10, 5)

'''[AK] Policy Network
https://gymnasium.farama.org/tutorials/training_agents/mujoco_reinforce/#policy-network

Policies are mapping from environment to probability distrib. of actions
https://gymnasium.farama.org/_images/mujoco_reinforce_fig2.png
"It consists of a neural network wth 2 linear layers that are shared
between both the predicted mean and standard deviation. Further, the
single individual linear layers are used to estimate the mean and the
standard deviation" - Gymnasium
- Linear Layers: Every neuron is connected to every other neuron between two layers
- Predicted Mean: Expected future reward based on current NN
- Stardard Deviation: Same as stats, but here represents distribution of rewards
- Non-Linearity: When something is not linear (e.g. normal distribution) (T_T)
'''

class Policy_Network(nn.Module):
    """Parametrized Policy Network."""

    def __init__(self, obs_space_dims: int, action_space_dims: int):
        """Initializes a neural network that estimates the mean and standard deviation
         of a normal distribution from which an action is sampled from.

        Args:
            obs_space_dims: Dimension of the observation space
            action_space_dims: Dimension of the action space
        """
        super().__init__()

        # [AK] hidden layers neuron count
        hidden_space1 = 16  # Nothing special with 16, feel free to change
        hidden_space2 = 32  # Nothing special with 32, feel free to change

        # Shared Network
        self.shared_net = nn.Sequential(
            nn.Linear(obs_space_dims, hidden_space1),
            nn.Tanh(),
            nn.Linear(hidden_space1, hidden_space2),
            nn.Tanh(),
        )
        "[AK] makes a NN with layer1 = obs, layer2 = hidden1, layer3 = hidden3"

        # [AK] Next two layers go from hidden to specific calculations for
        #   Predicted mean and STDDEV

        # Policy Mean specific Linear Layer
        self.policy_mean_net = nn.Sequential(
            nn.Linear(hidden_space2, action_space_dims)
        )

        # Policy Std Dev specific Linear Layer
        self.policy_stddev_net = nn.Sequential(
            nn.Linear(hidden_space2, action_space_dims)
        )

    def forward(self, env_obs: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        """Conditioned on the observation, returns the mean and standard deviation
         of a normal distribution from which an action is sampled from.

        Args:
            x: Observation from the environment

        Returns:
            action_means: predicted mean of the normal distribution
            action_stddevs: predicted standard deviation of the normal distribution
        """
        # [AK] action_means/stdevs are calculated based on
        #   1. finding the shared features (first two hidden layers)
        #   2. then finding the mean/stdev separately

        shared_features = self.shared_net(env_obs.float())
        action_means = self.policy_mean_net(shared_features)
        action_stddevs = torch.log(
            1 + torch.exp(self.policy_stddev_net(shared_features))
        )

        return action_means, action_stddevs
    
class REINFORCE:
    """REINFORCE algorithm.\n
    ‘RE’ward ‘I’ncrement ‘N’on-negative ‘F’actor times ‘O’ffset ‘R’einforcement times ‘C’haracteristic ‘E’ligibility"""

    def __init__(self, obs_space_dims: int, action_space_dims: int):
        """Initializes an agent that learns a policy via REINFORCE algorithm [1]
        to solve the task at hand (Inverted Pendulum v4).

        Args:
            obs_space_dims: Dimension of the observation space
            action_space_dims: Dimension of the action space
        """

        # Hyperparameters
        self.learning_rate = 1e-4  # Learning rate for policy optimization
        self.gamma = 0.99  # Discount factor
        self.eps = 1e-6  # small number for mathematical stability

        # [AK] Store probabilities of action and rewards from that action
        #   Presumably useful when backpropagating
        self.probs = []  # Stores probability values of the sampled action
        self.rewards = []  # Stores the corresponding rewards

        self.net = Policy_Network(obs_space_dims, action_space_dims)
        "[AK] Hidden/Mean/STDEV Network"
        self.optimizer = torch.optim.AdamW(self.net.parameters(), lr=self.learning_rate)
        """
        [AK] AdamW is an algorithm (https://docs.pytorch.org/docs/2.12/generated/torch.optim.AdamW.html)
        It puts calculations >> weight/reward decay in that order so calcs aren't conflated
        This helps generalize for real-world data because
        1. "Flatter" areas in gradient are should be given more momentum to change quickly
        2. Updates gradient based on changes in XYZ weight (smaller val, slower change)
        3. Applies weight decay so model prioritizes immediate rewards 
        """

    def sample_action(self, state: np.ndarray) -> float:
        """Returns an action, conditioned on the policy and observation.

        Args:
            state: Observation from the environment

        Returns:
            action: Action to be performed
        """

        # [AK] a tensor is an n-dim arr that can run on a GPU (hardware accel)
        state = torch.tensor(np.array([state]))
        # [AK] find predicted mean/stdev from 2HLL NN
        action_means, action_stddevs = self.net(state)

        # create a normal distribution from the predicted
        #   mean and standard deviation and sample an action
        distrib = Normal(action_means[0] + self.eps, action_stddevs[0] + self.eps)
        action = distrib.sample()
        prob = distrib.log_prob(action)

        action = action.numpy()

        self.probs.append(prob)

        return action

    def update(self):
        """Updates the policy network's weights."""
        running_g = 0
        gs = []

        #[AK] Backpropagation!!!
        # Discounted return (backwards) - [::-1] will return an array in reverse
        for R in self.rewards[::-1]:
            running_g = R + self.gamma * running_g
            gs.insert(0, running_g)

        deltas = torch.tensor(gs)
        "[AK] How much reward (discounted) for each action taken during the episode"
        log_probs = torch.stack(self.probs).squeeze()
        "[AK] takes the mean of the probability distribs"

        # Update the loss with the mean log probability and deltas
        # Now, we compute the correct total loss by taking the sum of the element-wise products.
        loss = -torch.sum(log_probs * deltas)
        "[AK] How much the current policy lost to the optimal policy"

        # Update the policy network
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        # Empty / zero out all episode-centric/related variables
        self.probs = []
        self.rewards = []

# Create and wrap the environment
env = gym.make("InvertedPendulum-v5")
wrapped_env = gym.wrappers.RecordEpisodeStatistics(env, 50)  # Records episode-reward

total_num_episodes = int(5e3)  # Total number of episodes (5000)
# Observation-space of InvertedPendulum-v5 (4)
obs_space_dims = env.observation_space.shape[0]
# Action-space of InvertedPendulum-v5 (1)
action_space_dims = env.action_space.shape[0]
rewards_over_seeds = []

# [AK] Seeds are numbers used to have deterministic control over randomness
for given_seed in [1, 2, 3, 5, 8]:  # Fibonacci seeds
    # set seed
    torch.manual_seed(given_seed)
    random.seed(given_seed)
    np.random.seed(given_seed)

    # Reinitialize agent every seed
    agent = REINFORCE(obs_space_dims, action_space_dims)
    reward_over_episodes = []

    for episode in tqdm(range(total_num_episodes)):
        # gymnasium v26 requires users to set seed while resetting the environment
        obs, info = wrapped_env.reset(seed=given_seed)

        done = False
        while not done:
            action = agent.sample_action(obs)
            "[AK] sample action based on Policy_Network (2HLL NN)"

            # Step return type - `tuple[ObsType, SupportsFloat, bool, bool, dict[str, Any]]`
            # These represent the next observation, the reward from the step,
            # if the episode is terminated, if the episode is truncated and
            # additional info from the step
            obs, reward, terminated, truncated, info = wrapped_env.step(action)
            agent.rewards.append(reward)

            # End the episode when either truncated or terminated is true
            #  - truncated: The episode duration reaches max number of timesteps
            #  - terminated: Any of the state space values is no longer finite.
            #
            done = terminated or truncated

        reward_over_episodes.append(wrapped_env.return_queue[-1])
        agent.update()

        if episode % 1000 == 0:
            avg_reward = int(np.mean(wrapped_env.return_queue))
            print("Episode:", episode, "Average Reward:", avg_reward)

    rewards_over_seeds.append(reward_over_episodes)

df1 = pd.DataFrame(rewards_over_seeds).melt()
df1.rename(columns={"variable": "episodes", "value": "reward"}, inplace=True)
sns.set_theme(style="darkgrid", context="talk", palette="rainbow")
sns.lineplot(x="episodes", y="reward", data=df1).set(
    title="REINFORCE for InvertedPendulum-v4"
)
plt.show()