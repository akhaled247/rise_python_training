import gymnasium as gym
from gymnasium.wrappers import FlattenObservation

env = gym.make('CartPole-v1', render_mode='human') # switch to `None` when training
observation, info = env.reset()

w_env = gym.make('CarRacing-v3', render_mode=None)
print(w_env.observation_space.shape)

'''
Wrappers are modifications to the env
Common others include `TimeLimit` `ClipAction` `RescaleAction` `TimeAwareObservation`
More information at https://gymnasium.farama.org/api/wrappers/
'''
wrapped_env = FlattenObservation(w_env)
print(wrapped_env.observation_space.shape)

''' __Action and Observation Space__
print(f"Action space: {env.action_space}")  # Discrete(2) - left or right
print(f"Sample action: {env.action_space.sample()}")  # 0 or 1

print(f"Observation space: {env.observation_space}")  # Box with 4 values
print(f"Sample observation: {env.observation_space.sample()}")  # Random valid observation
'''
breakpoint()

print(f"Starting observation: {observation}")
episode_over = False
total_reward = 0

while not episode_over:
    action = env.action_space.sample() # Random action
    observation, reward, terminated, truncated, info = env.step(action) #initializing vars, observing outcome

    total_reward += reward
    episode_over = terminated or truncated

print(f"Episode finished! Total reward: {total_reward}")
env.close()