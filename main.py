#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 16:45:10 2018

@author: sebastian
"""

from unityagents import UnityEnvironment
import numpy as np
import random
import torch
from collections import deque
from dqn_agent import Agent
from collections import OrderedDict
import matplotlib.pyplot as plt

def dqn(env, agent, n_episodes=2000, max_t=1000, eps_start=1.0, eps_end=0.01, eps_decay=0.995):
    """Deep Q-Learning.
   
    Params
    ======
        n_episodes (int): maximum number of training episodes
        max_t (int): maximum number of timesteps per episode
        eps_start (float): starting value of epsilon, for epsilon-greedy action selection
        eps_end (float): minimum value of epsilon
        eps_decay (float): multiplicative factor (per episode) for decreasing epsilon
    """
    scores = []                        # list containing scores from each episode
    scores_window = deque(maxlen=100)  # last 100 scores
    eps = eps_start                    # initialize epsilon
    saved = False
    brain_name = env.brain_names[0]
    for i_episode in range(1, n_episodes+1):
        env_info = env.reset()[brain_name]        # send the action to the environment
        state = env_info.vector_observations[0]   # get the next state
        score = 0
        for t in range(max_t):
            action = agent.act(state, eps)
            env_info = env.step(action)[brain_name]
            next_state = env_info.vector_observations[0]   # get the next state
            reward = env_info.rewards[0]   #get reward
            done = env_info.local_done[0]                  # see if episode has finished
            agent.step(state, action, reward, next_state, done)
            state = next_state
            score += reward
            if done:
                break 
        scores_window.append(score)       # save most recent score
        scores.append(score)              # save most recent score
        eps = max(eps_end, eps_decay*eps) # decrease epsilon
        print('\rEpisode {}\tAverage Score: {:.2f}'.format(i_episode, np.mean(scores_window)), end="")
        if i_episode % 100 == 0:
            print('\rEpisode {}\tAverage Score: {:.2f}'.format(i_episode, np.mean(scores_window)))
        if np.mean(scores_window)>=15.0:
            print('\nEnvironment solved in {:d} episodes!\tAverage Score: {:.2f}'.format(i_episode-100, np.mean(scores_window)))
            torch.save(agent.qnetwork_local.state_dict(), 'checkpoint.pth')
            saved = True
            break
    if not saved:
        torch.save(agent.qnetwork_local.state_dict(), 'checkpoint.pth')
    return scores




def main(trainMode, testMode):
    env = UnityEnvironment(file_name="env/Banana.x86_64")
    brain_name = env.brain_names[0]
    brain = env.brains[brain_name]
    env_info = env.reset(train_mode=trainMode)[brain_name]
    print('Number of agents:', len(env_info.agents))
    # number of actions
    action_size = brain.vector_action_space_size
    print('Number of actions:', action_size)
    
    # examine the state space 
    state = env_info.vector_observations[0]
    print('States look like:', state)
    state_size = len(state)
    print('States have length:', state_size)
    agent = Agent(state_size=state_size, action_size=action_size, seed=0)
    
    
    if (trainMode):
        trainAgent(env, agent)
    elif (testMode):
        watchTrainedAgent(env, agent)
    else:
        print('Please specify if you want to test (--test) \n '
              'or train (--train) the agent')
    
def trainAgent(env, agent):
        # get the default brain
    scores = dqn(env, agent)
    # plot the scores
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(np.arange(len(scores)), scores)
    plt.ylabel('Score')
    plt.xlabel('Episode #')
    plt.show()
    
def watchTrainedAgent(env, agent):
    import time
    # load the weights from file
    agent.qnetwork_local.load_state_dict(torch.load('checkpoint.pth'))
    brain_name = env.brain_names[0]
    env_info = env.reset()[brain_name]        # send the action to the environment
    state = env_info.vector_observations[0]   # get the next state
    score = 0                                          # initialize the score
    while True:
        action = agent.act(state)        # select an action
        env_info = env.step(action)[brain_name]        # send the action to the environment
        next_state = env_info.vector_observations[0]   # get the next state
        reward = env_info.rewards[0]                   # get the reward
        done = env_info.local_done[0]                  # see if episode has finished
        score += reward                                # update the score
        state = next_state                             # roll over the state to next time step
        time.sleep(0.033)                               # for Visualization ~ 30 fps
        if done:                                       # exit loop if episode finished
            break
        
    print("Score: {}".format(score))
    
if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Setup Paramenters for Banana Joe')
    parser.add_argument('--train', action='store_true', help='training')
    parser.add_argument('--test', action='store_true',  help='testing')
    #parser.add_argument('--schema', metavar='path', required=True,
     #                   help='path to schema')
    args = parser.parse_args()
    main(trainMode=args.train, testMode = args.test)