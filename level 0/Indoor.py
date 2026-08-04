    # enter text and save in vari
def main():
    Original_Text: str = input("Hi Harvard , whats up? ").strip()
    print("this is new text : ", change_text(Original_Text))

    # make Lowercase letter
def change_text(text: str):
    return text.lower()

main()