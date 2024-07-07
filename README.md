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
   git clone https://github.com/moelhaj996/Taxi-gam.git
Install Dependencies
sh
Copy code
pip install -r requirements.txt
Running the Game
Navigate to the game directory and run the following command:

sh
Copy code
python main.py
Sounds
Ensure the sound files (thrust.wav, land.wav, game_over.wav) are located in the assets/sounds directory as specified in the code.

## Sound Credits
All sound effects used in this game were sourced from  Freesound.org.

## Image Credits
All images are sourced from OpenGameArt.
## Acknowledgements
This project was assisted by using ChatGPT, a language model developed by OpenAI.
ChatGPT was used to check and improve the code quality.
Requirements
Python 3.x
Pygame
Type Annotations
The code includes type annotations for better code quality and readability.

Continuous Integration:
This project uses Continuous Integration to ensure code quality and functionality.

Setting Up CI
The CI is configured using GitHub Actions. The configuration file is located at .github/workflows/python-app.yml.




This structure includes:

- `.github/workflows/python-app.yml` - GitHub Actions workflow for continuous integration.
- `assets/` - Directory containing game assets.
  - `images/` - Images used in the game.
    - `taxi.png`, `platform.png`, `background.png` - Image files.
  - `sounds/` - Sound files used in the game.
    - `thrust.wav`, `land.wav`, `game_over.wav` - Sound files.
- `tests/` - Directory containing test files.
  - `__init__.py`, `test_game.py` - Test scripts.
- `main.py` - Main script to run the game.
- `requirements.txt` - List of dependencies.
- `README.md` - Project documentation.

