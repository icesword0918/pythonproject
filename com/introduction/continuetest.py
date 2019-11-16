total = 99
for number in range(1, 100):
    if number % 7 == 0:
        continue
    else:
        string = str(number)
        if string.endswith('7'):
            continue
    total -= 1
print("从1数到99共拍腿", total, "次。")
