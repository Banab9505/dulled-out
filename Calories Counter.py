# Burger Choices

Cheeseburger = 461
Fish_Burger = 431
Veggie_Burger = 420
No_burger = 0

burgers = [Cheeseburger,
           Fish_Burger,
           Veggie_Burger,
           No_burger]

# Drink Choices

Soft_Drink = 130
Orange_Juice = 160
Milk = 118
No_drink = 0

drinks = [Soft_Drink,
          Orange_Juice,
          Milk,
          No_drink]

# Side Choices

Fries = 100
Baked_Potato = 57
Chef_Salad = 70
No_side = 0

sides = [Fries,
         Baked_Potato,
         Chef_Salad,
         No_side]

# Dessert Choices


Apple_Pie = 167
Sundae = 266
Fruit_Cup = 75
No_dessert = 0

# Calculate

def calculate():

    Calories = 0
    Order = []

    burger_choice = input("Welcome to Chip's Fast  Food Emporium\nPlease enter burger choice: ")
    str(burger_choice)

    if burger_choice == 1:
        Order.append("Cheeseburger")
        return Cheeseburger + Calories
    elif burger_choice == 2:
        Order.append("Fish Burger")
        return Fish_Burger + Calories
    elif burger_choice == 3:
        Order.append("Veggie Burger")
        return Veggie_Burger + Calories
    elif burger_choice == 4:
        return No_burger + Calories
    else:
        print("Sorry, the option is invalid. Please slect a number from 1 to 4")


    side_choice = input("Please enter side choice:  ")
    str(side_choice)

    if side_choice == "1":
        Order.append("Fries")
        return Fries + Calories
    elif side_choice == 2:
        Order.append("Baked Potato")
        return Baked_Potato + Calories
    elif side_choice == 3:
        Order.append("Chef Salad")
        return Chef_Salad + Calories
    elif side_choice == 4:
        return Chef_Salad + Calories
    else:
        print("Sorry, the option is invalid. Please slect a number from 1 to 4")


    drink_choice = input("Please enter the drink choice: ")
    int(drink_choice)

    if drink_choice == "1":
        Order.append("Soft Drink")
        return Soft_Drink + Calories
    elif drink_choice == 2:
        Order.append("Orange Juice")
        return Orange_Juice + Calories
    elif drink_choice == 3:
        Order.append("Milk")
        return Milk + Calories
    elif drink_choice == 4:
        return No_drink + Calories
    else:
        print("Sorry, the option is invalid. Please slect a number from 1 to 4")


    dessert_choice = input("Please enter the desset choice: ")
    str(dessert_choice)

    if dessert_choice == "1":
        return Apple_Pie + Calories
    elif dessert_choice == 2:
        Order.append("Sundae")
        return Sundae + Calories
    elif dessert_choice == 3:
        Order.append("Fruit Cup")
        return Fruit_Cup + Calories
    elif dessert_choice == 4:
        return No_dessert + Calories
    else:
        print("Sorry, the option is invalid. Please select a number from 1 to 4")



    print("Total calories are: ", Calories)




calculate()
