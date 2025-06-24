from grid_world import GridWorld
from q_agent import QLearningAgent

def main():
    env = GridWorld()
    agent = QLearningAgent(env)
    agent.train(episodes=1000)
    agent.test_run()

if __name__ == "__main__":
    main()
