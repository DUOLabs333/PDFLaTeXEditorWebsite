initial = int(input())

years = 0
while initial <= 700000:
    initial = (initial * 1.071)
    years += 1
print(years)
