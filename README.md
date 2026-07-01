# Task
### *I am trying to learn Python for Multi-Agent Systems as fast as possible, based on the following training plan. This repo is organized using the structure specified in this file as well.*

# 50-Hour Python → SpecRLBench (Specification-Guided RL) Sprint Plan

This learning plan is centered around [SpecRLBench](https://github.com/BU-DEPEND-Lab/SpecRLBench), a state-of-the-art benchmark suite designed to evaluate generalization in specification-guided reinforcement learning using Linear Temporal Logic (LTL).

---

## **PHASE 1: Foundations of LTL & Gym Environments (Hours 1-10)**

### **Hours 1-3: Core Python & Gymnasium API**
- **Hour 1**: [Python.org Tutorial](https://docs.python.org/3/tutorial/) (basics, control flow, functions)
- **Hour 2**: Object-Oriented Programming (OOP) in Python (classes, inheritance, magic methods)
- **Hour 3**: Build a custom [Gymnasium Environment](https://gymnasium.farama.org/) representing a simplified 2D grid world with custom state and step functions.
- **Milestone**: Comfortable with OOP and the standard Gymnasium interface.

### **Hours 4-6: Linear Temporal Logic (LTL) & Automata**
- **Hour 4**: Learn LTL syntax and semantics (Boolean operators, temporal operators like $\mathsf{F}$, $\mathsf{G}$, $\mathsf{U}$). See [LTL Wikipedia](https://en.wikipedia.org/wiki/Linear_temporal_logic).
- **Hour 5**: Install and configure [Rabinizer 4](https://www7.in.tum.de/~kretinsk/rabinizer4.html) to translate LTL formulas into Büchi Automata or Deterministic Finite Automata (DFAs).
- **Hour 6**: Write a Python script to parse a simple LTL formula and trace state transitions on its corresponding automaton.
- **Milestone**: Understand how LTL specifications translate to formal automata.

### **Hours 7-10: PyTorch & Goal-Conditioned RL (GCRL)**
- **Hours 7-8**: [PyTorch Documentation](https://pytorch.org/docs/stable/index.html) - Tensors, neural networks (`nn.Module`), and optimization.
- **Hours 9-10**: Implement a basic Goal-Conditioned PPO or DQN agent in PyTorch to reach specific target coordinates in your custom Gym environment.
- **Milestone**: Ready to build neural network policies conditioned on task specifications.

---

## **PHASE 2: SpecRLBench & Integrated Environments (Hours 11-20)**

### **Hours 11-13: SpecRLBench Setup & Architecture**
- **Hour 11**: Clone and install [SpecRLBench GitHub Repository](https://github.com/BU-DEPEND-Lab/SpecRLBench). Read the [SpecRLBench Paper](https://arxiv.org/abs/2604.24729).
- **Hour 12**: Set up the conda environment (`specbench`) and verify the installation using `test_env.py`.
- **Hour 13**: Understand the environment interface (decomposition of observations into proposition-dependent $s_{AP}$ and independent $s_{\neq AP}$ parts).
- **Milestone**: SpecRLBench successfully installed and running locally.

### **Hours 14-16: Safety-Gymnasium & panda-gym Integration**
- **Hours 14-15**: Explore [Safety-Gymnasium](https://github.com/PKU-Alignment/safety-gymnasium) (used for navigation tasks like ZoneEnv with Point, Car, and Ant robots). See [Safety-Gymnasium Docs](https://safety-gymnasium.readthedocs.io/).
- **Hour 16**: Explore [panda-gym](https://github.com/qgallouedec/panda-gym) (used for 3D manipulation tasks with a 7-DoF robot arm). See [panda-gym Docs](https://panda-gym.readthedocs.io/).
- **Milestone**: Run basic physics-based simulation loops in both navigation and manipulation domains.

### **Hours 17-20: Multi-Agent & Dynamic Environments**
- **Hours 17-18**: Set up the multi-agent ZoneEnv variant using the [PettingZoo API](https://pettingzoo.farama.org/) and run a simulation loop with random actions.
- **Hours 19-20**: Configure dynamic moving regions in ZoneEnv to test policy robustness under changing environment dynamics.
- **Milestone**: Run multi-agent and dynamic robot simulations in SpecRLBench.

---

## **PHASE 3: Classic Baselines & Automata Embeddings (Hours 21-30)**

### **Hours 21-25: LTL2Action & GCRL-LTL Deep Dive**
- **Hours 21-23**: Study [LTL2Action GitHub](https://github.com/LTL2Action/LTL2Action) - learns to progress LTL formulas online and encodes their syntax trees via Graph Neural Networks (GNNs).
- **Hours 24-25**: Study [GCRL-LTL GitHub](https://github.com/RU-Automated-Reasoning-Group/GCRL-LTL) - uses a weighted graph search over Büchi automata to compose goal-conditioned policies.
- **Milestone**: Understand how syntax trees and automata graph searches are used to satisfy LTL.

### **Hours 26-30: RAD-Embeddings (Compositional Automata Embeddings)**
- **Hours 26-28**: Study [RAD-Embeddings GitHub](https://github.com/rad-dfa/rad-embeddings) and the [RAD-Embeddings Project Page](https://rad-embeddings.github.io/) - pre-trains latent DFA representations that are provably correct.
- **Hours 29-30**: Integrate RAD-Embeddings into a goal-conditioned policy and evaluate its generalization on simple tasks.
- **Milestone**: Understand latent representation learning for formal specifications.

---

## **PHASE 4: State-of-the-Art: DeepLTL & GenZ-LTL (Hours 31-40)**

### **Hours 31-35: DeepLTL Implementation**
- **Hours 31-33**: Study [DeepLTL GitHub](https://github.com/mathiasj33/deep-ltl) and [DeepLTL Project Page](https://deep-ltl.github.io) - learns to satisfy complex LTL specifications via subgoal sequence embeddings.
- **Hours 34-35**: Run the training scripts for DeepLTL on `LetterWorld` and `ZoneEnv`.
- **Milestone**: Successfully train and evaluate a DeepLTL model.

### **Hours 36-40: GenZ-LTL Implementation**
- **Hours 36-38**: Study [GenZ-LTL GitHub](https://github.com/BU-DEPEND-Lab/GenZ-LTL) and [GenZ-LTL Project Page](https://bu-depend-lab.github.io/GenZ-LTL/) - decomposes tasks into reach-avoid subgoals solved one at a time using safe RL and observation reduction.
- **Hours 39-40**: Run the training scripts for GenZ-LTL on `ZoneEnv` and inspect the saved model checkpoints.
- **Milestone**: Understand the state-of-the-art approach for zero-shot generalization to unseen LTL specifications.

---

## **PHASE 5: Benchmarking & Generalization Analysis (Hours 41-50)**

### **Hours 41-43: In-Distribution (IND) vs Out-of-Distribution (OOD) Evaluation**
- **Hours 41-42**: Run the evaluation scripts in SpecRLBench comparing all baselines on IND and OOD specifications (unseen formulas with longer subgoal sequences).
- **Hour 43**: Analyze the success rate ($\eta_s$), violation rate ($\eta_v$), and average steps ($\mu$) as shown in [SpecRLBench Paper Section 5](https://arxiv.org/abs/2604.24729).
- **Milestone**: Complete the core generalization benchmark.

### **Hours 44-46: Infinite-Horizon & Multi-Agent Benchmarking**
- **Hours 44-45**: Evaluate the baselines on infinite-horizon tasks (responsive $\Phi_{\text{rsp}}$, recurrence $\Phi_{\text{rec}}$, and persistence $\Phi_{\text{per}}$ behaviors).
- **Hour 46**: Benchmark the baselines on multi-agent cooperative and mixed tasks.
- **Milestone**: Understand the limits of current methods in infinite-horizon and multi-agent settings.

### **Hours 47-50: Custom Environment & Specification Design**
- **Hours 47-48**: Use `customize_env.py` to define a custom environment configuration (e.g., custom robot dynamics or region layout).
- **Hours 49-50**: Use the specification samplers in `sampler/README.md` to design new LTL specifications and test the generalization boundaries of your trained models.
- **Output**: A comprehensive benchmarking report comparing LTL-guided RL algorithms on custom tasks.

---

## **CRITICAL SUCCESS FACTORS**

### **For 50-Hour Sprint:**
1. **No Distractions**: Phone off, internet only for documentation and resources.
2. **Energy Management**: Optimize caffeine/nutrition strategy.
3. **Break Protocol**: 10 min every 2 hours, 30 min every 8 hours.
4. **Sleep Minimum**: 4-6 hours for cognitive function.
5. **Focus Strategy**: Start with `LetterWorld` (discrete grid world) before moving to high-dimensional continuous control like `ZoneEnv` (Ant/Car) or `ArmEnv`.
6. **Progress Tracking**: Mark milestone completion each phase.

### **Emergency Resources:**
- **SpecRLBench Issues**: [SpecRLBench GitHub Issues](https://github.com/BU-DEPEND-Lab/SpecRLBench/issues)
- **Safety-Gymnasium Help**: [Safety-Gymnasium GitHub Issues](https://github.com/PKU-Alignment/safety-gymnasium/issues)
- **PettingZoo Help**: [PettingZoo GitHub Issues](https://github.com/Farama-Foundation/PettingZoo/issues)
- **PyTorch Help**: [PyTorch Forums](https://discuss.pytorch.org/)

---

# 50-Hour Sprint Storage Structure

## Main Directory  
`C:\users\abdul\python-multiagent-training\`

## Folder Structure

```
python-multiagent-training/
├── code/
│   ├── phase-01-ltl-foundations/
│   ├── phase-02-specrlbench-envs/
│   ├── phase-03-classic-baselines/
│   ├── phase-04-sota-methods/
│   ├── phase-05-benchmarking/
│   └── final-prototype/
├── notes/
│   ├── hourly-logs/
│   ├── concepts/
│   └── resources/
├── data/
│   ├── model-checkpoints/
│   └── training-runs/
├── experiments/
│   ├── agent-tests/
│   └── evaluation-videos/
└── docs/
    ├── 50-hour-sprint-plan.md
    └── progress-tracking/
```

## Phase Code Structure
```
phase-XX-topic/
├── exercises/
│   ├── hour-XX/
│   └── hour-YY/
├── custom-configs/
├── prototype-code/
└── phase-notes.md
```

## Recommended Tools
- **Version Control**: Git repo with hourly commits.
- **IDE**: VS Code with Python + PyTorch extensions.
- **Environment**: Single conda env `specbench` (Python 3.10).
- **Notebooks**: Jupyter for interactive rendering and plotting.
- **Time Tracking**: Pomodoro timer (25min work, 5min break).

## Git Setup & Installation Commands  
```bash
cd C:\users\abdul\python-multiagent-training
git init

# Create and activate conda environment
conda create -n specbench python=3.10
conda activate specbench

# Clone and install SpecRLBench
git clone https://github.com/BU-DEPEND-Lab/SpecRLBench.git
cd SpecRLBench
./install.bash
```

## Hourly Workflow (50-Hour Sprint)
1. **Start hour**: Log in hourly-logs/hour-XX.md
2. **Work**: Save code in appropriate phase folder
3. **End hour**: Commit progress to git
4. **Milestone check**: Mark phase completion
5. **Break**: 10min every 2 hours (mandatory)
