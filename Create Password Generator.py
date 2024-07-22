#!/usr/bin/env python
# coding: utf-8

# In[1]:


# PAssword Generator

import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_characters

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Add random characters to the password
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the list to ensure randomness
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

# Prompt user for input
def password_generator():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 4:
            print("Password length should be at least 4 characters.")
        else:
            password = generate_password(length)
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Run the password generator
password_generator()

