def fibonacci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    print(series)
    
terms = int(input("Enter the number of terms: "))
fibonacci_series(terms)