# Dữ liệu
tong_so_hoc_sinh = 40
hoc_tieng_phap = 10
hoc_tieng_anh = 14
hoc_ca_hai = 6

# Tính số học sinh học ít nhất một trong hai ngôn ngữ
hoc_mot_trong_hai = hoc_tieng_phap + hoc_tieng_anh - hoc_ca_hai

# Tính số học sinh không học ngôn ngữ nào
khong_hoc_ngon_ngu_nao = tong_so_hoc_sinh - hoc_mot_trong_hai

print("Số học sinh không học tiếng Pháp và cũng không học tiếng Anh là:", khong_hoc_ngon_ngu_nao)
