import tools.function as f
import subprocess


def music(window=None):
    test = f.create_button(window=window, text='test', command=lambda: subprocess.call(['alsamixer', '/'], shell=True))
    test.place(x = 500, y = 400)