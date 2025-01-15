import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Define constants for the grid
GRID_SIZE = 5  # 5x5 grid

# Define robot directions
DIRECTIONS = ["UP", "RIGHT", "DOWN", "LEFT"]

class KarelWorld:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = np.zeros((grid_size, grid_size))
        self.robot_position = [0, 0]  # Start in the top-left corner
        self.robot_direction = 0  # Facing UP

    def place_item(self, x, y):
        self.grid[x][y] = 1  # Place an item

    def move(self):
        x, y = self.robot_position
        print("moving")
        if DIRECTIONS[self.robot_direction] == "UP" and x > 0:
            print("mov1")
            self.robot_position[0] -= 1
        elif DIRECTIONS[self.robot_direction] == "RIGHT" and y < self.grid_size - 1:
            print("mov2")
            
            self.robot_position[1] += 1
        elif DIRECTIONS[self.robot_direction] == "DOWN" and x < self.grid_size - 1:
            print("mov3")
            
            self.robot_position[0] += 1
        elif DIRECTIONS[self.robot_direction] == "LEFT" and y > 0:
            print("mov3")
            
            self.robot_position[1] -= 1

    def turn_left(self):
        print("turning, direction: ", self.robot_direction)
        
        self.robot_direction = (self.robot_direction - 1) % 4
        print("turning, direction: ", self.robot_direction)
        

    def pick_up(self):
        x, y = self.robot_position
        if self.grid[x][y] == 1:
            self.grid[x][y] = 0
            print("Picked up an item!")
        else:
            print("No item to pick up here.")

    def display_world(self):
        plt.clf()  # Clear the previous plot
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_xlim(-0.5, self.grid_size - 0.5)
        ax.set_ylim(-0.5, self.grid_size - 0.5)
        
        # Draw grid
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                rect = patches.Rectangle((y - 0.5, x - 0.5), 1, 1, linewidth=1, edgecolor='black', facecolor='white')
                ax.add_patch(rect)
                if self.grid[x][y] == 1:
                    ax.text(y, x, 'O', ha='center', va='center', fontsize=16, color='green')
        
        # Draw robot
        x, y = self.robot_position
        robot_directions = ['^', '>', 'v', '<']
        ax.text(y, x, robot_directions[self.robot_direction], ha='center', va='center', fontsize=16, color='red')

        ax.set_xticks(range(self.grid_size))
        ax.set_yticks(range(self.grid_size))
        ax.grid(True)
        plt.gca().invert_yaxis()
        plt.pause(0.01)  # Pause to allow updates

# Interactive Loop
if __name__ == "__main__":
    plt.ion()  # Enable interactive mode
    world = KarelWorld(GRID_SIZE)

    # Place items in the world
    world.place_item(2, 2)
    world.place_item(4, 4)

    print("Welcome to the Karel Simulator!")
    print("Commands: move, turn_left, pick_up, display, quit")

    while True:
        command = input("Enter command: ").strip().lower()
        if command == "move":
            world.move()
        elif command == "turn_left":
            world.turn_left()
        elif command == "pick_up":
            world.pick_up()
        elif command == "display":
            world.display_world()
        elif command == "quit":
            print("Exiting the simulator. Goodbye!")
            plt.ioff()  # Turn off interactive mode
            break
        else:
            print("Unknown command. Try: move, turn_left, pick_up, display, quit")
