# It's time to put up the Christmas tree at home! 🎄 But this year we want it to be special. We're going to create a function that receives the height of the tree (a positive integer between 1 and 100) and a special character to decorate it.

# The function should return a string that represents the Christmas tree, constructed as follows:

# The tree is made up of triangles of special characters.
# The spaces on the sides of the tree are represented with underscores _.
# All trees have a trunk of two lines, represented by the # character.
# The tree should always have the same length on each side.
# You must ensure the tree has the correct shape using line breaks \n for each line.


def create_xmas_tree(height, ornament):
    branches = [
        "_" * (height - layer - 1) + f"{ornament}" * (layer) for layer in range(height)
    ]
    # Construir el árbol combinando cada rama con su imagen espejo
    tree = [f"{b}{ornament}{b[::-1]}" for b in branches]
    trunk = "_" * (height - 1) + "\u0023" + "_" * (height - 1)
    complete = "".join(tree) + "\n" + trunk + "\n" + trunk
    return complete


print(create_xmas_tree(5, "+"))
