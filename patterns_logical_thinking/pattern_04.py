class solution:
    # Function to print the pattern of stars
    def pattern(self, N):
        # Outer Loop to handle rows
        for i in range(N):
            # Inner loop to handle columns for each rows
            for j in range(i+1):
                # Print the star
                print(i+1, end="")
            # After printing stars in each row move to next line
            print()

# Driver code
sol = solution()
N = 5
sol.pattern(N) 