print("TRẦN DANH HOÀNG")
print("MSSV:235752021610064")

chuoi = input('Nhap chuoi: ')
chuoi_moi = ''.join([ki_tu for ki_tu in chuoi if not ki_tu.isdigit()])
print('Chuoi sau khi loai b chu so:', chuoi_moi)
