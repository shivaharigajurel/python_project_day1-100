target = int(input())

even_sum = 0
for number in range(2, target+1, 2):
    even_sum += number
print(even_sum)


alternative_sum = 0
for number in range(1, target+1):
    if number%2==0:
        alternative_sum += number
print(alternative_sum)