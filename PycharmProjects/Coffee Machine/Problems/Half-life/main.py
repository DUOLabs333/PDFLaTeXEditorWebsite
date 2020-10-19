initial = int(input())
final = int(input())
half_lives = 0

while initial >= final:
    initial = initial // 2
    half_lives += 1

print(half_lives * 12)
