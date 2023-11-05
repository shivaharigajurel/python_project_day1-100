from art import logo
alphabet = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for char in start_text:
        if char in alphabet:

            position = alphabet.index(char)
            if cipher_direction == "encode":
                position = position+shift_amount
            elif cipher_direction == "decode":
                position = position - shift_amount
            else:
                print("Enter a valid text")
            end_text += alphabet[position]
        else:
            end_text+=char
    print(f"The {cipher_direction}d text is {end_text}")


print(logo)
should_continue = True
while should_continue:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%25

    caesar(start_text=text, shift_amount=shift, cipher_direction= direction)
    result = input('Type "Yes" if you want to go again. otherwise type "no"')
    if result == "no":
        should_continue = False
        print("Goodbye")


