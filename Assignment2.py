numbers = []
for x in range(2000, 3201):
    if x % 5 == 0:
        continue
    if x % 7 == 0:
       numbers.append(x)
print(numbers)