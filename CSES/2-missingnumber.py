n = int(input())
list_of_nums = [int(i) for i in input().split()]
real_list = [int(i) for i in range(1,n+1)]
print(sum(real_list)-sum(list_of_sums))

#Quite happy with this more elegant solution - the initial brute force one that I tried to implement got a TLE because i tried to go through every single element and compare it 
