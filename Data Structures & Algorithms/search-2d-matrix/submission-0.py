class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

    
        def search(start, end): 
            # TODO: Finish.
            print(start, end) 
            if start == end:
                return -1
            middle_ind = start + (end - start) // 2
            i, j =  middle_ind // n, middle_ind % n,
            middle = matrix[i][j]
            print(middle, middle_ind, i, j)
            if middle < target:
                return search(middle_ind + 1, end)
            elif middle > target:
                return search(start, middle_ind)
            return middle_ind
    
        return search(0, m * n) != -1
          