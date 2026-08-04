#Build a function to make emoji character
def convert(text_emoji: str):
    text_emoji = text_emoji.replace(":)","🙂")
    text_emoji = text_emoji.replace(":(","🙁")
    return text_emoji

    #Enter a text emoji
def main():
    original_text: str = input("Enter a text and emoji: ").strip()
    print("this is new  version text :", convert(original_text))


main()
