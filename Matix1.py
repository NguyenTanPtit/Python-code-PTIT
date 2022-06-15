class Matrix:

    def __init__(self, arr):
        self.arr = arr

    def printAns(self):
        brr = []
        for i in range(len(self.arr[0])):
            tmp = []
            for j in range(len(self.arr)):
                tmp.append(self.arr[j][i])
            brr.append(tmp)
        return brr

    def mulMatrix(self):
        other_matrix = self.printAns()
        ans = []
        for i in range(len(self.arr)):
            res = []
            for j in range(len(other_matrix[0])):
                tmp = 0
                for k in range(len(self.arr[0])):
                    tmp += self.arr[i][k] * other_matrix[k][j]
                res.append(tmp)
            ans.append(res)
        return ans


def main():
    test = int(input())
    while test:
        test -= 1
        n, m = [int(i) for i in input().split()]
        arr = []
        for i in range(n):
            arr.append([int(j) for j in input().split()])
        matrix = Matrix(arr)
        matrix_ans = matrix.mulMatrix()
        for i in range(len(matrix_ans)):
            for j in range(len(matrix_ans[0])):
                print(matrix_ans[i][j], end=' ')
            print()


main()
