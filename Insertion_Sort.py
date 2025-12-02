Number = [9,3,5,2,4,1,12]

def InsertionSort():
    Array_size = len(Number)

    for pointer in range(1, Array_size):
        # Making a temp variable which is to be inserted at correct position
        Value_To_Insert = Number[pointer]
        # Making Hole_Position (Correct position that we are trying to find)
        Hole_Poisition = pointer 

        # Conditional Loop for Shifting and finding correct position

        while Hole_Poisition > 0 and Number[Hole_Poisition - 1] > Value_To_Insert:

            # Shifting
            # Hole Position Decrement

            Number[Hole_Poisition] = Number[Hole_Poisition - 1]
            Hole_Poisition = Hole_Poisition - 1
        
        Number[Hole_Poisition] = Value_To_Insert

InsertionSort()
print(Number)