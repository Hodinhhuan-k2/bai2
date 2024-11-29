print("TRẦN DANH HOÀNG")
print("MSSV:235752021610064")

import math

def Tinh(R):
    # Kiểm tra giá trị bán kính
    if R <= 0:
        return "Giá trị bán kính không hợp lệ. Bán kính phải lớn hơn 0."
    
    # Tính chu vi và diện tích
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R**2
    
    return f"Chu vi: {chu_vi:.2f}, Diện tích: {dien_tich:.2f}"

# Nhập bán kính từ bàn phím
try:
    R = float(input("Nhập bán kính R: "))
    print(Tinh(R))
except ValueError:
    print("Giá trị nhập vào không hợp lệ. Vui lòng nhập số.")
