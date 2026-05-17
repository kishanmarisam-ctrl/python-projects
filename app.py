# strings #

x = 1
y = 2
print(x+y)
people_count = 10
people_name = "kishan"
print(len(people_name))
print(people_name[0])
print(people_name.upper())
print(people_name.lower())
print(people_name.title())
print(people_name.startswith("k"))
print(people_name.endswith("n"))
print(people_name.isalpha())
print(people_name.isalnum())
print(people_name.isdigit())
print(people_name.lstrip())
print(people_name.rstrip())
print(people_name.find("s"))
print(people_name.replace("k", "K"))

# numbers #

print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 // 5)
print(10 % 5)
print(10 ** 5)
print(bool(10 > 5))
print(bool(10 < 5))
print(bool(10 == 5))
print(bool(10 != 5))
print(bool(10 >= 5))
print(bool(10 <= 5))

# if , else , elif , and , or , not #

age = 17
if age >= 18:
    print("You are eligible to vote.")
elif age > 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

salary = True
credit_history = False
if salary and credit_history:
    print("You are eligible for a loan.")
elif salary or credit_history:
    print("You may be eligible for a loan.")
else:
    print("You are not eligible for a loan.")

tempature = 35
if not tempature > 30:
    print("The weather is not too hot.")
else:
    print("The weather is too hot.")


x = 12
if x in range(1, 11):
    print("x is between 1 and 10.")
else:
    print("x is not between 1 and 10.")

# while loop #

while x < 20:
    print(x)
    x += 1
