#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        pass
    
    def selectionSort(self, arr,n):
        for i in range(n):
            for j in range(i + 1, n):
                if arr[j] < arr[i]:
                    arr[j],arr[i] = arr[i], arr[j]