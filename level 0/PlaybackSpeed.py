    # enter text and save in vari
def main():
    Original_Text: str = input("Hi dare, Enter your text? ").strip()
    print("this is new text :", change_text(Original_Text))

    # make dotted space in my line text
def change_text(text: str):
    return text.replace(" " , "...")

main()