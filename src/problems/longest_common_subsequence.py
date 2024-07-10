# https://sites.google.com/site/mytechnicalcollection/algorithms/dynamic-programming/longest-common-subsequence
# Given two sequences, find the length of longest subsequence present in both of them. 
# A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. 
# For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. 
# So a string of length n has 2^n different possible subsequences.

# It is a classic computer science problem, the basis of diff (a file comparison program that outputs the differences between two files), and has applications in bioinformatics.

# Examples:

# LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.

# LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

# The naive solution for this problem is to generate all subsequences of both given sequences and find the longest matching subsequence. This solution is exponential in term of time complexity. 
# Let us see how this problem possesses both important properties of a Dynamic Programming (DP) Problem.