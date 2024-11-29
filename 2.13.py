print("TRẦN DANH HOÀNG")
print("MSSV:235752021610064")

import cmath

# Nhập các hệ số a, b, c từ bàn phím
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Tính delta
delta = b**2 - 4*a*c

# Xử lý các trường hợp
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x = -c / b
        print(f"Nghiệm của phương trình là: x = {x}")
else:
    if delta > 0:
        x1 = (-b + cmath.sqrt(delta)) / (2*a)
        x2 = (-b - cmath.sqrt(delta)) / (2*a)
        print(f"Có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Có một nghiệm kép: x = {x}")
    else:
        real_part = -b / (2*a)
        imaginary_part = cmath.sqrt(-delta) / (2*a)
        print(f"Có hai nghiệm phức: x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i")
