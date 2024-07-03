#Bucket Sort

def bucket_sort(arr):
    n=max(arr)
    buckets=[[] for i in range(n)]
    
    for num in arr:
        index=num//10
        buckets[index].append(num)
    
    for b in buckets:
        b.sort()

    r=[]
    for b in buckets:
        for num in b:
            r.append(num)

    return r
    

if __name__ == "__main__" :
    l=[10,50,100,35,45,23,72]
    l1=bucket_sort(l)
    print(l1)
