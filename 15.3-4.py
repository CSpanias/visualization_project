import matplotlib.pyplot as plt

from random_walk import RandomWalk

# keep making new walks, as long as the program is active
while True:
    # make a random walks
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # plot the points in the walks
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    # generate a list of numbers equal to the number of points in the walk
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=1, zorder=1)

    # emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100, zorder=2)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
     s=100, zorder=2)

    # remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
