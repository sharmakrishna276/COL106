def insertion_sort(a):
    n=len(a)
    for i in range(1,n):
        j=i-1
        while j>=0:
            if a[j+1]<a[j]:
                x=a[j]
                a[j]=a[j+1]
                a[j+1]=x
            j-=1
    return a

a=list(map(int,input().split()))
print(insertion_sort(a))