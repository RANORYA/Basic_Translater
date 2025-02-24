def load_dictionary(file_path):
    dictionary = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            if ":" in line:
                key, value = line.split(":", 1)
                dictionary[key] = value

    except FileNotFoundError:
        print("Sözlük dosyası bulunamadı.")

    return dictionary


def main():
    dic_tr_en = load_dictionary("C:\\Users\\aposy\\Desktop\\Tarsus\\bionluk\\translate_database\\dic_en_tr.txt")  # Türkçe-İngilizce sözlük dosyası
    dic_tr_az = load_dictionary("C:\\Users\\aposy\\Desktop\\Tarsus\\bionluk\\translate_database\\dic_az_en.txt")  # Türkçe-Azerbaycanca sözlük dosyası

    while True:
        print("""
        1. Turkish to English Translation
        2. Turkish to Azerbaijani Translation
        3. Exit""")
        option = int(input("Select an option: "))

        if option == 1:
            text = input("Enter the Turkish text to translate: ")
            if len(text.split()) >= 10:
                translated_text = ""
                for word in text.split():
                    translated_word = dic_tr_en.get(word)
                    if translated_word:
                        translated_text += translated_word + " "
                    else:
                        translated_text += word + " "
                print(translated_text.strip())

            else:
                print("Please enter a minimum of 10 words")

        elif option == 2:
            text = input("Enter the Turkish text to translate: ")
            if len(text.split()) >= 10:
                translated_text = ""
                for word in text.split():
                    translated_word = dic_tr_az.get(word)
                    if translated_word:
                        translated_text += translated_word + " "
                    else:
                        translated_text += word + " "
                print(translated_text.strip())

            else:
                print("Please enter a minimum of 10 words")

        elif option == 3:
            print("Exiting")
            break

        else:
            print("Invalid option!")


if __name__ == '__main__':
    main()
