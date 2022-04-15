def num_translate():
    while True:
        try:
            client_translate = input("Введите число от 0 - 10 на английском: ")
            num_translate = {
                "zero" : "ноль",
                "one" : "один",
                "two" : "два",
                "three" : "три",
                "four" : "четыре",
                "five" : "пять",
                "six" : "шесть",
                "seven" : "семь",
                "eight" : "восемь",
                "nine" : "девять",
                "ten" : "десять",
            }

            for key, valye in num_translate.items():
                if client_translate == key:
                    print(valye)
            if client_translate not in num_translate:
                print("None")
                
                
        except ValueError:
            print("Error 404")
                
if __name__ == "__main__":
    num_translate()