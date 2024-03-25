import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define properties of the Mandelbrot set
WIDTH = 600
HEIGHT = 400
MAX_ITER = 100


# Generate the Mandelbrot set
def mandelbrot(c):
    z = c
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z * z + c
        n += 1
    if n == MAX_ITER:
        return MAX_ITER
    return n


# Create the zoom effect
def zoom(xmin, xmax, ymin, ymax, zoom=0.1):
    width = xmax - xmin
    height = ymax - ymin
    factor = zoom
    return (
        xmin + width * factor,
        xmax - width * factor,
        ymin + height * factor,
        ymax - height * factor,
    )


# Generate the frames
def generate_frames(xmin, xmax, ymin, ymax):
    r1 = np.linspace(xmin, xmax, WIDTH)
    r2 = np.linspace(ymin, ymax, HEIGHT)
    return (r1, r2, np.array([[mandelbrot(complex(r, i)) for r in r1] for i in r2]))


# Create the animation
def animate(i):
    global XMIN, XMAX, YMIN, YMAX
    XMIN, XMAX, YMIN, YMAX = zoom(XMIN, XMAX, YMIN, YMAX)
    ax.clear()
    ax.imshow(
        generate_frames(XMIN, XMAX, YMIN, YMAX)[2],
        cmap="hot",
        interpolation="bilinear",
        extent=[XMIN, XMAX, YMIN, YMAX],
    )
    plt.axis("off")


XMIN, XMAX, YMIN, YMAX = -0.9, -0.6, -0.2, 0.2
fig, ax = plt.subplots()

ani = animation.FuncAnimation(fig, animate, frames=100, interval=100)
ani.save("mandelbrot_zoom.mp4", writer="ffmpeg", fps=10)
print("Animation saved as mandelbrot_zoom.mp4")

plt.show()
