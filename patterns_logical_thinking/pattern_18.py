class Solution:
    # function to print the pattern.
    def pattern(self, N):
        # outer loop to print the row.
        # first triangle
        for i in range(N):
            # convert letter A to ASCII
            char = ord('E')
            # inner loops to print the columns.
            for j in range(i+1):
                # for odd rows start with 1 else 0
                print(chr(char), end="")
                # increment the ASCII by 1
                char = char-1
            print()

sol = Solution()
N = 5
sol.pattern(N)
