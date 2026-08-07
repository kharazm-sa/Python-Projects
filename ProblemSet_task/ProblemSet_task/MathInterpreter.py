def main():
    Process = input("Expression: ")
    x, y, z = Process.split(" ")

    if y == "+":
        result = int(x) + int(z)

    elif y == "-":
        result = int(x) - int(z)

    elif y == "*":
        result = int(x) * int(z)

    elif y == "/":
        if int(z) == 0:
            print("Invalid")
        else:
            result = int(x) / int(z)

    else:
        print("Invalid operator")
        return

    print(f"{result:.1f}")


main()