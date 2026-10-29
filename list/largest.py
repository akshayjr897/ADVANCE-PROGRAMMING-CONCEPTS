def largest(a):
    big = a[0]
    for x in a:
        if x > big:
            big = x
    return big

a = list(map(int, input("Enter numbers: ").split()))
print("Largest:", largest(a))