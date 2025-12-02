Number = [9,3,5,2,4,1,12]

def InsertionSort():
    # Insertion sort builds a sorted prefix one element at a time (ascending).
    Array_size = len(Number)

    for pointer in range(1, Array_size):  # pointer marks the first unsorted element
        Value_To_Insert = Number[pointer]  # value we need to insert into the sorted prefix
        Hole_Position = pointer            # current hole index where insertion may land

        # Move left while items are larger than the value we want to insert
        while Hole_Position > 0 and Number[Hole_Position - 1] > Value_To_Insert:
            Number[Hole_Position] = Number[Hole_Position - 1]  # shift larger item right
            Hole_Position = Hole_Position - 1                  # hole slides left

        # Drop the saved value into its correct position
        Number[Hole_Position] = Value_To_Insert

InsertionSort()
print(Number)
