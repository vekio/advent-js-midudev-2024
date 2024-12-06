# Your task is to write a function that receives a list of integers (which may include duplicates) and returns a new list without duplicates, sorted in ascending order.
def prepare_gifts(gifts):
    return sorted(set(gifts))
