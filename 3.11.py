print("TRẦN DANH HOÀNG")
print("MSSV:235752021610064")

def benefit(t, n, k):
    # Tính số tiền nhận được sau k tháng
    total_amount = n * ((1 + t / 100) ** k)
    return total_amount

# Nhập lãi suất, số vốn và số tháng
t = float(input("Nhập lãi suất tiết kiệm (t%/tháng): "))
n = float(input("Nhập số vốn ban đầu (n): "))
k = int(input("Nhập số tháng gửi (k): "))

# Tính số tiền nhận được
result = benefit(t, n, k)
print(f"Số tiền nhận được sau {k} tháng là: {result:.2f}")
