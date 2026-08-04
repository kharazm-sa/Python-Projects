# Customer's final price
def dollars_to_float(d: str):
    d = float(d.replace('$', ''))
    return d

    # Tip calculation
def percent_to_float(p: str):
    p = float(p.replace('%', ''))
    p = float(p / 100)
    return p

    # Calculator for calculating tips
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


main()
