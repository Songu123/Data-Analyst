words = " 1 a 5 7 f 0 89 g i 11 88 3 p"
w_new = [len(i)==2 for i in words.split()]
w_new = [i for i in words.split() if len(i)==2]
print("Danh sách có độ dài 2 kí tự: ", w_new)
print("Số lượng tập con có độ dài 2 ký tự: ", len(w_new))

