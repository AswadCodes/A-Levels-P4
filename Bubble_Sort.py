Number = [5,2,1,55,70,14,20]

def BubbleSort():
    No_Swaps = False
    Boundary = len(Number)-1

    while No_Swaps == False:
        No_Swaps = True

        for i in range(Boundary):
            if Number[i] < Number[i+1]: # Descending order
                Temp = Number[i]
                Number[i] = Number[i+1]
                Number[i+1] = Temp
                No_Swaps = False
        Boundary = Boundary - 1


BubbleSort()
print(Number)