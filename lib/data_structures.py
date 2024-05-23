spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        names.append(food["name"])
    return names

def get_spiciest_foods(spicy_foods):
    spiciest = []
    for food in spicy_foods:
      if food["heat_level"] > 5:
        spiciest.append(food["name"])
    return spiciest

def print_spicy_foods(spicy_foods):
  for food in spicy_foods:
    num_peppers = int(food["heat_level"] / 3)  
    pepper_string = "" * num_peppers  
    print(f"{food['name']} ({food['cuisine']}) | Heat Level: {pepper_string}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    cuisine_food_dict = {food["cuisine"]: food.copy() for food in spicy_foods}
    return cuisine_food_dict

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
    num_peppers = int(food["heat_level"] / 3)  
    pepper_string = "" * num_peppers
            if  num_peppers > 5 : 
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {pepper_string}")

def get_average_heat_level(spicy_foods):
    new_list = []
    for food in spicy_foods:
      heat_average = int(food["heat_level"])
      new_list.append(heat_average)
    return sum(new_list) / len(new_list) 

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
