#!/usr/bin/python

# Native modules
import random

# Third-party modules
import scipy.misc

# User-defined modules
import soccer


def main():
  # Initialize the random number generator
  random.seed(0)

  # Create a soccer environment
  soccer_env = soccer.SoccerEnvironment()

  # Run many episodes
  for episode_ind in range(10):
    # Print the episode number
    print('')
    print('Episode {}:'.format(episode_ind + 1))
    # Reset the environment
    observation = soccer_env.reset()
    # Print the initial state
    print('Initial state:\n{}\n'.format(observation))
    # Run the episode
    is_running = True
    while is_running:
      # Render the environment
      soccer_env.render()
      # Get the screenshot
      screenshot = soccer_env.renderer.get_screenshot()
      # Take a random action
      action = random.choice(soccer_env.actions)
      observation = soccer_env.take_action(action)
      # Check the terminal state
      if soccer_env.state.is_terminal():
        print('Terminal state:\n{}'.format(observation))
        print('Episode {} ends at time step {}'.format(
            episode_ind + 1, soccer_env.state.time_step + 1))
        is_running = False
    # Save the last image
    screenshot_path = 'screenshot.png'
    scipy.misc.imsave(screenshot_path, screenshot)
    print('The last screenshot is saved to {}'.format(screenshot_path))


if __name__ == '__main__':
  main()