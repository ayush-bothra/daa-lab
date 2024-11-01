def lcs_multiple(sequences):
    def lcs(seq1, seq2):
        dp = [[""] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]
        directions = [[None] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]
        
        for i in range(1, len(seq1) + 1):
            for j in range(1, len(seq2) + 1):
                if seq1[i - 1] == seq2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + seq1[i - 1]
                    directions[i][j] = "diag"  # Move diagonally (character match)
                elif len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                    dp[i][j] = dp[i - 1][j]
                    directions[i][j] = "up"    # Move up
                else:
                    dp[i][j] = dp[i][j - 1]
                    directions[i][j] = "left"  # Move left

        return dp[-1][-1], directions

    # Start with the LCS of the first two sequences
    max_sequence = ""
    for i in range(len(sequences)):
        common_sequence = sequences[i]
        
        for j in range(len(sequences)):
            common_sequence, directions = lcs(common_sequence, sequences[j])
            if not common_sequence:  # If common subsequence is empty, break early
                break
        max_sequence = max(max_sequence, common_sequence, key=len)

    return max_sequence, directions

# Test with given sequences
sequences = ["abcpqrs", "pqrsabc", "abcdefp"]
result, directions = lcs_multiple(sequences)
print("Longest common subsequence:", result)
print("Directions matrix:")
for row in directions:
    print(row)
