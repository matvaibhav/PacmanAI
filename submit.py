#do not modify the function names
#You are given L and M as input
#Each of your functions should return the minimum possible L value alongside the marker positions
#Or return -1,[] if no solution exists for the given L

#Your backtracking function implementation
import time


def BT(L, M):
    "*** YOUR CODE HERE ***"

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
        #print marker
        global tracker
        tracker += 1
        if(isSafe(marker) == False):
            return
        if (len(marker) == M):
            return True;
        for i in range(j,L+1):
            marker.append(i)
            status = GolombBT(L,M,marker,i+1)
            if(status):
                return L,marker
            del marker[len(marker)-1]
        return 0
    marker = [0]
    global tracker
    tracker = 0
    marker = GolombBT(L, M, marker,1)
    print marker
    print tracker
    return marker

countOfConsistencyChecks=0

#Your backtracking+Forward checking function implementation
def FC(L, M):
    "*** YOUR CODE HERE ***"
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
        #print marker
        global tracker
        tracker+=1
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
    global tracker
    tracker = 0
    marker = [0]
    marker = GolombFC(L, M, marker,1)
    print marker
    print tracker
    return marker

#Bonus: backtracking + constraint propagation
def CP(L, M):
    "*** YOUR CODE HERE ***"
    return -1,[]

t0 = time.time()
# BT(54,10)
# BT(0,0)
FC(55,10)
t1 = time.time()
print t1-t0
# BT(6,4)
# FC(54,10)