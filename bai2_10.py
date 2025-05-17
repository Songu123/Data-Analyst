print("Các số tự nhiên có ba chữ số tạo thành cấp số nhân với công bội là số tự nhiên khác 0:")
for num in range(100, 1000):
    a = num // 100               # hàng trăm
    b = (num // 10) % 10         # hàng chục
    c = num % 10                 # hàng đơn vị
    if a != 0 and c != 0 and b * b == a * c:
        print(num)
