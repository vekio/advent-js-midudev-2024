# The Grinch has hacked 🏴‍☠️ Santa Claus's workshop systems and has encoded the names of all the important files. Now the elves can't find the original files and they need your help to decipher the names.

# Each file follows this format:

# It starts with a number (can contain any number of digits).
# Then has an underscore _.
# Continues with a file name and its extension.
# Ends with an extra extension at the end (which we don't need).
# Keep in mind that the file names may contain letters (a-z, A-Z), numbers (0-9), other underscores (_), and hyphens (-).

# Your task is to implement a function that receives a string with the name of an encoded file and returns only the important part: the file name and its extension.


def decode_filename(filename: str) -> str:
    without_number_arr = filename.split("_")[1:]
    without_number = "_".join(without_number_arr)
    without_dot_arr = without_number.split(".")[:-1]
    without_dot = ".".join(without_dot_arr)
    return without_dot


print(decode_filename("2023122512345678_sleighDesign.png.grinchwa"))
# ➞ "sleighDesign.png"
