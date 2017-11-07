# Manipulating DataFrames with pandas on Data Camp

#######################################

# Part 1: Extracting and transforming DataFrames

#######################################

## Positional and labeled indexing

# Assign the row position of election.loc['Bedford']: x
x = 4

# Assign the column position of election['winner']: y
y = 4

# Print the boolean equivalence
print(election.iloc[x, y] == election.loc['Bedford', 'winner'])

## Indexing and column rearrangement
