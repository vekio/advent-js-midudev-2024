# The grinch 👹 has passed through Santa Claus's workshop! And what a mess he has made. He has changed the order of some packages, so shipments cannot be made.

# Luckily, the elf Pheralb has detected the pattern the grinch followed to jumble them. He has written the rules that we must follow to reorder the packages. The instructions are as follows:

# You will receive a string containing letters and parentheses.
# Every time you find a pair of parentheses, you need to reverse the content within them.
# If there are nested parentheses, solve the innermost ones first.
# Return the resulting string with parentheses removed, but with the content correctly reversed.


def fix_packages(packages: str) -> str:
    stack = []
    current = ""

    for char in packages:
        if char == "(":
            stack.append(current)
            current = ""
        elif char == ")":
            current = stack.pop() + current[::-1]
        else:
            current += char

    return current


text1 = "abc(def(gh)i)jk"
text2 = "a(bc)de"
text3 = "a(bc(def)g)h"
print(fix_packages(text1))
