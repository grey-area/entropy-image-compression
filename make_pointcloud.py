import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')
from tqdm import tqdm
from utils import lighten_color


class Cloud:
    def __init__(self, c1, c2, N):
        self.groups = 20
        self.group_size = N // self.groups
        self.x = np.concatenate([np.random.uniform(0, 0.5, self.group_size) if group_i % 2 == 0 else np.random.uniform(0.5, 1, self.group_size) for group_i in range(self.groups)])
        self.y = np.random.uniform(0, 1, N)
        self.vx = 0.02 * np.random.normal(size=N)
        self.vy = 0.02 * np.random.normal(size=N)
        self.colors = [c1, c2]
        self.N = N

    def update(self, dt):
        self.x += dt * self.vx
        self.y += dt * self.vy

        self.vx[np.logical_or(self.x > 1, self.x < 0)] *= -1
        self.x[self.x > 1] = 1
        self.x[self.x < 0] = 0

        self.vy[np.logical_or(self.y > 1, self.y < 0)] *= -1
        self.y[self.y > 1] = 1
        self.y[self.y < 0] = 0


def plot_frame(cloud, ax, frame_i):
    for group_i in range(cloud.groups):
        start = cloud.group_size * group_i
        end = cloud.group_size * (group_i + 1)
        ax.scatter(cloud.x[start:end], cloud.y[start:end], c=[cloud.colors[group_i % 2]], s=10)

    plt.xticks([])
    plt.yticks([])
    plt.axis('off')
    plt.xlim((0, 1))
    plt.ylim((0, 1))
    ax.set_aspect('equal')
    plt.tight_layout()

    plt.savefig(f'frames/{frame_i:04d}.png', dpi=102.9)
    ax.clear()


if __name__ == '__main__':
    N = 100000
    t_max = 22
    fps = 30
    dt = 1 / fps

    c1 = lighten_color('C0', 1.1)
    c2 = lighten_color('C3', 2.0)
    cloud = Cloud(c1, c2, N)

    fig, ax = plt.subplots(1, 1, figsize=(7, 7))

    for frame_i, t in enumerate(tqdm(np.arange(0, t_max + dt, dt))):
        plot_frame(cloud, ax, frame_i)
        cloud.update(dt)