string=list (range(10,20,2))
print(string)

team=["火箭","勇士","开拓者","雷霆","爵士","公牛","马刺","森林狼"]
for index,item in enumerate(team):
    if index%2==0:
        print(item+"\t\t",end=' ')
    else:
        print(item+"\n")