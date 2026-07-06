# Implementing simple recusion using loops
prev2 = 0
prev1 = 1

for i in range(10):
    nextNum = prev2+prev1
    # print(nextNum)
    prev2 = prev1
    prev1 = nextNum

count = 0
# Recursion 
def fibonacci(prev1, prev2):
    global count
    if count <= 4:
        nextNum = prev1 + prev2
        print(nextNum)
        prev2 = prev1
        prev1 = nextNum
        count += 1
        fibonacci(prev1, prev2)
    else:
        return 

fibonacci(1,0)
