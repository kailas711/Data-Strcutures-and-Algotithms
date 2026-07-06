class solution:
    # Function to print the pattern of stars
    def solution(self, N):
        # Outer Loop to handle rows
        for i in range(N):
            # Inner loop to handle columns for each rows
            counter = 0
            for j in range(i+1):
                # Print the star
                counter +=1
                print(counter, end="")
            # After printing stars in each row move to next line
            print()

# Driver code
sol = solution()
N = 5
sol.solution(N) 