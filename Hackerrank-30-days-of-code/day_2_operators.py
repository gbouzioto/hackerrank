
# Complete the solve function below.


def solve(_meal_cost, _tip_percent, _tax_percent):
    tip = _meal_cost * tip_percent / 100
    tax = _meal_cost * tax_percent / 100
    total_meal_cost = round(_meal_cost + tip + tax)
    return total_meal_cost


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    cost = solve(meal_cost, tip_percent, tax_percent)
    print("The total meal cost is {} dollars.".format(cost))
