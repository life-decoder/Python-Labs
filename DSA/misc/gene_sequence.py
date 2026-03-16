def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-2):
    n, m = len(seq1), len(seq2)
    
    # Initialize the matrix with zeros
    score_matrix = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill the first row and column with gap penalties
    for i in range(n + 1):
        score_matrix[i][0] = i * gap
    for j in range(m + 1):
        score_matrix[0][j] = j * gap

    # Fill the rest of the matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Calculate score for match/mismatch
            diag_score = score_matrix[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
            # Calculate score for gaps
            up_score = score_matrix[i-1][j] + gap
            left_score = score_matrix[i][j-1] + gap
            
            # The cell value is the maximum of these three possibilities
            score_matrix[i][j] = max(diag_score, up_score, left_score)

    # Traceback to find the alignment
    align1, align2 = "", ""
    i, j = n, m
    
    while i > 0 and j > 0:
        score = score_matrix[i][j]
        diag = score_matrix[i-1][j-1]
        up = score_matrix[i-1][j]
        left = score_matrix[i][j-1]

        if score == diag + (match if seq1[i-1] == seq2[j-1] else mismatch):
            align1 += seq1[i-1]
            align2 += seq2[j-1]
            i -= 1
            j -= 1
        elif score == up + gap:
            align1 += seq1[i-1]
            align2 += "-"
            i -= 1
        else:
            align1 += "-"
            align2 += seq2[j-1]
            j -= 1

    # Add remaining characters if one sequence is longer
    while i > 0:
        align1 += seq1[i-1]
        align2 += "-"
        i -= 1
    while j > 0:
        align1 += "-"
        align2 += seq2[j-1]
        j -= 1

    return align1[::-1], align2[::-1], score_matrix[n][m]

# Example Usage:
s1, s2 = "GATTACA", "GCATGCU"
a1, a2, final_score = needleman_wunsch(s1, s2)

print(f"Alignment 1: {a1}")
print(f"Alignment 2: {a2}")
print(f"Total Score: {final_score}")