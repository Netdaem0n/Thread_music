a = dict()
iii = 0

while True:
    if iii == 3:
        break
    key_1: str = input()
    key_data: str = input()
    a[key_1] = key_data
    iii += 1

print(a)