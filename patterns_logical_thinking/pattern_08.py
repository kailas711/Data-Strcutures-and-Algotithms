class Solution:
    # Function to print the pattern.
    def pattern(self, N):
        # Outer loop to print the row.
        for i in range(N):
            #Inner loop to print the columns.
            for j in range(i):
                print("-", end="") # Print the space.
            # After printing stars for each row move to next line.
            for k in range(2*N-2*i+1):
                print("*", end="")
            for j in range(i):
                print("-", end="") # Print the space.
            print()

sol = Solution()
N = 5
sol.pattern(N)