#Insertion sort

def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        j=i-1
        comp=arr[i]
        while(j>=0):
            if(arr[j]>comp):
                arr[j+1]=arr[j]
            else:
                break
            j=j-1
        arr[j+1]=comp

    return arr

if __name__ == "__main__" :
    l=[2,9,4,5,7]
    l1=insertion_sort(l)
    print(l1)
