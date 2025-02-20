# Space Taxi Game

## Description

Space Taxi is a simple game where you control a taxi that moves up and down on the screen. Your objective is to land on platforms and avoid falling off the screen. Each successful landing on a platform increases your score.

## How to Play

1. **Launch the Game**
   - Run the game script to start the game. Ensure you have Python and Pygame installed.

2. **Control the Taxi**
   - The taxi moves up and down automatically.
   - Use the left and right arrow keys to move the platforms horizontally.

3. **Scoring**
   - Land the taxi on the red platforms to increase your score.
   - Each successful landing on a platform adds to your score.

4. **Game Over**
   - The game ends if the taxi falls off the bottom of the screen.
   - When the game is over, a "Game Over" message will be displayed.

## Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/moelhaj996/Space-Taxi-Game
## Install Dependencies

pip install -r requirements.txt



## Sound Credits
All sound effects used in this game were sourced from  Freesound.org.

## Image Credits
All images are sourced from OpenGameArt.
## Acknowledgements
This project was assisted by using ChatGPT,it was used to check and improve the code quality.
Requirements
Python 3.x
Pygame
Type Annotations
The code includes type annotations for better code quality and readability.

## Continuous Integration:
This project uses Continuous Integration to ensure code quality and functionality.

## Setting Up CI
The CI is configured using GitHub Actions. The configuration file is located at .github/workflows/python-app.yml.



# Project Directory Structure

```mermaid
graph TD
    A[project/] --> B[.github/]
    B --> C[workflows/]
    C --> D[python-app.yml]
    A --> E[assets/]
    E --> F[images/]
    F --> G[taxi.png]
    F --> H[platform.png]
    F --> I[background.png]
    E --> J[sounds/]
    J --> K[thrust.wav]
    J --> L[land.wav]
    J --> M[game_over.wav]
    A --> N[tests/]
    N --> O[__init__.py]
    N --> P[test_game.py]
    A --> Q[main.py]
    A --> R[requirements.txt]
    A --> S[README.md]
