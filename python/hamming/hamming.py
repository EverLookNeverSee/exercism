def distance(strand_a: str, strand_b: str) -> int:
    """
    Calculating hamming distance
    :param strand_a: str, DNA sequence
    :param strand_b: str, DNA sequence
    :return: int, number of differences
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Length of sequences must be equal")

    return sum(item_1 != item_2 for item_1, item_2 in zip(strand_a, strand_b))
