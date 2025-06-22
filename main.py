
morse_code_dictionary = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",

    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",

    ".": ".-.-.-",",": "--..--","?": "..--..","'": ".----.",
    "!": "-.-.--","/": "-..-.","(": "-.--.-","&": ".-...",
    ":": "---...",";": "-.-.-.","=": "-...-","+": ".-.-.",
    "-": "-....-","_": "..--.-","\"": ".-..-.","$": "...-..-",
    "@": ".--.-."
}

user_input =(input("enter the text or morse-code to be translated").upper())

if user_input.startswith(".") or user_input.startswith("-"):
    words = user_input.strip().split(" ")
    response = []
    for word in words:
        if word == "/":
            response.append(" ")
        else:
            for key, value in morse_code_dictionary.items():
                if value == word:
                    response.append(key)
                    break
    print("".join(response))

else:
    words = list(user_input.strip().strip("/"))
    response = []
    for word in words:
        if word == " ":
            response.append("/")
        else:
            response.append(morse_code_dictionary[word])
    print(" ".join(response))


