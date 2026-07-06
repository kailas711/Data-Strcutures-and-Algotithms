class Solution:
    # Function to print the pattern 
    def pattern(self, N):
        # Outer loop to handle rows
        for i in range(N):
            # Inner loop to handle columns for each row
            for j in range(N-i):
                # Print the star
                print("*", end="")
            # After printing stars for each row move to next line
            print()

sol = Solution()
N = 5
sol.pattern(N)