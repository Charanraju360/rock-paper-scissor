﻿# rock-paper-scissor

# Rock-Paper-Scissors Game

## Overview
This is a simple command-line Rock-Paper-Scissors game written in Python. The player competes against the computer in a classic game of chance.

## How It Works
- The player enters their choice: `"rock"`, `"paper"`, or `"scissor"`.
- The program randomly selects one of the three items.
- The winner is determined based on the traditional rules:
  - Rock beats Scissors
  - Paper beats Rock
  - Scissors beats Paper
- If both selections are the same, it's a tie.

## Requirements
- Python 3.13 or any other version
- No additional libraries required (built-in `random` module is used)

## Running the Game
1. Open a terminal or command prompt.
2. Run the script using:
   ```sh
   python main.py
   ```
3. Follow the instructions to input your choice.
4. The program will display the computer's selection and declare the winner.

## Known Issue
- The program checks for `"scissors"` in one condition but defines `"scissor"` in the list. This might cause incorrect results. You may want to update `"scissors"` to `"scissor"` for consistency.

## Future Improvements
- Support for multiple rounds.
- Add user score tracking.
- Implement a graphical interface.

Have fun playing!
