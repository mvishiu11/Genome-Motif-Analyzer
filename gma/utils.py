
def hamming_distance(seq1, seq2):
            """Calculates the Hamming distance between two sequences."""
            return sum(c1 != c2 for c1, c2 in zip(seq1, seq2))