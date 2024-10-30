# Logan Hays
# UWYO COSC 1010
# Submission Date: 10/29/2024
# HW 02
# Lab Section: 13
# Sources, people worked with, help given to: 
# your
# comments
# here

morse_code = {
    "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".", 
    "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-", 
    "J": ".---", "W": ".--", "K": "-.-", "X": "-..-", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
}

letters = input("What word would you like in morse code: ")

def input_to_morse(letters):
  morse_word = ''
  for letter in letters.upper():
      if letter in morse_code:
          morse_word += morse_code[letter] + ' '
      else:
          morse_word += ' '
  return morse_word

print(input_to_morse(letters))