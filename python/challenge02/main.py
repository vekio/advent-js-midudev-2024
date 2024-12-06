# Given an array of names, you must create a rectangular frame that contains all of them.
# Each name must be on a line, aligned to the left.
# The frame is built with * and has a border one line thick.
# The width of the frame automatically adapts to the longest name plus a margin of 1 space on each side.

names = ["midu", "madeval", "educalvolpz"]


def createFrame(names):
    longest = 0
    for n in names:
        if len(n) > longest:
            longest = len(n)

    limits = "*" * (longest + 4)
    table = "\n".join([f'* {n}{" "*(longest-len(n))} *' for n in names])
    return f"{limits}\n{table}\n{limits}"


print(createFrame(names))
