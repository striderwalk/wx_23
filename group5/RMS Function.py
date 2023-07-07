import math


def rmsValue(arr, n):
    square = 0
    mean = 0.0
    root = 0.0

    Data_LB = 0
    Data_UB = 10
    for i in range(Data_LB, Data_UB):
        square += arr[i] ** 2

    # Calculate Mean
    mean = square / (float)(Data_UB)

    # Calculate Root
    root = math.sqrt(mean)

    return root


# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    print(rmsValue(arr, Data_UB))
