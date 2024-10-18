PI = 3.14159265
PEOPLE_PER_LARGE = 7
PEOPLE_PER_MEDIUM = 3
PEOPLE_PER_SMALL = 1
DIAMETER_LARGE = 20
DIAMETER_MEDIUM = 16
DIAMETER_SMALL = 12
COST_LARGE = 14.68
COST_MEDIUM = 11.48
COST_SMALL = 7.28


def people():
    num_people = int(input("Please enter how many guests to order for:"))
    large, med, small = 0, 0, 0
    large = num_people // PEOPLE_PER_LARGE
    r = num_people % PEOPLE_PER_LARGE
    if r != 0:
        med = r // PEOPLE_PER_MEDIUM
        r2 = r % PEOPLE_PER_MEDIUM
        if r2 != 0:
            small = r2 // PEOPLE_PER_SMALL
            if r % PEOPLE_PER_SMALL != 0:
                small += 1
    print(f"{large} large pizzas, {med} medium pizzas, and {small} small pizzas will be needed.\n")
    return num_people, large, med, small


def area(num_people, large, med, small):
    total_area = large * PI * ((DIAMETER_LARGE / 2) ** 2) + med * PI * ((DIAMETER_MEDIUM / 2) ** 2) + small * PI * (
                (DIAMETER_SMALL / 2) ** 2)
    area_per_person = total_area / num_people
    print(f"A total of {total_area:.2f} square inches of pizza will be ordered ({area_per_person:.2f} per guest).")


def cost(large, med, small):
    tip = int(input("Please enter the tip as a percentage (i.e. 10 means 10%):"))
    cost_before_tip = large*COST_LARGE + med*COST_MEDIUM + small*COST_SMALL
    total_cost = cost_before_tip*(tip*.01+1)
    print(f"The total cost of the event will be: ${total_cost:.2f}.\n")


def main():
    num_people, large, med, small = people()
    area(num_people, large, med, small)
    cost(large, med, small)


if __name__ == "__main__":
    """The program will calculate the number of large, medium, 
    and small pizzas needed. Based on those numbers, it will 
    then calculate the total price (including tip), and just 
    for fun, the total number of square inches of pizza ordered 
    and average square inches per person."""
    main()  # format numbers like this: {your_variable_name:.2f}
