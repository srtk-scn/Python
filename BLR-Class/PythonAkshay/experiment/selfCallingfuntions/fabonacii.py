def fibonacci_series(n):
    series = []
    for i in range(1, n + 1):
        if i == 1:
            series.append(0)
        elif i == 2:
            series.append(1)
        else:
            series.append(series[-1] + series[-2])
    return series

# Example usage
print(fibonacci_series(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]