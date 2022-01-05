#Split_string_method
import random
names_string = input("Кто участвует в рулетке? ")
names = names_string.split(", ")

num_items = len(names)

random_choice = random.randint(0, num_items - 1)
print(names[random_choice], "бам! убит")

