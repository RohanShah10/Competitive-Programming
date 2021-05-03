n = int(input())
while n!=1:
    print(f"{n} ", end="")
    if n%2 == 0:
        n = n//2
    else:
        n = (n*3)+1
    
print("1", end="")

#Key thing that I learnt here was how to print without going onto a new line immediately after
  
