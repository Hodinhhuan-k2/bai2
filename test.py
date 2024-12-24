import serial

# Kết nối với cổng COM của Arduino (thay COM3 bằng cổng của bạn)
ser = serial.Serial('COM3', 9600)

while True:
    # Đọc dữ liệu từ Arduino
    data = ser.readline().decode('utf-8').strip()  # Đọc và giải mã dữ liệu
    print(data)  # Hiển thị dữ liệu nhận được từ Arduino
