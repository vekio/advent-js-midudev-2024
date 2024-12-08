# It's time to select the fastest reindeer for Santa's journeys! 🦌🎄
# Santa Claus has organized exciting reindeer races to determine which ones are in the best shape.

# Your task is to display each reindeer's progress on a snow track in isometric format.

# The information you receive:

# indices: An array of integers representing each reindeer's progress on the track:
# 0: The lane is empty.
# Positive number: The reindeer's current position from the beginning of the track.
# Negative number: The reindeer's current position from the end of the track.
# length: The length of each lane.
# Return a string representing the race track:

# Each lane has exactly length positions filled with snow (~).
# Each reindeer is represented with the letter r.
# Lanes are numbered at the end with /1, /2, etc.
# The view is isometric, so the lower lanes are shifted to the right.


def draw_race(indices, length):
    lanes = []
    for i, p in enumerate(indices):
        space = " " * (len(indices) - i - 1)
        snow = "~" * (length)
        if p > 0:
            snow = snow[:p] + "r" + snow[p + 1 :]
        if p < 0:
            p = abs(p)
            snow = snow[p:] + "r" + snow[: p - 1]
        lane = space + snow + f" /{i+1}"
        lanes.append(lane)
    result = "\n".join(lanes)
    return result


# print(draw_race([2, -1, 0, 5], 8))
print(draw_race([0, 5, -3], 10))
