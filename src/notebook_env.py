import os
import sys
from pathlib import Path
import socket

# machine/server
print(
    f"\n---------------------------------\nWorking on the host: {socket.gethostname()}"
)

# Python version
print(f"\n---------------------------------\nPython version: {sys.version}")

# Python kernel
print(f"\n---------------------------------\nPython interpreter: {sys.executable}")

# set root directory
ROOT = Path.cwd().parents[0]
print(f"\n---------------------------------\nRoot (ROOT) directory is set to {ROOT}")

# set plotting font style
from matplotlib import rcParams

rcParams["font.family"] = "sans-serif"
rcParams["font.sans-serif"] = ["Arial"]
rcParams["figure.figsize"] = (12, 6)
rcParams["xtick.labelsize"] = 16
rcParams["ytick.labelsize"] = 16
rcParams["legend.fontsize"] = "large"

# set pandas display options
import pandas as pd

pd.options.display.max_rows = 999
pd.options.display.max_columns = 999

# clean namespace
del rcParams
