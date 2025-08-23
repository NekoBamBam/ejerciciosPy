#Dada la lista nums = [1,2,3,4,5,6], cuenta cuántos números pares hay.

nums = [1,2,3,4,5,6]
pares = sum(1 for n in nums if n % 2 == 0)
print(pares)