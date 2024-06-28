# Space Taxi Game

Welcome to the Space Taxi Game! This README file provides instructions on how to set up, run, and play the game.

## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Running the Game](#running-the-game)
5. [Game Controls](#game-controls)
6. [Game Mechanics](#game-mechanics)
7. [Assets](#assets)
8. [Troubleshooting](#troubleshooting)

## Introduction
Space Taxi is a 2D arcade-style game where you control a taxi navigating through space. Your objective is to land safely on platforms while managing fuel and avoiding obstacles.

## Prerequisites
Before running the game, ensure you have the following installed on your system:
- Python 3.6 or higher
- Pygame library

## Installation
1. **Clone the repository:**
    ```sh
    git clone https://github.com/moelhaj996/Taxi-gam.git
    cd Taxi-gam
    ```

2. **Install the Pygame library:**
    ```sh
    pip install pygame
    ```

3. **Ensure the asset files are in the correct directory:**
    The sound files (`thrust.wav`, `land.wav`, `game_over.wav`) should be located in the `assets/sounds` directory.

Game Controls
UP Arrow: Thrust upward
LEFT Arrow: Thrust left
RIGHT Arrow: Thrust right
Game Mechanics
Gravity: Constantly pulls the taxi downwards.
Thrust: Use the arrow keys to apply thrust and navigate.
Fuel: Limited fuel supply. Manage it wisely to avoid running out.
Platforms: Land on red platforms to refuel and gain points.
Game Over: If you fall off the screen or run out of fuel, the game ends.
Assets
Ensure the following sound files are present in the assets/sounds directory:

thrust.wav
land.wav
game_over.wav
Troubleshooting
Sound Issues: If sound files fail to load, check the paths and ensure the files are in the correct directory.
Game Crashes: Ensure you have the correct version of Python and Pygame installed.
For further assistance, feel free to open an issue on the GitHub repository.

Enjoy the game! 🚀
