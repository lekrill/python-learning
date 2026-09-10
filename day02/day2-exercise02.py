
#List Declaration
fruits = ["apple", "banana", "cherry", "date", "elderberry", "apple", "apple","cherry" ]

#Dictionary Declaration
fruit_count = {}

# Count the occurrences of each fruit
for x in fruits:
    if x in fruit_count:
        fruit_count[x] += 1
    else:
        fruit_count[x] = 1

# Display the results
for x, count in fruit_count.items():
    print(f"{x}: {count}")