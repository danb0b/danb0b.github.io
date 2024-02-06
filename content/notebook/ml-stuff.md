## Commands

```bash
conda create -y -n sb3
conda activate sb3
pip install stable-baselines3[extra]
pip install mujoco==2.3.7
# pip install gymnasium
pip install gymnasium[mujoco]
# pip install git+https://github.com/Farama-Foundation/Gymnasium.git # addresses issue between mujoco3 and gymnasium .29
conda install jupyter
conda install -c conda-forge libstdcxx-ng #fix for anaconda linux, found here: https://stackoverflow.com/questions/71010343/cannot-load-swrast-and-iris-drivers-in-fedora-35/72200748#72200748
echo "export PATH=\$PATH:$HOME/.local/bin" >> .bashrc
# conda env config vars set MUJOCO_GL=glfw PYOPENGL_PLATFORM=glfw
conda deactivate && conda activate mujoco
```

## Pytorch workflow

https://machinelearningmastery.com/pytorch-tutorial-develop-deep-learning-models/
https://keras.io/guides/writing_a_custom_training_loop_in_torch/

## SB3

https://stable-baselines3.readthedocs.io/
https://github.com/DLR-RM/stable-baselines3?tab=readme-ov-file
https://araffin.github.io/post/sb3/

### Colab Notebooks

https://github.com/araffin/rl-tutorial-jnrr19 (made local)
https://github.com/Stable-Baselines-Team/rl-colab-notebooks/tree/sb3 (made local)


## Mujoco
https://pypi.org/project/mujoco/#history

## IsaacSim

running in cpu mode

https://forums.developer.nvidia.com/t/run-isaac-gym-in-cpu-mode-without-a-cuda-capable-gpu-on-the-device/227954/2

## MuJoCo / gymnasium

https://duckduckgo.com/?t=ffab&q=gymnasium+mujoco&ia=web
https://gymnasium.farama.org/environments/mujoco/

## Gymnasium

https://pypi.org/project/gymnasium/
https://gymnasium.farama.org/environments/mujoco/half_cheetah/


RL within gym
https://gymnasium.farama.org/tutorials/training_agents/reinforce_invpend_gym_v26/#sphx-glr-tutorials-training-agents-reinforce-invpend-gym-v26-py


render mode:
gym jupyter stable baselines You tried to call render() but no `render_mode` was passed to the env constructor.
https://github.com/openai/gym/issues/2780
https://github.com/openai/gym/issues/762


### Mujoco 3 issue:

https://stackoverflow.com/questions/77438425/mujoco-structs-mjdata-object-has-no-attribute-solver-iter
https://github.com/Farama-Foundation/Gymnasium/pull/746
https://github.com/Farama-Foundation/Gymnasium/issues/749

## RL aselines zoo
https://github.com/DLR-RM/rl-baselines3-zoo


https://huggingface.co/MattStammers/appo-mujoco_ant-sota


## 
https://www.science.org/doi/10.1126/scirobotics.aau5872

https://www.youtube.com/watch?v=aTDkYFZFWug

https://rlsummerschool.com/

https://mrs.felk.cvut.cz/summer-school-2023/


https://wandb.ai/site

https://link.springer.com/article/10.1007/s12555-021-0099-8
https://arxiv.org/pdf/2104.04644.pdf
https://arxiv.org/pdf/2308.03014.pdf
https://arxiv.org/pdf/1812.11103.pdf

https://www.nature.com/articles/s41598-023-32106-5
https://www.nature.com/articles/s42254-021-00314-5
https://www.nature.com/articles/s41598-022-18536-7
https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/csy2.12062