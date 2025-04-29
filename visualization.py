from copy import deepcopy

def visualize(grid, robots):
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    fig2 = plt.figure(figsize=(12, 9))
    plt.grid(False)
    plt.xticks(range(len(grid[0])))
    plt.yticks(range(len(grid)))

    frames = []
    n = max([len(robot.path) for robot in robots])

    # Copy the grid and mark goal locations with a specific value (-1)
    goal_marked_grid = deepcopy(grid)
    for robot in robots:
        goal = robot.dst
        goal_marked_grid[goal.y][goal.x] = -1  # Unique value for goals

    for j in np.arange(n):
        frame = deepcopy(goal_marked_grid)
        for i, robot in enumerate(robots):
            if j < len(robot.path):
                frame[robot.path[j].y][robot.path[j].x] = i + 2
            else:
                frame[robot.path[-1].y][robot.path[-1].x] = i + 2

        im = plt.imshow(frame, interpolation='nearest', cmap='viridis')
        frames.append((im,))

    ani = animation.ArtistAnimation(fig2, frames, interval=200, repeat_delay=0, blit=False)

    plt.rcParams['animation.ffmpeg_path'] = 'D:\\SOFT\\ffmpeg\\bin\\ffmpeg'
    FFwriter = animation.FFMpegWriter()
    # ani.save('im.mp4', writer=FFwriter, fps=30)
    plt.show()


def outlinePath(grid, robots):
    import matplotlib.pyplot as plt

    fig3 = plt.figure(figsize=(12, 9))
    plt.grid(False)
    plt.xticks(range(len(grid[0])))
    plt.yticks(range(len(grid)))

    outline = deepcopy(grid)
    n = max([len(robot.path) for robot in robots])

    # Show base grid
    plt.imshow(outline, interpolation='nearest', cmap='viridis')

    for i, robot in enumerate(robots):
        xCoords = []
        yCoords = []
        for j in range(n):
            if j < len(robot.path):
                xCoords.append(robot.path[j].x)
                yCoords.append(robot.path[j].y)

        plt.plot(xCoords, yCoords, color='yellow', linewidth=2, label=robot.name)

        # Mark the goal
        plt.scatter(robot.dst.x, robot.dst.y, color='red', marker='*', s=200, edgecolors='black', zorder=5)

    plt.legend()
    plt.show()
