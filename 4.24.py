print("TRẦN DANH HOÀNG")
print("MSSV:235752021610064")

input_str = input("Nhập vào một câu: ")
upper_count = 0
lower_count = 0
for char in input_str:
    if char.isupper():  
        upper_count += 1
    elif char.islower():  
        lower_count += 1

print(f"Chữ hoa: {upper_count}")
print(f"Chữ thường: {lower_count}")
