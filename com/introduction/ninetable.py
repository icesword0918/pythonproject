for i in range(1, 10):
    for j in range(1, i + 1):
        print(str(j) + "*" + str(i) + "=" + str(j * i) + "\t", end=' ')
    print('')  # 换行
