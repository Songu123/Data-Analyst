print("Các số tự nhiên lẻ có ba chữ số tạo thành cấp số cộng:")
for num in range(100, 1000, 2):  # Chỉ xét số lẻ
    a = num // 100               # chữ số hàng trăm
    b = (num // 10) % 10         # chữ số hàng chục
    c = num % 10                 # chữ số hàng đơn vị
    if 2 * b == a + c:
        print(num)
