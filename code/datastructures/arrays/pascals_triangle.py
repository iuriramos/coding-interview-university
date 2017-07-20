def pascals_triangle(n):
    triangle = [[]]
    for num in range(n + 1):
        curr = triangle[-1]
        next = curr[:]
        j = len(next) -1
        while j >= 1:
            next[j] += next[j -1]
            j -= 1
        next.append(1)
        triangle.append(next)
    return triangle
    
def pascals_triangle_easy(n):
    if n == 0:
        return [[]]
    triangle = [[], [1]]
    for num in range(1, n + 1):
        curr = triangle[-1]
        next = [1]
        for i in range(1, len(curr)):
            next.append(curr[i] + curr[i - 1])
        next.append(1)
        triangle.append(next)
    return triangle
    
if __name__ == '__main__':
    print (pascals_triangle(5))
    print (pascals_triangle_easy(5))
