class MagicList:
    def __init__(self):
        self.data = [0]

    def findMin(self):
        M = self.data
        mini = M[1]
        return mini

        ''' you need to find and return the smallest
            element in MagicList M.
            Write your code after this comment.
        '''

    def insert(self, E):
        M = self.data
        M.append(E)
        i=len(M)-1
        while i!=0:
            if M[i] < M[(i) // 2]:
                M[i], M[(i)// 2] = M[(i) // 2], M[i]
            i=i//2

        return M

    def deleteMin(self):
        M = self.data
        M[-1], M[1] = M[1], M[-1]
        M.remove(M[-1])
        i = 1
        if len(M) % 2 != 0:
            while 2 * i < len(M):
                if M[i] > M[2 * i]:
                    M[i], M[2 * i] = M[2 * i], M[i]
                i += 1
        else:
            while (2 * i + 1) < len(M):
                if M[i] > M[2 * i + 1]:
                    M[i], M[2 * i + 1] = M[2 * i + 1], M[i]
                i += 1

        ''' you need to delete the minimum element in
            MagicList M, so that properties of the MagicList
            are satisfied. Return M after deleting the 
            minimum element.
            Write your code after this comment.
        '''


def K_sum(L, K):
    M = MagicList()
    for i in L:
        M.insert(i)
    sum = 0
    for k in range(0, K):
        sum = sum + M.findMin()
        M.deleteMin()

    return sum

    ''' you need to find the sum of smallest K elements
        of L using a MagicList. Return the sum.
        Write your code after this comment.
    '''


if __name__ == "__main__":
    '''Here are a few test cases'''

    '''insert and findMin'''
    M = MagicList()
    M.insert(4)
    M.insert(3)
    M.insert(5)
    x = M.findMin()
    if x == 3:
        print("testcase 1 : Passed")
    else:
        print("testcase 1 : Failed")

    '''deleteMin and findMin'''
    M.deleteMin()
    x = M.findMin()
    if x == 4:
        print("testcase 2 : Passed")
    else:
        print("testcase 2 : Failed")

    '''k-sum'''
    L = [2, 5, 8, 3, 6, 1, 0, 9, 4]
    K = 4
    x = K_sum(L, K)
    if x == 6:
        print("testcase 3 : Passed")
    else:
        print("testcase 3 : Failed")