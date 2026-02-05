num = [1, 2, 3, 4, 5, 4, 3, 2, 1]
t = 7

for i, value in enumerate(num):
    if value == t:
        print("Element found at index:", i)
        break
else:
    print("Element not found in the list", -1)
