Names = ["Taha","Ali","Bano","Papoo"]
#          0      1      2      3
# len (Names) gives 4

flag = False
for x in range(len(Names)):    # start from 0 to Len of array (4) - 1 i.e 3
    if Names[x] == "Papoo":
        print("found at index : ", x)
        flag = True
if flag == False:
    print("Not found") 