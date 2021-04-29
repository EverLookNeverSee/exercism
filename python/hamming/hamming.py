def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Length of sequences must be equal")

    return sum(item_1 != item_2 for item_1, item_2 in zip(strand_a, strand_b))
