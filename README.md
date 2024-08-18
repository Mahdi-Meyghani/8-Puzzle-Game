# 8-Puzzle Game

## Overview

This is an implementation of the **8-puzzle game** written in Python using the `tkinter` library for the graphical user interface. The objective of the game is to arrange the tiles in a specific order by sliding them into the empty space. The game starts by displaying the correct order of tiles, and then the player shuffles the puzzle and begins solving it.

## How to Play

1. **Start the Game:** Run the application, and the initial state of the puzzle will be shown, displaying the target configuration that the player must achieve.
2. **Shuffle the Puzzle:** Press the "Shuffle" button to randomize the tiles' positions. Once shuffled, the player can begin solving the puzzle.
3. **Move the Tiles:** Click on any valid adjacent tile (next to the empty space) to slide it into the empty space. Only tiles adjacent to the empty space can be moved.
4. **Invalid Moves:** If you attempt to click on a tile that cannot be moved (i.e., not adjacent to the empty space), a message box will appear saying "You pressed an invalid button."
5. **Win Condition:** When the puzzle is successfully solved, a message box will pop up congratulating you with the message "You win!".
6. **Executable Version:** There is also a precompiled `.exe` file of the game included in the `exe-(Easy)` folder. This is an easy version of the game that becomes harder after the second shuffle.

## What is the 8-Puzzle Game?

The 8-puzzle game consists of a 3x3 grid with eight numbered tiles and one empty space. The goal is to move the tiles by sliding them into the empty space to achieve a specific target configuration, typically arranging the numbers in ascending order from 1 to 8, with the empty space in the bottom-right corner.

### Rules of the Game:

- Only tiles adjacent to the empty space can be moved.
- The player can shuffle the puzzle to randomize the tiles at the beginning of the game.
- The puzzle is considered solved when the tiles are arranged in the target configuration.

The game is a well-known challenge in artificial intelligence and algorithm development because of its combinatorial nature, requiring logical thinking and sometimes the use of heuristic algorithms to solve more complex versions.

## Installation and Execution

### Requirements

To run the Python version of the game, you will need:

- Python 3.x
- tkinter library (usually comes pre-installed with Python)

### Running the Game

1. Clone or download this repository to your local machine.
```bash
git clone <repository_url>
```

2. Navigate to the directory containing the game files.
```bash
cd 8-puzzle-game
```

3. Run the game with the following command:
```bash
python main.py
```
Alternatively, if you want to play the compiled `.exe` version:

1. Navigate to the `exe-(Easy)` folder.
2. Run the `.exe` file directly by double-clicking it.

> **Note:** The first shuffle in the `.exe` version is easy, but next ones are difficult.

### Enjoy the Game!
We hope you enjoy solving the 8-puzzle! Whether you're playing the easy or hard version, this classic puzzle game offers a satisfying challenge for players of all levels.
