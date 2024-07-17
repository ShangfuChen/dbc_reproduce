# Diffusion Model-Augmented Behavioral Cloning

[Shang-Fu Chen\*](https://shangfuchen.github.io/),
[Hsiang-Chun Wang\*](https://openreview.net/profile?id=~Hsiang-Chun_Wang1),
[Ming-Hao Hsu](https://qaz159qaz159.github.io/),
[Chun-Mao Lai](https://www.mecoli.net/),
[Shao-Hua Sun](https://shaohua0116.github.io) at [NTU RLL lab](https://nturll.xyz/about)

[[Project website]](https://nturobotlearninglab.github.io/dbc/) [[Paper]](https://arxiv.org/abs/2302.13335)

This is the official PyTorch implementation of the paper ["Diffusion Model-Augmented Behavioral Cloning"](https://nturobotlearninglab.github.io/dbc/) (ICML2024).

![image](framework.jpeg)

## Installation

1. This code base requires `Python 3.7.2` or higher. All package requirements are in
   `requirements.txt`. To install from scratch using Anaconda, use the following
   commands.

```
conda create -n [your_env_name] python=3.7.2
conda activate [your_env_name]
pip install -r requirements.txt

cd d4rl
pip install -e .
cd ../rl-toolkit
pip install -e .

mkdir -p data/trained_models
```

2. Setup [Weights and Biases](https://wandb.ai/site) by first logging in with `wandb login <YOUR_API_KEY>` and then editing `config.yaml` with your W&B username and project name.

```
python download_demos.py
```

## How to reproduce experiments
- For diffusion model pretraining, run `dbc/ddpm.py`.
- For policy learning, you can either run `dbc/main.py` for single experiment or run `wandb sweep configs/<env>/<alg.yaml>` to run a wandb sweep. 
- We have provided both methods to reproduce our result. Configuration files for policy learning of all tasks can be found at `configs`.

We specify how to train diffusion models and the location of configuration files as following:

### Maze2D

- Ours:
    1. DM pretraining: `./runs/maze/train_dm.sh`
    2. Policy learning: `./runs/maze/dbc.sh` or `./wandb.sh ./configs/maze/dbc.yaml`
- BC: `./runs/maze/bc.sh` or `./wandb.sh ./configs/maze/bc.yaml`

### Fetch Pick

- Ours:
    1. DM pretraining: `./runs/fetchPick/train_dm.sh`
    2. Policy learning: `./runs/fetchPick/dbc.sh` or `./wandb.sh ./configs/fetchPick/dbc.yaml`
- BC: `./runs/fetchPick/bc.sh` or `./wandb.sh ./configs/fetchPick/bc.yaml`

### Hand Rotate

- Ours:
    1. DM pretraining: `./runs/hand/train_dm.sh`
    2. Policy learning: `./runs/hand/dbc.sh` or `./wandb.sh ./configs/hand/dbc.yaml`
- BC: `./runs/hand/bc.sh` or `./wandb.sh ./configs/hand/bc.yaml`

### Half Cheetah

- Ours:
    1. DM pretraining: `./runs/halfcheetah/train_dm.sh`
    2. Policy learning: `./runs/halfcheetah/dbc.sh` or `./wandb.sh ./configs/halfcheetah/dbc.yaml`
- BC: `./runs/halfcheetah/bc.sh` or `./wandb.sh ./configs/halfcheetah/bc.yaml`

### Walker

- Ours:
    1. DM pretraining: `./runs/walker/train_dm.sh`
    2. Policy learning: `./runs/walker/dbc.sh` or `./wandb.sh ./configs/walker/dbc.yaml`
- BC: `./runs/walker/bc.sh` or `./wandb.sh ./configs/walker/bc.yaml`

### Ant Goal

- Ours:
    1. DM pretraining: `./runs/antReach/train_dm.sh`
    2. Policy learning: `./runs/antReach/dbc.sh` or `./wandb.sh ./configs/antReach/dbc.yaml`
- BC: `./runs/antReach/bc.sh` or `./wandb.sh ./configs/antReach/bc.yaml`

## Code Structure

- `dbc`: method and custom environment code.
  - `rl-toolkit/rlf/algos/il/dbc.py`: Algorithm of our method
  - `rl-toolkit/rlf/algos/il/bc.py`: Algorithm of BC
  - `d4rl/d4rl/pointmaze/maze_model.py`: Maze2D task
  - `dbc/envs/fetch/custom_fetch.py`: Fetch Pick task.
  - `dbc/envs/hand/manipulate.py`: Hand Rotate task.
- `rl-toolkit`: base RL code and code for imitation learning baselines from [rl-toolkit](https://github.com/ASzot/rl-toolkit).
- `d4rl`: Codebase from [D4RL: Datasets for Deep Data-Driven Reinforcement Learning](https://github.com/rail-berkeley/d4rl) for Maze2D.

## Acknowledgement

- The Fetch and Hand Rotate environments are with some tweaking from [OpenAI](https://github.com/openai/gym/tree/6df1b994bae791667a556e193d2a215b8a1e397a/gym/envs/robotics)
- The Ant environment is with some tweaking from [DnC](https://github.com/dibyaghosh/dnc)
- The Maze2D environment is based on [D4RL: Datasets for Deep Data-Driven Reinforcement Learning](https://github.com/rail-berkeley/d4rl).
- The Walker2d environment is in [OpenAI Gym](https://github.com/openai/gym/blob/master/gym/envs/mujoco/walker2d_v3.py).

## Reference

This repo is based on the official PyTorch [implementation](https://github.com/clvrai/goal_prox_il) of the paper ["Generalizable Imitation Learning from Observation via Inferring Goal Proximity"](https://clvrai.github.io/goal_prox_il/)

## Citation

```
@article{wang2023diffusion,
  title={Diffusion Model-Augmented Behavioral Cloning},
  author={Wang, Hsiang-Chun and Chen, Shang-Fu and Hsu, Ming-Hao and Lai, Chun-Mao and Sun, Shao-Hua},
  journal={arXiv preprint arXiv:2302.13335},
  year={2023}
}
```