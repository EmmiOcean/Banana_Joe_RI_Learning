[//]: # (Image References)

[image1]: https://user-images.githubusercontent.com/10624937/42135619-d90f2f28-7d12-11e8-8823-82b970a54d7e.gif "Trained Agent"

# Project: Training an agent for Deep Reinforcement Learning - Navigation

For this project, you will train an agent to navigate (and collect bananas!) in a large, square world.  

## Game environment

In this project, we train **Deep Q-Learning** (**DQN**) Agent which walks around in the banana catching game simulator(Unity ML-Agents environment).
It is the first project of the [Deep Reinforcement Learning Nanodegree (DRLND)](https://www.udacity.com/course/deep-reinforcement-learning-nanodegree--nd893) and was adapted from the original version on [Udacity Github Repository](https://github.com/udacity/deep-reinforcement-learning/tree/master/p1_navigation).

![Trained Agent][image1]

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana.  Thus, the goal of your agent is to collect as many yellow bananas as possible while avoiding blue bananas.  

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around agent's forward direction.  Given this information, the agent has to learn how to best select actions.  Four discrete actions are available, corresponding to:
- **`0`** - move forward.
- **`1`** - move backward.
- **`2`** - turn left.
- **`3`** - turn right.

The task is episodic, and in order to solve the environment, your agent must get an average score of +13 over 100 consecutive episodes.

## Getting Started
1. Check [Prerequisite](https://github.com/udacity/deep-reinforcement-learning/#dependencies), and follow the instructions.

2. Download the environment from one of the links below.  You need only select the environment that matches your operating system:
    - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)

    (_For Windows users_) Check out [this link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

    (_For AWS_) If you'd like to train the agent on AWS (and have not [enabled a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md)), then please use [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux_NoVis.zip) to obtain the environment.

3. Clone [this](https://github.com/EmmiOcean/Banana_Joe_RI_Learning.git) repository.

4. Place the file in `env/` directory, and unzip (or decompress) the file.

## Instructions
### Jupyter Notebook
To train the agent, start jupyter notebook, open `Navigation.ipynb` and execute! For more information, please check instructions inside the notebook.

### Command line 
To train the agent via command line type `python main.py --train`

To see the agent walking inside the enviroment use the command `python main.py --test`





# Banana_Joe_RI_Learning
