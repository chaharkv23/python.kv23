from functools import reduce

nums = [12,23,34,45,56,67,78,89,90]

evens = list(filter(lambda n:n%2==0,nums))
print(evens)
doubles = list(map(lambda n : n*2,evens))
print(doubles)
sum = reduce(lambda a,b: a+b,doubles)
print(sum)