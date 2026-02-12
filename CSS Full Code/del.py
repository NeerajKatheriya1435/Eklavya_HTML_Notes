from Bio.Align import PairwiseAligner

aligner = PairwiseAligner()

seq1 = "ATGCTATGCTTTAAA"
seq2 = "ATGCAGCTTAAATTA"

alignments = aligner.align(seq1, seq2)

# print(alignments[0])
# alignment = alignments[0]
# print("Score:", alignment)

# aligner.match_score = 1
# aligner.mismatch_score = -1
# aligner.open_gap_score = -2
# aligner.extend_gap_score = -0.5
print(alignments[0])

