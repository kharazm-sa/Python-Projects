    # enter a text and word review
def main():
    Text = str(input("how do you feel about life ? ")).strip().lower()
    if is_true(Text):
        print("Yes")
    else:
        print("No")

    # Checking a condition using a word passed by another function
def is_true(text):
    if text == "42" or text == "forty-two" or text == "forty two":
        return True
    else:
        return False

main()