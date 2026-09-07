class Solution:
    def partition (self,arr,st,end):
        pivot=arr[end]
        index=st-1
        
        for j in range(st,end):
            if arr[j]<=pivot:
                index +=1
                arr[index],arr[j]=arr[j],arr[index]
        arr[index + 1],arr[end]=arr[end],arr[index + 1]
        return index + 1

    def quickSort(self,arr,st,end):
        if st<end:
            pivotIndex=self.partition(arr,st,end)
            self.quickSort(arr,st,pivotIndex-1)
            self.quickSort(arr,pivotIndex +1,end)
    
            