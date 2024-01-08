import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants representing cell states
ALIVE = 255
DEAD = 0


def update_cells(frame, image, board, size):
    # Create a copy of the current board to store the new state
    new_board = board.copy()

    # Iterate through each cell in the board
    for i in range(size):
        for j in range(size):
            # Calculate the sum of neighbors' states
            neighbors_sum = int((board[i, (j - 1) % size] + board[i, (j + 1) % size] +
                                 board[(i - 1) % size, j] + board[(i + 1) % size, j] +
                                 board[(i - 1) % size, (j - 1) % size] + board[(i - 1) % size, (j + 1) % size] +
                                 board[(i + 1) % size, (j - 1) % size] + board[(i + 1) % size, (j + 1) % size]) / 255)

            # Apply the rules of the Game of Life
            if board[i, j] == ALIVE:
                new_board[i, j] = DEAD if neighbors_sum < 2 or neighbors_sum > 3 else ALIVE
            else:
                new_board[i, j] = ALIVE if neighbors_sum == 3 else DEAD

    # Update the image with the new state
    image.set_array(new_board)

    # Update the original board with the new state for the next iteration
    board[:] = new_board[:]

    return image,


# Increase the scale of the board
board_size = 100
update_interval = 50

# Initialize the board with random initial state
initial_state = np.random.choice([ALIVE, DEAD], board_size * board_size, p=[0.2, 0.8]).reshape(board_size, board_size)

# Plot settings
figure, axes = plt.subplots()
plot_image = axes.imshow(initial_state, interpolation='nearest', cmap='gray_r')
animation_object = animation.FuncAnimation(figure, update_cells, fargs=(plot_image, initial_state, board_size),
                                           frames=10,
                                           interval=update_interval,
                                           save_count=50)

plt.show()
