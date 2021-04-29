def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Length of sequences must be equal")

