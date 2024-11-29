print("TRẦN DANH HOÀNG")
print("MSSV:235752021610064")


n = int(input("Nhập số nguyên n: "))
def fibonacci_lesser_than_n(n):
    fib = []  
    a, b = 0, 1  
    while a < n:
        fib.append(a)  
        a, b = b, a + b  
    return fib

fibonacci_numbers = fibonacci_lesser_than_n(n)
print(fibonacci_numbers)
