#1 - File not found handling

try:
    with open("unknown.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")

#2 - 
