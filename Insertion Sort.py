# def insertion_sort(a):
#     n=len(a)
#     for i in range(1,n):
#         j=i-1
#         while j>=0:
#             if a[j+1]<a[j]:
#                 x=a[j]
#                 a[j]=a[j+1]
#                 a[j+1]=x
#             j-=1
#     return a

# a=list(map(int,input().split()))
# print(insertion_sort(a))

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