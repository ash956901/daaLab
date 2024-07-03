#Merge sort
def merge(arr,start,mid,end):
    first=arr[start:mid+1]
    second=arr[mid+1:end+1]

    i=0
    j=0
    k=start

    while(i<(len(first)) and j<(len(second))):
        if(first[i]<second[j]):
            arr[k]=first[i]
            i+=1
            
        elif(second[j]<first[i]):
            arr[k]=second[j]
            j+=1
        else:
            arr[k]=first[i]
            arr[k]=second[j]
            i+=1
            j+=1
        k+=1

    while(i<(len(first))):
        arr[k]=first[i]
        i+=1
        k+=1
    while(j<(len(second))):
        arr[k]=second[j]
        j+=1
        k+=1
    

def merge_sort(s,e,arr):
    if(s>=e):
        return 
    
    mid=(s+e)//2

    merge_sort(s,mid,arr)

    merge_sort(mid+1,e,arr)

    merge(arr,s,mid,e)


if __name__ == "__main__" :
    l=[10,50,100,35,45,23,72]
    merge_sort(0,len(l)-1,l)
    print(l)
