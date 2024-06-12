# alcemy_challenge

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Detailed Description](#detailed_description)
  
## Installation

1. Navigate to the project directory:

    ```bash
    cd alcemy_challenge
    ```

3. Install dependencies using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables (if any).

## Usage

1. Start the main.py:

    ```bash
    python main.py
    ```



## Detailed Description
Solution of this flood it problem - https://arxiv.org/abs/1001.4420
This is a game to be played from the terminal. User can enter the number of tiles n and number of colors m.
A n*n matrix will be formed with 0 to m-1 integers (where each integer represents a color) randomly assigned to each cell. 
### Automated Mode 
User can play the game in automated mode where the game will calculate the best possible move at every
iteration and show the matrix at each step and total number of moves in the end.
### User Driven Mode
In this mode, user will be given option to choose the next best possible move. If the user rejects that,
then he/she will be given an option to enter their own choice.

There are two main functions:
### flood_fill() 
This function calls itself recursively until it covers the cells connected to the origin with the color 
provided

### find_best_move() 
This function checks for every m, whether that is the best fit. It uses the find_filled_cells function
to determine the number of cells filled by a color, and it returns the number of cells filled. The maximum of all the m 
colors is then chosen for the next best move. 



