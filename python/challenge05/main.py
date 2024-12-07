# Santa Claus's elves 🧝🧝‍♂️ have found a bunch of mismatched magic boots in the workshop. Each boot is described by two values:

# type indicates if it's a left boot (I) or a right boot (R).
# size indicates the size of the boot.
# Your task is to help the elves pair all the boots of the same size having a left and a right one. To do this, you should return a list of the available boots after pairing them.

# Note: You can have more than one pair of boots of the same size!
shoes = [
    {"type": "I", "size": 38},
    {"type": "R", "size": 38},
    {"type": "R", "size": 42},
    {"type": "I", "size": 41},
    {"type": "I", "size": 42},
]

shoes2 = [
    {"type": "I", "size": 38},
    {"type": "R", "size": 38},
    {"type": "I", "size": 38},
    {"type": "I", "size": 38},
    {"type": "R", "size": 38},
]

shoes3 = [
    {"type": "I", "size": 38},
    {"type": "R", "size": 36},
    {"type": "R", "size": 42},
    {"type": "I", "size": 41},
    {"type": "I", "size": 43},
]

shoes4 = [
    {"type": "I", "size": 40},
    {"type": "R", "size": 40},
    {"type": "I", "size": 40},
    {"type": "R", "size": 40},
]


def organizeShoes(shoes):
    izq = [shoe for shoe in shoes if shoe["type"] == "I"]
    der = [shoe for shoe in shoes if shoe["type"] == "R"]

    result = []
    for i in izq:
        for d in der:
            if d["size"] == i["size"]:
                result.append(i["size"])
                der.remove(d)

    return result


print(organizeShoes(shoes4))
