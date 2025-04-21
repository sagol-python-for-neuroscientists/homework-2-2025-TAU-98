MORSE_CODE = {
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',

    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',

    '.': '.-.-.-', ',': '--..--', ':': '---...',
    "'": '.----.', '-': '-....-'
}


def english_to_morse(input_file="lorem.txt", output_file="lorem_morse.txt"):
    with open(input_file, "r") as f:
        text = f.read()

    text = text.upper()
    words = text.split()
    print(f"Word count from lorem.txt: {len(words)}")

    morse_lines = []

    for word in words:
        morse_word = ''.join([MORSE_CODE.get(char, '') for char in word])
        morse_lines.append(morse_word)

    with open(output_file, "w") as f:
        f.writelines([line + "\n" for line in morse_lines])  

    print(f"Lines written to {output_file}: {len(morse_lines)}")


if __name__ == "__main__":
    english_to_morse()

    with open("lorem_morse.txt", "r") as f:
        data = f.read()
        print("Dashes (-):", data.count("-"))
        print("Dots (.):", data.count("."))
        print("Newlines (\\n):", data.count("\n"))  
if __name__ == '__main__':
    # Question 1
    english_to_morse()  # uses default input_file and output_file
    print("Question 1 solution: Morse code file created.")