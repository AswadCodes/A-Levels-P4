Array_Data = sorted([1,5,8,90,5,7,20,50]) 
# Must be sorted in binary searching

Lower_Bound = 0
Upper_Bound = len(Array_Data)-1
Found = False
Not_Present = False
Num_To_search = int(input("Enter the number to search"))

while Found == False and Not_Present == False:

    Mid_Point = int((Lower_Bound+Upper_Bound)/2)

    if Array_Data[Mid_Point] == Num_To_search:
        Found = True
        print("Number Found at index ", Mid_Point)
    elif Array_Data[Mid_Point] > Num_To_search:
        Upper_Bound = Mid_Point - 1
    else:
        Lower_Bound = Mid_Point + 1

    if Lower_Bound > Upper_Bound :
        Not_Present = True

if Found == False and Not_Present == False:
    print("Number not Found")