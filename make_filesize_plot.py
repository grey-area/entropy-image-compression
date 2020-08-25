import numpy as np
import matplotlib.pyplot as plt
import matplotlib
plt.style.use('dark_background')
matplotlib.rcParams.update({'font.size': 18})
from pathlib import Path
from tqdm import tqdm
from utils import lighten_color


def plot_side_frame(ax, filesizes, new_fname):
    xs = np.arange(len(filesizes)) / 30.0

    ax.plot(xs, filesizes, c=c1, lw=3.5)
    ax.scatter([xs[-1]], [filesize], c=[c1])
    ax.set_xlabel('Time')
    ax.set_ylabel('kB')
    ax.set_xlim((0, 661/30))
    ax.set_ylim((0, 1000))
    ax.set_title(f'PNG file size: {filesize} kB', fontsize=25, color=c1)

    plt.tight_layout()
    plt.savefig(new_fname, dpi=102.9)
    ax.clear()


if __name__ == '__main__':
    fig, ax = plt.subplots(1, 1, figsize=(5.4444444444444444444, 7))
    c1 = lighten_color('C0', 1.1)

    filesizes = []
    frames = sorted(list(Path('frames').glob('*.png')))
    new_dir = Path('side_frames')

    for old_fname in tqdm(frames):
        new_fname = new_dir / old_fname.name

        filesize = old_fname.stat().st_size // 1024
        filesizes.append(filesize)

        plot_side_frame(ax, filesizes, new_fname)