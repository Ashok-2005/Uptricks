import numpy as np
import random
from collections import defaultdict
import gym

class QLearningAgent:
    def __init__(self, action_space, alpha=0.1, gamma=0.99, epsilon=0.1):
        self.action_space = action_space
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = defaultdict(lambda: np.zeros(action_space))

    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.randint(0, self.action_space - 1)
        else:
            return np.argmax(self.q_table[state])

    def update_q_value(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state])
        current_q = self.q_table[state][action]
        new_q = (1 - self.alpha) * current_q + self.alpha * (reward + self.gamma * self.q_table[next_state][best_next_action])
        self.q_table[state][action] = new_q

# Example usage for a gym environment (e.g., CartPole)
env = gym.make("CartPole-v1")
state_space_size = env.observation_space.shape[0]
action_space_size = env.action_space.n

agent = QLearningAgent(action_space_size)

num_episodes = 1000

for episode in range(num_episodes):
    state = env.reset()
    total_reward = 0

    while True:
        action = agent.choose_action(state)
        next_state, reward, done, _ = env.step(action)

        agent.update_q_value(state, action, reward, next_state)

        total_reward += reward
        state = next_state

        if done:
            break

    if episode % 100 == 0:
        print(f"Episode {episode}, Total Reward: {total_reward}")

# Test the trained agent
test_episodes = 10

for _ in range(test_episodes):
    state = env.reset()
    total_reward = 0

    while True:
        action = np.argmax(agent.q_table[state])
        next_state, reward, done, _ = env.step(action)

        total_reward += reward
        state = next_state

        if done:
            break

    print(f"Test Total Reward: {total_reward}")