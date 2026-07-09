class Solution:
    # Function to print the pattern
    def pattern(self, N):
        # Outer loop to print the rows
        for i in range(N):
            # Inner loop to print the columns for the rows
            counter = 0
            for j in range(N-i):
                # Print the stars
                counter += 1
                print(counter, end ="")
            # After printing stars for each row move to next line
            print()

sol = Solution()
N = 5
sol.pattern(N) 