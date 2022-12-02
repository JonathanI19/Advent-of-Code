#!/usr/bin/env python3

def main():
    with open("input.txt", 'r') as input:
        lines = input.read()
    
    elves = lines.split("\n\n")
    calories = []

    for elf in elves:
        total = []
        bag = elf.split("\n")
        for food in bag:
            
            # If statement handles a minor bug
            if food != "":
                total.append(int(food))
                
        calories.append(sum(total))
    
    calories.sort(reverse=True)
    print(sum(calories[:3]))
  
    
    
if __name__ == "__main__":
    m = main()