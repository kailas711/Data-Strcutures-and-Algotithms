class Solution:
    # function to print the pattern.
    def pattern(self, N):
        # outer loop to print the row.
        # first triangle
        for i in range(N):
            # inner loops to print the columns.
            # print the number
            val = 1 if i % 2 != 0 else 0
            for j in range(i):
                # for odd rows start with 1 else 0
                print(val, end="")
                # toggle between 1 and 0
                val = 1 - val
            print()

sol = Solution()
N = 5
sol.pattern(N)
