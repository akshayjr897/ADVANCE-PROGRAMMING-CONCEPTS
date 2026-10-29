def average(a):
    return sum(a) / len(a)

a = list(map(int, input("Enter numbers: ").split()))
print("Average:", average(a))