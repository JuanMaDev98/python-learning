import os
from pathlib import Path

# get the current working directory
current_working_directory = os.getcwd()

# print output to the console
print(current_working_directory)

# output will look something similar to this on a macOS system
# /Users/dionysialemonaki/Documents/my-projects/python-project




# get the current working directory
current_working_directory = Path.cwd()

# print output to the console
print(current_working_directory)

# output will look something similar to this on a macOS system
# /Users/dionysialemonaki/Documents/my-projects/python-project