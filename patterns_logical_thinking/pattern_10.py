class Solution:
    # function to print the pattern.
    def pattern(self, N):
        # outer loop to print the row.
        # first triangle
        for i in range(N):
            # inner loops to print the columns.
            # print the stars
            for j in range(i):
                print("*", end="") 
           # print space later
            for k in range(N-i):
                print(" ", end="")
            # move to next line after printing stars for rows 
            print()
        
        # second triangle
        for i in range(N):
            # inner loops to print the columns.
            # print the stars
            for j in range(N-i-1):
                print("*", end="") 
           # print space later
            for k in range(i):
                print(" ", end="")
            # move to next line after printing stars for rows 
            print()

sol = Solution()
N = 5
sol.pattern(N)
