def rotate(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l=len(matrix)
        matrix.reverse()
        
        outer=[]
        for i in range(len(matrix)):
                inner=[]
                for j in range(len(matrix[i])):
                      
                        inner.append(matrix[j][i])
                outer.append(inner)       
        
        matrix=outer
        print(matrix)

rotate([[1,2,3],[4,5,6],[7,8,9]])


'''
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

'''
