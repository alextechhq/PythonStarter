import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Define constants for the grid
GRID_SIZE = 5  # 5x5 grid

# Define robot directions
DIRECTIONS = ["UP", "RIGHT", "DOWN", "LEFT"]

class RobotWorld:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = np.zeros((grid_size, grid_size))
        self.robot_position = [0, 0]  # Start in the top-left corner
        self.robot_direction = 0  # Facing UP

        # Create the figure and axes for the grid
        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        self.ax.set_xlim(-0.5, self.grid_size - 0.5)
        self.ax.set_ylim(-0.5, self.grid_size - 0.5)
        self.ax.set_aspect('equal')

        # Remove axis ticks and labels
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])

        plt.gca().invert_yaxis()

        # Draw the grid
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                self.ax.add_patch(
                    patches.Rectangle(
                        (y - 0.5, x - 0.5), 1, 1, fill=False, edgecolor="black", linewidth=0.8
                    )
                )

        self.robot_directions = ['^', '>', 'v', '<']
        self.robot_text = None
        self.item_texts = []
        self.items_placed = 0  # Track number of items placed
        self.items_picked_up = 0  # Track number of items picked up

    def place_item(self, x, y):
        self.grid[x][y] = 1  # Place an item
        self.items_placed += 1  # Increment placed item count
        self.item_texts.append(
            self.ax.text(
                y, x, 'O', ha='center', va='center', fontsize=16, color='green'
            )
        )

    def update_display(self):
        # Clear robot from previous position
        if self.robot_text:
            self.robot_text.remove()

        # Draw robot at current position
        x, y = self.robot_position
        self.robot_text = self.ax.text(
            y, x, self.robot_directions[self.robot_direction],
            ha='center', va='center', fontsize=16, color='red'
        )
        self.fig.canvas.draw_idle()
        plt.pause(0.01)

    def move(self):
        x, y = self.robot_position
        if DIRECTIONS[self.robot_direction] == "UP" and x > 0:
            self.robot_position[0] -= 1
        elif DIRECTIONS[self.robot_direction] == "RIGHT" and y < self.grid_size - 1:
            self.robot_position[1] += 1
        elif DIRECTIONS[self.robot_direction] == "DOWN" and x < self.grid_size - 1:
            self.robot_position[0] += 1
        elif DIRECTIONS[self.robot_direction] == "LEFT" and y > 0:
            self.robot_position[1] -= 1
        self.update_display()

  

    def pick_up(self):
        x, y = self.robot_position
        if self.grid[x][y] == 1:
            self.grid[x][y] = 0
            self.items_picked_up += 1  # Increment picked-up item count
            print("Picked up an item!")
            # Remove the corresponding text
            for item_text in self.item_texts:
                if item_text.get_position() == (y, x):
                    item_text.remove()
                    self.item_texts.remove(item_text)
                    break
        else:
            print("No item to pick up here.")
        self.update_display()

        # Check if all items have been picked up
        if self.items_picked_up == self.items_placed:
            self.success()  # Trigger success message when all items are picked up

 

# Interactive Loop
if __name__ == "__main__":
    world = RobotWorld(GRID_SIZE)

    print("Welcome to the Robot Simulator!")
    print("Commands: move, turn_left, pick_up, go_path, quit")

    # Initialize display
    world.update_display()

    while True:
        command = input("Enter command: ").strip().lower()
        if command == "move":
            world.move()
        elif command == "turn_left":
            world.turn_left()
        elif command == "go_path":
            world.go_path()
        elif command == "pick_up":
            world.pick_up()
        elif command == "quit":
            print("Exiting the simulator. Goodbye!")
            plt.close(world.fig)
            break
        else:
            print("Unknown command. Try: move, turn_left, pick_up, quit")
