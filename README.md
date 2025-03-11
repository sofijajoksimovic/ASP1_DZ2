# ASP1_DZ2: Stablo pretrage (Decision tree)

## Description
This project is an implementation of solving Einstein's Riddle using a decision tree. 
A decision tree is used to explore and eliminate possibilities until the solution that satisfies all conditions is reached.

## Features
- **Tree Representation**: The puzzle is represented as a tree structure, where each node contains a possible state of the game.
- **Input Method**: Players can provide input either via standard input or from a file.
- **Validation**: Players can validate whether their selected pairs of terms are correct and check whether the current state is valid.
- **Hints**: The game provides hints to help the player solve the puzzle.
- **Multiple Solutions**: The game can have multiple solutions, and players can view different possible paths leading to the solution.

## Requirements
- Python 3.x
- No external libraries are required for running this project.

## Usage

### Running the Game

1. **Start the Game**:  
   The game allows you to input data either through standard input or a file. After selecting the input method, the game will prompt you for further data to start the game.

2. **Select Actions**:  
   Once the game begins, you can perform several actions:
   
   - **Option 1**: View the entire tree structure of the game.
   - **Option 2**: View all unique solutions and paths to reach them.
   - **Option 3**: Start the game by making moves to match terms.
   - **Option 4**: Exit the game.

3. **Game Loop**:  
   During gameplay, you will be prompted to select pairs of terms to match. The game will check whether your choices are valid and whether you're on the right path toward a solution.

4. **Hints**:  
   If you're stuck, you can ask for a hint. The game will try to provide assistance based on the current state.

5. **End the Game**:  
   You can exit the game at any time or finish it by solving the puzzle.
