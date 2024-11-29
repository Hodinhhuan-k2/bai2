print("TRẦN DANH HOÀNG")
print("MSSV:235752021610064")

def count_letters_and_digits(sentence):
     """Đếm số chữ cái và số chữ số trong câu."""
     letters_count = sum(c.isalpha() for c in sentence)
     digits_count = sum(c.isdigit() for c in sentence)

     return letters_count, digits_count
input_sentence = input("Nhâp câu: ")
letters, digits = count_letters_and_digits(input_sentence)
print(f"số chữ cái là: {letters}")
print(f"số chữ số là: {digits}")
