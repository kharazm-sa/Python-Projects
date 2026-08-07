def main():
    Welcome = input("hello, welcome to out bank ! what can i help you ? ").strip().lower()

    if Welcome.startswith("hello"):
        print("0$")
    elif Welcome.startswith("h"):
        print("20$")
    else:
        print("100$")

main()