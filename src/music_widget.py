import tools.function as f
import subprocess


def music(window=None):
    f.create_button(window=window, text='test', command=lambda: subprocess.call(['alsamixer', '/'], shell=False))
