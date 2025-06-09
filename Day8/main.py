import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shifted_amount, cipher_direction):
    plain_text = ""
    if cipher_direction == "decode":
        shifted_amount *= -1
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shifted_amount
            shifted_position %= len(alphabet)
            plain_text += alphabet[shifted_position]
        else:
            plain_text += letter
    print(f"The {cipher_direction}d text is {plain_text}")
    
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    if direction not in ["encode", "decode"]:
        print("Invalid direction. Please enter 'encode' or 'decode'.")
        continue
    text = input("type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(original_text=text, shifted_amount=shift, cipher_direction=direction)
    
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no': \n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")
