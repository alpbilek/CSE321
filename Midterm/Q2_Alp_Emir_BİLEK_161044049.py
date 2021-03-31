def absent(array):
    length=len(array)-1
    desired_sum=(length+1)*(length+2)/2
    sum_arr=sum(array)
    return int(desired_sum-sum_arr)

def Absent_Integer(arr):
    leng=len(arr[0])
    size=len(arr)-1
    for i in range(0,size):
        if (arr[i][leng-1]+arr[i+1][leng-1]) %2 ==0:
            return i + 1


def main():
    array=[0b0000,0b0001,0b0010,0b0011,0b0101]
    print("If given input array isn't sorted,answer is:",absent(array))
    arr2=[[0,0,0,0,0],[0,0,0,0,1],[0,0,0,1,0],[0,0,0,1,1],[0,0,1,0,1]]
    print("If given input array is sorted,answer is:",Absent_Integer(arr2))
main()

