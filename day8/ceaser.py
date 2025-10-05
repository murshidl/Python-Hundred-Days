# def calculate_love_score(name1="murshid ahsan ali", name2="misbah zohar"):
#     combined_name = (name1 + name2).lower()
    
#     true_count = sum(combined_name.count(char) for char in "true")
#     love_count = sum(combined_name.count(char) for char in "love")
    
#     love_score = int(str(true_count) + str(love_count))
    
#     print(love_score)
# calculate_love_score()

from art import tprint

tprint("Caesar")  # You can write any banner text here

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type encode to encrypt the text or decode to decrypt the text:\n").lower()
text = input("Enter your message:\n").lower()
shift = int(input("Enter the shift value:\n"))

def ceaser(original_text, shift_value, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_value *= -1
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_value
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    print(f"Here is your {encode_or_decode}d message: {output_text}")

ceaser(original_text=text, shift_value=shift, encode_or_decode=direction)
