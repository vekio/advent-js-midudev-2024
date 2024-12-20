# Santa Claus 🎅 is checking the list of gifts he must deliver this Christmas. However, some gifts are missing, others are duplicated, and some have incorrect quantities. He needs your help to solve the problem.

# You will receive two arrays:

# received: List with the gifts Santa currently has.
# expected: List with the gifts Santa should have.
# Your task is to write a function that, given received and expected, returns an object with two properties:

# missing: An object where the keys are the names of the missing gifts and the values are the quantities that are missing.
# extra: An object where the keys are the names of the extra or duplicated gifts and the values are the quantities that are extra.
# Keep in mind that:

# Gifts may be repeated in both lists.
# The gift lists are unordered.
# If there are no missing or extra gifts, the corresponding properties (missing or extra) should be empty objects.

from collections import Counter


def fix_gift_list(received: list[str], expected: list[str]) -> dict[str, int]:
    count1 = Counter(received)
    count2 = Counter(expected)

    # Combinar claves únicas de ambos contadores
    all_items = set(count1.keys()).union(count2.keys())

    # Calcular diferencias en un solo bucle
    missing = {}
    extra = {}
    for item in all_items:
        diff = count1[item] - count2[item]
        if diff > 0:
            extra[item] = diff
        elif diff < 0:
            missing[item] = -diff

    return {"missing": missing, "extra": extra}
