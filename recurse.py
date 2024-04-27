def tri_recursion(k):
    result = k + tri_recursion(k - 1)
    print(result)
tri_recursion(6)