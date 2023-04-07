import requests

# Open two files for writing only
file1 = open("high_sugar.txt", "w")
file2 = open("low_sugar.txt", "w")

# Send API request to retrieve all fruits and their sugar content
response = requests.get("https://fruityvice.com/api/fruit/all")
fruits = response.json()

# Iterate through all fruits and write their names to the appropriate file based on sugar content
for fruit in fruits:
    if fruit['nutritions']['sugar'] > 7:
        file1.write(fruit['name'] + "\n")
    else:
        file2.write(fruit['name'] + "\n")

# Close the files
file1.close()
file2.close()

# Open the high sugar file and print its contents
with open("high_sugar.txt", "r") as file:
    high_sugar_fruits = file.readlines()
    print("High sugar fruits:")
    for fruit in high_sugar_fruits:
        print(fruit.strip())

