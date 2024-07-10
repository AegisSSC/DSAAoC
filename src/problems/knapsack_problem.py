# https://sites.google.com/site/mytechnicalcollection/algorithms/dynamic-programming/knapsack-problem
# Knapsack Problem

# • You have a knapsack that has capacity (weight) C.

# • You have several items I1,…,In.

# • Each item Ij has a weight wj and a benefit bj.

# • You want to place a certain number of copies of each item Ij in the knapsack so that:

# – The knapsack weight capacity is not exceeded and

# – The total benefit is maximal.

# Key question

# • Suppose f(w) represents the maximal possible benefit of a knapsack with weight w.

# • We want to find (in the example) f(5).

# • Is there anything we can say about f(w) for arbitrary w?

# Key observation

# • To fill a knapsack with items of weight w, we must have added items into the knapsack in some order.

# • Suppose the last such item was Ij with weight wi and benefit bi.

# • Consider the knapsack with weight (w- wi). Clearly, we chose to add Ij to this knapsack because of all items with weight wi or less, Ij had the max benefit bi.