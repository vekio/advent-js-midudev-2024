# ChatGPT has arrived at the North Pole and the elf Sam Elfman is working on an application for managing gifts and children.

# To enhance the presentation, he wants to create a function drawTable that receives an array of objects and converts it into a text table.

# The drawn table should represent the object data as follows:

# It has a header with the column name.
# The column name has the first letter capitalized.
# Each row should contain the values of the objects in the corresponding order.
# Each value must be left-aligned.
# Fields always leave a space on the left.
# Fields leave the necessary space on the right to align the box.


def draw_table(data: list[dict[str, str | int]]) -> str:

    keys = list(data[0].keys())
    column1 = [str(d.get(keys[0])) for d in data]
    column1.append(keys[0])
    m1 = len(max(column1, key=len))

    if len(keys) > 1:
        column2 = [str(d.get(keys[1])) for d in data]
        column2.append(keys[1])
        m2 = len(max(column2, key=len))

    separator = "+-" + "-" * m1 + "-+"
    header = f"| {keys[0].capitalize()}{' ' * (m1 + 1 - len(keys[0]))}|"
    values = []
    for c in column1[:-1]:
        values.append(f"| {c}{' ' * (m1 - len(c))} |")

    if len(keys) > 1:
        separator += "-" + "-" * m2 + "-+"
        header += f" {keys[1].capitalize()}{' ' * (m2 + 1 - len(keys[1]))}|"
        for i, c in enumerate(column2[:-1]):
            values[i] = values[i] + f" {c}{' ' * (m2 - len(c))} |"

    return (
        f"{separator}\n{header}\n{separator}\n" + "\n".join(values) + f"\n{separator}"
    )


print(
    draw_table(
        [
            {"gift": "Doll"},
            {"gift": "Book"},
        ]
    )
)
