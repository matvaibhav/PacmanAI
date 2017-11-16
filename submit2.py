#do not modify the function names
#You are given L and M as input
#Each of your functions should return the minimum possible L value alongside the marker positions
#Or return -1,[] if no solution exists for the given L

#Your backtracking function implementation
import time


def BT(L, M):
    "*** YOUR CODE HERE ***"
    # Driver function that calls the actual Bactracking function repeatedly with decreasing values of length till the optimal length is reached.
    def getGolumb(L, M):
        marker = [0]

        solution = -1, []
        if (M == 1):
            solution = 0,[0]
            return 0,[0]
        currentSolution = -9999999
        global countOfConsistencyChecks
        countOfConsistencyChecks = 0
        while (currentSolution != 0):
            marker = [0]
            currentSolution = GolombBT(L, M, marker, 1)
            if (currentSolution != 0):
                solution = currentSolution
            L = L - 1
        # print countOfConsistencyChecks
        return solution

    # The isSafe() method checks whether the current placement of markers is valid for a Golomb Ruler
    def isSafe(marker):
        diff = [0]
        for i in range(0,len(marker)):
            for j in range(i+1,len(marker)):
                if(marker[j]-marker[i] in diff):
                    return False;
                else:
                    diff.append(marker[j]-marker[i])
        return True

    def GolombBT(L,M,marker,j):
        global countOfConsistencyChecks
        countOfConsistencyChecks += 1
        if(isSafe(marker) == False):
            return
        if (len(marker) == M):
            return True;
        for i in range(j,L+1):
            marker.append(i)
            status = GolombBT(L,M,marker,i+1)
            if(status):
                return L, marker
            del marker[len(marker)-1]
        return 0
    return getGolumb(L, M)
# tracker=0


#Your backtracking+Forward checking function implementation
def FC(L, M):
    "*** YOUR CODE HERE ***"

    # Driver function that calls the actual GolombFC function repeatedly with decreasing values of length till the optimal length is reached.
    def getGolumb(L, M):
        marker = [0]

        solution = -1, []
        if (M == 1):
            solution = 0,[0]
            return 0,[0]
        currentSolution = -9999999
        while (currentSolution != 0):
            global countOfConsistencyChecks
            countOfConsistencyChecks = 0
            marker = [0]
            currentSolution = GolombFC(L, M, marker, 1)
            if (currentSolution != 0):
                solution = currentSolution
            L = L - 1

        # print countOfConsistencyChecks
        return solution

    # The isSafe() method checks whether the current placement of markers is valid for a Golomb Ruler
    def isSafe(marker):
        diff = set([0])
        for i in range(0,len(marker)):
            for j in range(i+1,len(marker)):
                if(marker[j]-marker[i] in diff):
                    return False;
                else:
                    diff.add(marker[j]-marker[i])
        return True,diff

    def GolombFC(L,M,marker,j):
        global countOfConsistencyChecks
        countOfConsistencyChecks+=1
        safe, diff = isSafe(marker)
        if(safe == False):
            return
        if (len(marker) == M):
            return True;

        for i in range(j,L+1):
            cont = False
            for elem in marker:
                if i-elem in diff:
                    cont = True;
                    break
            if(i>=L+1):
                return
            if(cont):
                continue

            marker.append(i)
            status = GolombFC(L,M,marker,i+1)
            if(status):
                return marker
            del marker[len(marker)-1]
        return 0

    return getGolumb(L, M)
#Bonus: backtracking + constraint propagation
def CP(L, M):
    "*** YOUR CODE HERE ***"
    return -1,[]

# BT(7,4)
# # BT(10,4)
# # BT(55,10)
# # BT(2,1)
# BT(6,4)

# this function can be used to run FC and BT on a sample dataset.
def testData():

    L=[6,10,25,55,60]
    M = [4, 6, 8, 10]
    print 'Backtracking statistics:'
    print 'L    M   solution    Time'
    for  i in range(len(M)):
        for j in range(len(L)):
            t0 = time.time()
            solution = BT(L[j],M[i])
            t1 = time.time()
            print L[j],'\t',M[i], '\t', solution , '\t', t1-t0

    print 'Forward Checking statistics:'
    print 'L    M   solution    Time'
    for i in range(len(M)):
        for j in range(len(L)):
            t0 = time.time()
            solution = FC(L[j], M[i])
            t1 = time.time()
            print L[j], '\t', M[i], '\t', solution, '\t', t1 - t0

# testData()
# FC(1,2)

