---
title: Machine Learning Notes
---


## Commands

```bash
conda create -y -n sb3 python=3.11 # no mujoco2.3.7 version for python 3.12
conda activate sb3
conda install pip
pip install mujoco==2.3.7
pip install gymnasium[mujoco]
pip install stable-baselines3[extra]
# pip install gymnasium
# pip install git+https://github.com/Farama-Foundation/Gymnasium.git # addresses issue between mujoco3 and gymnasium .29
conda install -y jupyter
conda install -y -c conda-forge libstdcxx-ng #fix for anaconda linux, found here: https://stackoverflow.com/questions/71010343/cannot-load-swrast-and-iris-drivers-in-fedora-35/72200748#72200748
# conda env config vars set MUJOCO_GL=glfw PYOPENGL_PLATFORM=glfw
conda env config vars set MUJOCO_GL=osmesa PYOPENGL_PLATFORM=osmesa
conda deactivate && conda activate sb3
```

plain python environment

```bash
# python3 -m venv ~/envs/sb3
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt install -y python3.11-venv
python3.11 -m venv ~/envs/sb3
. envs/sb3/bin/activate
pip install --upgrade pip
pip install stable-baselines3[extra]
pip install mujoco==2.3.7
pip install gymnasium[mujoco]
pip install jupyter
```

some things get installed in .local/bin, so we need to do

```bash
echo "export PATH=\$PATH:$HOME/.local/bin" >> .bashrc
```

##

1. conda activate sb3
1. git clone rl zoo
1. cd rl zoo
1. pip install -e .

## Pytorch workflow

<https://machinelearningmastery.com/pytorch-tutorial-develop-deep-learning-models/>
<https://keras.io/guides/writing_a_custom_training_loop_in_torch/>

## SB3

<https://stable-baselines3.readthedocs.io/>
<https://github.com/DLR-RM/stable-baselines3?tab=readme-ov-file>
<https://araffin.github.io/post/sb3/>

### Colab Notebooks

<https://github.com/araffin/rl-tutorial-jnrr19> (made local)
<https://github.com/Stable-Baselines-Team/rl-colab-notebooks/tree/sb3> (made local)

tensorboard: <https://stable-baselines3.readthedocs.io/en/master/guide/tensorboard.html>

```bash
tensorboard --logdir leg1-tb/
```

## RL baselines zoo

<https://github.com/DLR-RM/rl-baselines3-zoo>

<https://huggingface.co/MattStammers/appo-mujoco_ant-sota>

## Mujoco

<https://pypi.org/project/mujoco/#history>
<https://mujoco.readthedocs.io/en/latest/XMLreference.html#actuator-position>

## IsaacSim

running in cpu mode

<https://forums.developer.nvidia.com/t/run-isaac-gym-in-cpu-mode-without-a-cuda-capable-gpu-on-the-device/227954/2>

## MuJoCo / gymnasium

<https://duckduckgo.com/?t=ffab&q=gymnasium+mujoco&ia=web>
<https://gymnasium.farama.org/environments/mujoco/>

## Gymnasium

<https://pypi.org/project/gymnasium/>
<https://gymnasium.farama.org/environments/mujoco/half_cheetah/>
<https://github.com/Farama-Foundation/Gymnasium/>
<https://github.com/Farama-Foundation/gym-examples>

RL within gym
<https://gymnasium.farama.org/tutorials/training_agents/reinforce_invpend_gym_v26/#sphx-glr-tutorials-training-agents-reinforce-invpend-gym-v26-py>

render mode:
gym jupyter stable baselines You tried to call render() but no `render_mode` was passed to the env constructor.
<https://github.com/openai/gym/issues/2780>
<https://github.com/openai/gym/issues/762>

### Mujoco 3 issue

<https://stackoverflow.com/questions/77438425/mujoco-structs-mjdata-object-has-no-attribute-solver-iter>
<https://github.com/Farama-Foundation/Gymnasium/pull/746>
<https://github.com/Farama-Foundation/Gymnasium/issues/749>

##

<https://www.science.org/doi/10.1126/scirobotics.aau5872>

<https://www.youtube.com/watch?v=aTDkYFZFWug>

<https://rlsummerschool.com/>

<https://mrs.felk.cvut.cz/summer-school-2023/>

<https://wandb.ai/site>

<https://link.springer.com/article/10.1007/s12555-021-0099-8>
<https://arxiv.org/pdf/2104.04644.pdf>
<https://arxiv.org/pdf/2308.03014.pdf>
<https://arxiv.org/pdf/1812.11103.pdf>

<https://www.nature.com/articles/s41598-023-32106-5>
<https://www.nature.com/articles/s42254-021-00314-5>
<https://www.nature.com/articles/s41598-022-18536-7>
<https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/csy2.12062>

## Time Series forecasting

<https://machinelearningmastery.com/how-to-develop-convolutional-neural-network-models-for-time-series-forecasting/>
<https://blog.research.google/2021/12/interpretable-deep-learning-for-time.html>
<https://www.sciencedirect.com/science/article/pii/S0169207021000637>

<https://bookdown.org/rdpeng/timeseriesbook/general-kalman-filter.html>
<https://ocw.mit.edu/courses/14-384-time-series-analysis-fall-2013/resources/mit14_384f13_lec21/>

<https://www.baeldung.com/cs/reinforcement-learning-neural-network>

<https://www.cs.rice.edu/~vardi/dag01/givan1.pdf>

<https://ocw.mit.edu/courses/14-384-time-series-analysis-fall-2013/download/>

<https://www.youtube.com/watch?v=ZoJ2OctrFLA&list=PLvcbYUQ5t0UHOLnBzl46_Q6QKtFgfMGc3>

## Kalman Filter

<https://ocw.mit.edu/courses/14-384-time-series-analysis-fall-2013/download/>

<https://ocw.mit.edu/courses/14-384-time-series-analysis-fall-2013/resources/mit14_384f13_lec21/>

<https://bookdown.org/rdpeng/timeseriesbook/general-kalman-filter.html>

## Hessian

<https://math.stackexchange.com/questions/3680708/what-is-the-difference-between-the-jacobian-hessian-and-the-gradient>

<https://en.wikipedia.org/wiki/Hessian_matrix>

## Donkeycar

<https://medium.com/@vigosslive2/self-driving-with-reinforcement-learning-in-donkeycar-simulator-ea4f3f85c609>
<https://mushr.io/tutorials/deep_learning/>

Duckietown

* <https://github.com/orgs/duckietown/repositories?type=all>
* <https://duckietown.com/guides/start-teaching/>
* <https://duckietown.com/educational-resources/>
* <https://docs.duckietown.com/daffy/devmanual-software/intermediate/simulation/index.html>

turtlebot
<https://github.com/ITTcs/gym-turtlebot3>

## CMAES

<https://towardsdatascience.com/efficient-feature-selection-via-cma-es-covariance-matrix-adaptation-evolution-strategy-ee312bc7b173>
<https://pypi.org/project/cmaes/>
<https://github.com/CMA-ES/pycma>

```bash
tensorboard --logdir log4
```
