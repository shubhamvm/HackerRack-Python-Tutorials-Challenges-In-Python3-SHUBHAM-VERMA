a = input("Enter String: ")
b = input("Enter SubString: ")
count = 0
for i in range(len(a)):
    if a[i:].startswith(b):
        count += 1
print (count)
