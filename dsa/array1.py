# Given an array of integers arr[] of size N and an integer, the task is to rotate the array elements to the left by d positions.


def rotate(L, d, n):
    k = L.index(d)
    new_lis = []
    new_lis = L[k+1:]+L[0:k+1]
    return new_lis
 
 
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    N = len(arr)
 
    # Function call
    arr = rotate(arr, d, N)
    for i in arr:
        print(i, end=" ")

# Initialize a temporary array(temp[n]) of length same as the original array
# Initialize an integer(k) to keep a track of the current index
# Store the elements from the position d to n-1 in the temporary array
# Now, store 0 to d-1 elements of the original array in the temporary array
# Lastly, copy back the temporary array to the original array