import random

names = input("Enter your names:")
split_names = names.split(', ')
people = len(split_names)
random_person = random.randint(0, people - 1)
person_to_pay = random.choice(split_names)
#person_to_pay = split_names[random_person]
print(f"{person_to_pay} is going to pay the bill")