class solution:
    # Function to print pattern of stars
    def pattern(self, N):
        # Outer Loop to handle rows
        for i in range(N):
            # Inner loop to handle columns for each row
            for j in range(i+1):
                # Print the star
                print("*", end="")
            # After printing stars in a row move to the next line
            print()

# Driver code
sol = solution()
N =5
sol.pattern(N) # Call the function to print the pattern