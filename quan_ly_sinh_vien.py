lsv = []
def nhap():
    for i in range(0,n,1):
        print('Nhập sinh viên thứ ', i + 1)
        masv = int(input('Nhập mã sinh viên: '))
        tensv = input('Nhập họ tên: ')
        lopsv = input('Nhập lớp: ')
        gioitinh = (input('Nhập giới tính sinh viên: '))
        d = {"masv":masv, "tensv":tensv, "lopsv":lopsv, "gioitinh":gioitinh}
        lsv.append(d)

def xoa():
    tk = int(input('Nhập mã sinh viên cần xóa: '))
    for i in range(0, len(lsv)):
        if lsv[i].get("masv") == tk:
            lsv.remove(lsv[i])
            print('Đã xóa sinh viên.')
        else:
            print('Không có trong danh sách sinh viên.')

def sua():
    tk = int(input('Nhập mã sinh viên cần sửa: '))
    for i in range(0, len(lsv)):
        if lsv[i].get("masv") == tk:
            masv = int(input("Nhập mã sinh viên: "))
            tensv = input('Nhập họ tên: ')
            lopsv = input('Nhập lớp: ')
            gioitinh = input('Nhập giới tính sinh viên: ')
            d = {"masv":masv, "tensv":tensv, "lopsv":lopsv, "gioitinh":gioitinh}
            lsv[i] = d
        else:
            print('Không có trong danh sách sinh viên.')

def them():
    print('Nhập thông tin sinh viên cần thêm: ')
    masv = int(input("Nhập mã sinh viên: "))
    tensv = input('Nhập họ tên: ')
    lopsv = input('Nhập lớp: ')
    gioitinh = input('Nhập giới tính sinh viên: ')
    d = {"masv":masv, "tensv":tensv, "lopsv":lopsv, "gioitinh":gioitinh}
    lsv.append(d)

def hienthi():
    print(lsv[0:])

while True:
    print('''-------------------
1. Nhập danh sách sinh viên.
2. Thêm sinh viên vào danh sách.
3. Xóa sinh viên khỏi danh sách.
4. Sửa sinh viên trong danh sách.
5. Xem danh sách sinh viên.
6. Thoát!.
------------------------''')
    chon = int(input('Vui lòng nhập lựa chọn: '))
    if chon == 1:
        n = int(input('Nhập số sinh viên: '))
        nhap()
    if chon == 2:
        them()
    if chon == 3:
        xoa()
    if chon == 4:
        sua()
    if chon == 5:
        hienthi()
    if chon == 6:
        break
    