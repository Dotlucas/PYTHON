from string import ascii_letters, digits, punctuation

for first_caracter in ascii_letters + digits + punctuation:
    for second_caracter in ascii_letters + digits + punctuation:
        for third_caracter in ascii_letters + digits + punctuation:
            for fourth_caracter in ascii_letters + digits + punctuation:
                print(first_caracter, second_caracter, third_caracter, fourth_caracter)