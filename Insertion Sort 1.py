def insertion_sort(a):
    n=len(a)
    if n==1:
        return a
    else:
        return insert(insertion_sort(a[:n-1]),a[n-1])
    
def insert(a,b):
    n=len(a)
    if a[n-1]<=b:
        ans=a[:]
        ans.append(b)
    elif b<a[0]:
        ans=[b]
        ans.extend(a)
    else:
        ans=insert(a[:n-1],b)
        ans.append(a[n-1])
    return ans

a=list(map(int,input().split()))
print(insertion_sort(a))