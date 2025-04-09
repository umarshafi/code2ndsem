def merge(arr,left,mid,right):
n1=mid-left +1
n2=right-mid
l=arr[left:left+n1]
r=arr[mid+1:mid+1+n2]
i=j=0
k=left
while i<n1 and j<n2:
ifl[i]<=r[j]
arr[k]=l[i]
i+=1
else:
arr[k]=r[j]
j+=1
k+=1
else:
arr[k]=l[i]
j+=1
k+=1
whle i<n1:
arr[k]=l[i]
i+=1
k+=1