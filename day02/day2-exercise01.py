
#List Declaration
numbers = [134, 235, 323, 4444, 125]

#Dictionary Declaration

results = {
    "Even": [],
    "Odd": []
}

for n in numbers:
    if n % 2 == 0:
        results["Even"].append(n)
    else:
        results["Odd"].append(n)

#Display the results

print("Even numbers:", results["Even"])
print("Odd numbers:", results["Odd"])