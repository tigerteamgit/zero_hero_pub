print("hello world")

def add(x,y):
    return x + y

print(add(2,2))


def my_worker(fruit):
    statement = f"My favorite meal is chicken and {fruit}"
    meals = {"dinner":statement}
    return meals

meal = my_worker("Apples")

def human(food):
    consume = food["dinner"]
    return consume

my_meal = human(meal)