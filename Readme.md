# PythonStarter

Welcome to **PythonStarter**! This repository contains two simple Python scripts that demonstrate basic programming concepts such as robotics simulation and random number generation.

## Getting Started

To run the scripts in this repository, you need to have **Python 3.12** (or a compatible version) installed on your system, as well as **VS Code** (Visual Studio Code) as an Integrated Development Environment (IDE). Follow the instructions below to set up the environment.

### Prerequisites

#### 1. **Install Python 3.12**
   - Visit the [official Python website](https://www.python.org/downloads/release/python-3120/) to download and install Python 3.12.
   - Follow the installation instructions based on your operating system:
     - **Windows:** Download the `.exe` installer and follow the prompts.
     - **macOS:** Download the `.pkg` installer and follow the instructions.
     - **Linux:** You can typically install Python using your package manager (e.g., `sudo apt-get install python3.12`).

   **Make sure to check the box to add Python to your system's PATH during installation.**

#### 2. **Install VS Code**
   - Download and install [Visual Studio Code (VS Code)](https://code.visualstudio.com/).
   - Once installed, open VS Code and install the **Python extension** from the marketplace for better syntax highlighting, linting, and debugging support.

### Install Dependencies

1. Open the terminal in VS Code (or your command line interface).
2. Install the required dependencies using `pip`:
   ```bash
   pip install matplotlib numpy
   ```

### Running the Scripts

#### 1. `random_number_generator.py`
This script generates a random number between a given minimum and maximum value.

**What is a function?**
A function is a block of code that performs a specific task. Functions help to organize code into reusable pieces. In Python, you define a function using the `def` keyword, followed by the function name and parentheses `()`.

**How the script works:**
1. The script defines a function called `generate_random_number` that takes two parameters: `min_value` and `max_value`.
2. Inside the function, the `random.randint` method is used to generate a random number between `min_value` and `max_value`.
3. The function returns the generated random number.
4. The script then calls this function with specific values (e.g., 1 and 100) and prints the result.

**Running the script:**

1. Open a terminal in your code editor or command line interface.
2. Navigate to the directory where `random_number_generator.py` is located.
3. Run the script by typing:
   ```bash
   python random_number_generator.py
   ```

**Example output:**
```
The randomly generated number between 1 and 100 is: 57
```

**Code explanation:**
```python
import random  # Import the random module to generate random numbers

def generate_random_number(min_value, max_value):
    """Generate a random number between min_value and max_value."""
    return random.randint(min_value, max_value)

# Define the range for the random number
min_value = 1
max_value = 100

# Generate and print the random number
random_number = generate_random_number(min_value, max_value)
print(f"The randomly generated number between {min_value} and {max_value} is: {random_number}")
```

#### 2. `moving_robot.py`
This script simulates a robot moving on a 5x5 grid. The robot can move, turn left, and pick up items. The world is visualized using matplotlib.

**Running the script:**

1. Open a terminal in your code editor or command line interface.
2. Navigate to the directory where `moving_robot.py` is located.
3. Run the script by typing:
   ```bash
   python moving_robot.py
   ```

**Commands:** Once the script is running, you'll interact with the robot using these commands:
- `move`: Moves the robot one step forward in the current direction.
- `turn_left`: Turns the robot 90 degrees to the left.
- `go_path`: The robot will turn around and move two steps forward (you can extend this functionality).
- `pick_up`: Picks up an item from the robot's current position.
- `quit`: Exits the simulator.

**Example output in the terminal:**
```
Welcome to the Karel Simulator!
Commands: move, turn_left, pick_up, quit
```

**Visual Output:** The robot's movement will be displayed on a grid in a graphical window, where:
- `^` represents the robot facing upwards.
- `>` represents the robot facing right.
- `v` represents the robot facing downwards.
- `<` represents the robot facing left.

### Customizing the Code

- **`moving_robot.py`:** You can modify the grid size and robot's behavior by editing the constants at the top of the file.
  - For example, to change the grid size, modify the `GRID_SIZE` constant.
  - To change the robot’s initial position or direction, modify `self.robot_position` and `self.robot_direction`.

- **`random_number_generator.py`:** You can change the range of random numbers by adjusting the `min_value` and `max_value` variables.

### `go_path` Assignment

The `go_path` command is currently partially implemented. Your task is to extend its functionality. Here are some ideas on how you can enhance it:

1. **Add More Movements:** Make the robot move in a specific pattern or path.
2. **Add Conditions:** Make the robot check for obstacles or items before moving.
3. **Combine Commands:** Combine multiple commands to create a more complex behavior.

**Example:**
```python
def go_path(self):
    self.turn_left()
    self.turn_left()
    self.move()
    self.move()
    # Add more movements or conditions here
    # For example, turn right and move forward
```

Feel free to experiment and add your own logic to make the robot's behavior more interesting!

### Troubleshooting

**Error: "No module named 'matplotlib' or 'numpy'":**

Ensure that you've installed the necessary dependencies:
```bash
pip install matplotlib numpy
```

**Issue with Python version:** Make sure you're using Python 3.12 or a compatible version. If you have multiple Python versions installed, you can use:
```bash
python3.12 moving_robot.py
```

### Contributing

If you'd like to contribute to this project, feel free to fork the repository, make changes, and create a pull request. We welcome improvements, bug fixes, or additional features!

### License

This repository is licensed under the MIT License. See the LICENSE file for more information.

Thank you for checking out PythonStarter. Happy coding! 🚀

### Key Updates:
- Added step-by-step instructions for running the scripts.
- Provided sample output for each script.
- Included troubleshooting steps for common issues.
- Explained how to customize the code for both scripts.

### Contact

In case of questions or problems, please just contact me under info@alextechhq.com