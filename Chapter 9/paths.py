# Write your code here :-)
from pathlib import Path
import os

print(Path.cwd())
print(Path.cwd().is_absolute())
print(os.path.abspath('.'))
