"""
graph paper.py

Makes a graph chart based on your input.

"""

import sys

rowNum = "How many rows? "
columnNum = "How many columns? "
rowSpace = "How many spaces within each row? "
colSpace = "How many spaces within each column? "


print("Hello, let's build a graph.")
print()

# Get inputs from user and entry checker
def getInt(graph):
    assert isinstance(graph, str)

    while True:
        try:
            gr = input(graph)
        except EOFError:
            sys.exit(1)
        except KeyboardInterrupt:
            sys.exit(1)

        try:
            rowNum = int(gr)
            columnNum = int(gr)
            rowSpace = int(gr)
            colSpace = int(gr)
            
        except ValueError:
            print()
            print(f"Sorry, please enter a whole number.")
            continue #go back to while

        return rowNum or columnNum or rowSpace or colSpace

row = getInt(f"{rowNum}")
column = getInt(f"{columnNum}")
rowSpace = getInt(f"{rowSpace}")
colSpace = getInt(f"{colSpace}")

## Code for graph printing ##       

colsp= colSpace * "-"
colem= colSpace * " "

for outer in range(row):
    print(f"+{colsp}" * column + "+")

    for inner in range(rowSpace):
        print(f"|{colem}" * column + "|")
    
print(f"+{colsp}" * column + "+")


sys.exit(0)
