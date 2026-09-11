#a minimax algorithm
def minimax(depth,nodeIndex,isMax,scores,height):
    if depth == height:
        return scores[nodeIndex]
 
    if isMax:
        return max(minimax(depth+1,nodeIndex*2,False,scores,height),
                   minimax(depth+1,nodeIndex*2 + 1,False,scores,height))
 
    else:
        return min(minimax(depth+1,nodeIndex*2,True,scores,height),
                   minimax(depth+1,nodeIndex*2 + 1,True,scores,height))
#main program
scores=list(map(int,input("Enter the 8 of leaf nodes values: ").split()))
height=3
result=minimax(0,0,True,scores,height)
print("The optimal value is:", result)