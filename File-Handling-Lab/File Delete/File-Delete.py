import os
try:
    os.remove("../File Writer/my_first_file.txt")
except FileNotFoundError:
    print("File aready deleted")