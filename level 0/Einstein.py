    #Constructing Einstein's formula for calculating
def Formula(num_mass: int):
    C=300000
    return int(num_mass*C*C)

    #Enter a Mass
def main():
    num = int(input("Enter a Mass: ").strip())
    print(f"Result =>, {Formula(num):,}")


main()
