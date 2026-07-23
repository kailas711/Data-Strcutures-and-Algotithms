class Solution:
    # function to print the pattern.
    def pattern(self, N):
        # outer loop to print the row.
        # first triangle
        for i in range(N):
            # inner loops to print the columns.
            # print space first
            for k in range(N-i):
                print(" ", end="")
            # print the stars
            for j in range(2*i-1):
                print("*", end="") 
           # print space later
            for k in range(N-i):
                print(" ", end="")
            # move to next line after printing stars for rows 
            print()
        
        # second triangle
        for i in range(N):
            # inner loops to print the columns.
            # print space first
            for k in range(i):
                print(" ", end="")
            # print the stars
            for j in range(2*N-2*i-1):
                print("*", end="") 
           # print space later
            for k in range(i):
                print(" ", end="")
            # move to next line after printing stars for rows 
            print()

sol = Solution()
N = 5
sol.pattern(N)
