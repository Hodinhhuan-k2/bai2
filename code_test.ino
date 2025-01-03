#include <Wire.h>
#include <LiquidCrystal_I2C.h>

int cambien = 2;         // Cảm biến kết nối với chân 2
int dem = 0;             // Biến đếm số lượng sản phẩm
int pre = HIGH;          // Biến lưu trạng thái của cảm biến trước đó

// Khởi tạo LCD với địa chỉ I2C là 0x27, kích thước màn hình 16x2
LiquidCrystal_I2C lcd(0x27, 16, 2);

// Khai báo các chân nối với mạch ULN2003
int motorPin1 = 8;
int motorPin2 = 9;
int motorPin3 = 10;
int motorPin4 = 11;

// Mảng định nghĩa các bước của động cơ bước 28BYJ-48 (4 pha)
int steps[8][4] = {
  {1, 0, 0, 0},
  {1, 1, 0, 0},
  {0, 1, 0, 0},
  {0, 1, 1, 0},
  {0, 0, 1, 0},
  {0, 0, 1, 1},
  {0, 0, 0, 1},
  {1, 0, 0, 1}
};

void setup() 
{
  Wire.begin();  // Khởi tạo I2C (không cần tham số vì sử dụng chân mặc định A4, A5)
  lcd.begin(16, 2);  // Khởi động LCD với kích thước 16x2
  lcd.backlight();  // Bật đèn nền LCD
  
  lcd.setCursor(0, 0);  // Đặt con trỏ tại vị trí dòng 0, cột 0
  lcd.print("DO AN NHOM 5"); 
  lcd.setCursor(1, 0);
  lcd.print("O An Nhom 5");
  delay(2000);  // Dừng 2 giây trước khi chuyển sang dòng tiếp theo

  lcd.clear();  // Xóa màn hình LCD
  lcd.setCursor(0, 1);  // Di chuyển con trỏ đến dòng 2, cột 0
  pinMode(cambien, INPUT);  // Đặt chân cảm biến là INPUT
  lcd.backlight();  // Bật đèn nền LCD

  // Khởi tạo các chân điều khiển động cơ bước là OUTPUT
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(motorPin3, OUTPUT);
  pinMode(motorPin4, OUTPUT);

  // Bắt đầu giao tiếp Serial để gửi dữ liệu đến máy tính
  Serial.begin(9600);
}

void loop()
{
  int giatricambien = digitalRead(cambien);  // Đọc giá trị từ cảm biến
  if (giatricambien == LOW && pre == HIGH)  // Khi cảm biến chuyển từ HIGH xuống LOW
  {
    dem = dem + 1;  // Tăng số lượng sản phẩm
    delay(200);  // Thêm một chút thời gian debounce
  }
  pre = giatricambien;  // Lưu trạng thái cảm biến hiện tại

  // Xóa dòng LCD cũ và hiển thị lại số lượng sản phẩm
  lcd.setCursor(0, 0);  // Di chuyển con trỏ về vị trí dòng 0, cột 0
  lcd.print("So luong: ");
  lcd.setCursor(10, 0);  // Di chuyển con trỏ để in số lượng
  lcd.print("  ");  // Xóa các ký tự cũ
  lcd.print(dem);  // In số lượng sản phẩm hiện tại

  // Gửi số lượng sản phẩm qua Serial Monitor (máy tính)
  Serial.print("So luong san pham: ");
  Serial.println(dem);

  // Lặp qua các bước để quay động cơ
  for (int i = 0; i < 10; i++) {  // Số bước để quay một vòng
    for (int j = 0; j < 8; j++) {
      // Cập nhật các chân điều khiển động cơ bước
      digitalWrite(motorPin1, steps[j][0]);
      digitalWrite(motorPin2, steps[j][1]);
      digitalWrite(motorPin3, steps[j][2]);
      digitalWrite(motorPin4, steps[j][3]);
      delay(1);  // Đợi một chút trước khi chuyển sang bước tiếp theo
    }
  }
}
