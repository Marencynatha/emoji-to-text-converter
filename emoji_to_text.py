import emoji

def emoji_to_text(input_text):
    """
    Convert emojis in the input text to their text equivalents.
    
    Args:
        input_text (str): The input string containing emojis.
        
    Returns:
        str: The text with emojis replaced by their descriptions.
    """
    return emoji.demojize(input_text)

def main():
    print("Welcome to the Emoji to Text Converter!")
    print("Type your text containing emojis below:")
    input_text = input("> ")
    converted_text = emoji_to_text(input_text)
    print("\nConverted Text:")
    print(converted_text)

if __name__ == "__main__":
    main()
