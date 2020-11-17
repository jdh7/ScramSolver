import copy
print("Welcome to Scram Solver. This program requires numerical conversions
        of picture halves found on individual scramble square picture pieces
        and returns the solved puzzle."\n)
print("Determine the four sets of pairs on the scramble square pieces and 
        assign each half an integer from -4 to 4. Enter each integer of the
        card when prompted from top -> right -> bottom -> left.")
ue1 = list(map(int,input("Please insert the first card (TRBL):").split()))
ue2 = list(map(int,input("Please insert the second card (TRBL):").split()))
ue3 = list(map(int,input("Please insert the third card (TRBL):").split()))
ue4 = list(map(int,input("Please insert the fourth card (TRBL):").split()))
ue5 = list(map(int,input("Please insert the fifth card (TRBL):").split()))
ue6 = list(map(int,input("Please insert the sixth card (TRBL):").split()))
ue7 = list(map(int,input("Please insert the seventh card (TRBL):").split()))
ue8 = list(map(int,input("Please insert the eighth card (TRBL):").split()))

# unplaced = [[-1,-3,-4,-2],
#             [1,2,3,4],
#             [4,-1,-4,-2],
#             [1,-3,-2,4],
#             [-3,-1,-2,-4],
#             [-2, 3, -1,1],
#             [3,2,-1,4],
#             [3,-4,2,-3],
#             [-2,-1,-3,3]]

unplaced = [eu1, ue2, ue3, ue4, ue5, ue6, ue7, ue8]

unplacedDeep = copy.deepcopy(unplaced)

def orientation(piece):
    myOrder = [1, 2, 3, 0]                              
    NewOrder = [piece[i] for i in myOrder]
    return NewOrder                          


def EdgeCheck(potentialcard):  # takes the current card orientation as argument

    if len(solution) == 1: #1
        if potentialcard[0] + solution[0][0][2] == 0:   # checked
            return True
        else:
            return False
    if len(solution) == 2: #2
        if potentialcard[1] + solution[1][0][3] == 0:   # checked
            return True
        else:
            return False
    if len(solution) == 3: #3                    # checked
        if potentialcard[1] + solution[0][0][3] == 0 and potentialcard[2] + solution[2][0][0] == 0:
            return True
        else:
            return False
    if len(solution) == 4: #4
        if potentialcard[2] + solution[3][0][0] == 0:   # checked
            return True
        else:
            return False
    if len(solution) == 5: #5                   # checked
        if potentialcard[3] + solution[4][0][1] == 0 and potentialcard[2] + solution[0][0][0] == 0:
            return True
        else:
            return False
    if len(solution) == 6: #6                   # checked
        if potentialcard[3] + solution[5][0][1] == 0:
            return True
        else:
            return False
    if len(solution) == 7: #7                   # checked
        if potentialcard[0] + solution[6][0][2] == 0 and potentialcard[3] + solution[0][0][1] == 0:
            return True
        else:
            return False
    if len(solution) == 8: #8                   # checked
        if potentialcard[0] + solution[7][0][2] == 0 and potentialcard[3] + solution[1][0][1] == 0:
            return True
        else:
            return False


def UsedSolCheck(string, solutions):
    checks = [e for e in solutions]
    checks.append(string)
    if checks in snapshot:
        return False
    else:
        return True

def UsedCheck(lizt, zsolution):
    czeck = []
    for a in zsolution:
        czeck.append(a)
    if lizt in czeck:
        return False
    else:
        return True 

solvisited = []
solution = []
snapshot = []

for i in range(len(unplaced)):
    solution = [[unplacedDeep[i], 0]]
    solutionDeep = [unplacedDeep[i]]                                 
    strnger = int(str(1)+str(i))
    solvisited = [strnger]
    snapshot = []
    cycles = -1
    print("Attempts:", "Solution length", len(solution), "i piece:", i, unplacedDeep[i])

    if len(solution) == 9:
        break
    
    while len(solution) >0 and len(solution) < 9:
        for a in range(2):
            unplaced = unplacedDeep[:]
            
            if len(solution) == 0 or len(solution) == 9:
                break

            for j in range(len(unplaced)):
                cycles += 1
                
                for n in range(0, 4):
                    Stringer = int(str(n+1)+str(j)+str(len(solution)))

                    if (EdgeCheck(unplaced[j]) == True) and UsedSolCheck(Stringer, solvisited) and UsedCheck(unplacedDeep[j], solutionDeep):
                        
                        x = unplaced[j]
                        goodCard = [x,n]
                        solution.append(goodCard)
                        solutionDeep.append(unplacedDeep[j])
                        solvisited.append(Stringer)
                        cycles = 0

                    else:
                        unplaced[j] = orientation((unplaced[j]))
                    
                    if len(solution) == 9:
                        print("attempts:", "Solution Found:", solution, "\n", solutionDeep)
                        break 

                if cycles == 8:

                    snapshot.append([e for e in solvisited])
                    solvisited = solvisited[:-1]
                    solution.pop()
                    solutionDeep.pop()
                    cycles = -1
