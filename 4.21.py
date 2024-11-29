print("TRẦN DANH HOÀNG")
print("MSSV:235752021610064")

def chia_het_cho_5(binary_str):
    decimal = int(binary_str, 2)
    return decimal % 5 == 0

input_str = input("Nhập chuỗi các số nhị phân 4 chữ số (phân tách bởi dấu phẩy): ")
binary_numbers = input_str.split(',')
result = [binary for binary in binary_numbers if chia_het_cho_5(binary)]

if result:
    print(",".join(result))
else:
    print("Không có số nhị phân nào chia hết cho 5.")
