#Quick Sort
def find_pivot(s,e,arr):
    pivot=arr[s]
    i=s
    j=e
    
    while True:
        while(i<=j and arr[j]>=pivot):
            j-=1
        while(i<=j and arr[i]<=pivot):
            i+=1

        if (i<=j):
            arr[i],arr[j]=arr[j],arr[i]
        else :
            break

    arr[j],arr[s]=arr[s],arr[j]

    return j
    

def quick_sort(s,e,arr):
    if(s>=e):
        return
    
    pivot_index=find_pivot(s,e,arr)

    quick_sort(s,pivot_index-1,arr)
    quick_sort(pivot_index+1,e,arr)



if __name__ == "__main__" :
    l=[10,50,100,35,45,23,72]
    quick_sort(0,len(l)-1,l)
    print(l)
