import time, sys
from IPython.display import clear_output

def update_progress(bar_name, progress):
    bar_length = 20
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
    if progress < 0:
        progress = 0
    if progress >= 1:
        progress = 1

    block = int(round(bar_length * progress))

    clear_output(wait = True)
    text = "{0}: [{1}] {2:.1f}%".format(bar_name, "#" * block + "-" * (bar_length - block), progress * 100)
    print(text)