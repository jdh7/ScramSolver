unplaced = [[-1,-3,-4,-2],
            [1,2,3,4],
            [4,-1,-4,-2],
            [1,-3,-2,4],
            [-3,-1,-2,-4],
            [-2, 3, -1,1],
            [3,2,-1,4],
            [3,-4,2,-3],
            [-2,-1,-3,3]]
unplacedDeep = [[-1,-3,-4,-2],
            [1,2,3,4],
            [4,-1,-4,-2],
            [1,-3,-2,4],
            [-3,-1,-2,-4],
            [-2, 3, -1,1],
            [3,2,-1,4],
            [3,-4,2,-3],
            [-2,-1,-3,3]]

def orientation(carD):
    myOrder = [1, 2, 3, 0]                              
    NewOrder = [carD[i] for i in myOrder]
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
    checkS = [e for e in solutions]
    checkS.append(string)
    if checkS in snapshot:
        return False
    else:
        return True

# def UsedCheck(lizt, zsolution):
#     czeck = []
#     for a, _ in zsolution:
#         czeck.append(a)
#     if lizt in czeck:
#         return False
#     else:
#         return True 

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

attppp = 0
answers = [0,0,0,0,0,0,0,0,0]

for i in range(len(unplaced)):
    solution = [[unplacedDeep[i], 0]]
    solutionDeep = [unplacedDeep[i]]                                 
    strnger = int(str(1)+str(i))
    solvisited = [strnger]
    snapshot = []
    cycles = -1
    print("Attempts:", attppp, "Solution length", len(solution), "i piece:", i, unplacedDeep[i], answers)

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
                    attppp += 1

                    if (EdgeCheck(unplaced[j]) == True) and UsedSolCheck(Stringer, solvisited) and UsedCheck(unplacedDeep[j], solutionDeep):
                        # pdb.set_trace()
                        
                        # print(f'solvisited is {solvisited}')
                        # print(f'snapshot is {snapshot}')
                        # print(f'j is {j} and potential card is: {unplaced[j]} deepcopy is: {unplacedDeep[j]}')
                        # print(f'solution is: {solution}')
                        # print(f'EdgeCheck is {EdgeCheck(unplaced[j])}')
                        # print(f'UsedSolCheck is {UsedSolCheck(Stringer, solvisited)}')
                        # print(f'UsedCheck is {UsedCheck(unplacedDeep[j], solution)}')
                        # print("EdgeCheck =",EdgeCheck(unplaced[j]) and UsedSolCheck(Stringer, solvisited) and UsedCheck(unplacedDeep[j], solution))
                        
                        x = unplaced[j]
                        goodCard = [x,n]
                        solution.append(goodCard)
                        solutionDeep.append(unplacedDeep[j])
                        solvisited.append(Stringer)
                        cycles = 0
                        answers[len(solution)-1] += 1

                    else:
                        unplaced[j] = orientation((unplaced[j]))
                    
                    if len(solution) == 9:
                        print("attempts:", attppp, "Solution Found:", solution, "\n", solutionDeep)
                        break 

                if cycles == 8:
                    # if len(solution) > 7:
                    #     pdb.set_trace()
                    #     print("\n\n","*****prePOP*****")
                    #     print("prepop snap:", snapshot)
                    #     print("solvisited:", solvisited) 
                    #     print("Solution so far:", solution)
                    #     print("\n")

                    snapshot.append([e for e in solvisited])
                    solvisited = solvisited[:-1]
                    solution.pop()
                    solutionDeep.pop()
                    cycles = -1

                    # if len(solution) > 7:
                    #     print("$$$$ Popped $$$$")
                    #     print("pop snap:", snapshot)
                    #     print("pop solvisited:", solvisited) 
                    #     print("pop Solution so far:", solution)
                    #     print("\n")
                    #     #pdb.set_trace()
                    #  
