# Name: Huy Anh Nguyen
# Class: CSCE 3550.001
# Date: 10/27/2021
# Project 2: Simplified AES system
# Description: Implementation of a simplified version of AES encryption system. 

import re

# Read in input file.
def read_data(file_name):
	
	file = open(file_name, "r")
	content = file.read()
	file.close()
	# Convert list to int
	return content

# Write to an output file.
def write_data(content, file_name):

	file = open(file_name, "a")
	for element in content:
		file.write(element)
	file.close()

# Proprocessing function.
def pre_processing(content):
	result = re.sub(r'[^\w\s]', '', content)
	result = re.sub(r'\s+', '', result)
	return result

# Generate a key for Vigenère Cipher.
def generate_key(content, key):
    processed_key = []
    key_length = len(key)
    content_length=len(content)
    key_index = 0

    for i in range(0, content_length):
    	processed_key.append(key[key_index])
    	key_index += 1
    	if key_index > key_length - 1:
    		key_index = 0
    return "".join(processed_key)


# Substitution using Vigenère Cipher.
def substitution(content, key):
    cipher_text = []
    for i in range(len(content)):
        x = (ord(content[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))

# Padding function.
def padding(content):
	if (content != None) and len(content):
		reminder = len(content) % 16
		pads = 16 - reminder
		for i in range(len(content) + pads):
			if i >= len(content):
				content += "A"
	return content

# Function to print the padded string to the screen,
# and write it to the output file.
def print_padded(content, file_name):
	file = open(file_name, "a")
	file.write("\n\nPadding:\n")
	for i in range(len(content)):
		if i < len(content):
			print(content[i] + "", end='')
			file.write(content[i] + "")
		if (i+1) % 4 == 0:
			print("")
			file.write("" + "\n")
		if (i+1) % 16 == 0:
			print("\n", end='')
			file.write("\n")


# Driver code
def driver_code():
	# variables to save user's inputs
	input_filename = input("Enter the name of the input plaintext file: ")
	key_filename = input("Enter the name of the input key file: ")
	output_filename = input("Enter the name of the output ciphertext file: ")

	input_content = read_data(input_filename) # save input's content
	key_content = read_data(key_filename) # save key's content

	# Part a - Preprocessing
	processed_content = pre_processing(input_content) # save input after processing
	print(f'Preprocessing:\n{processed_content}') # Print to the screen

	result = "Preprocessing:\n" + processed_content # temporary variable to save the result
	write_data(result, output_filename) # save to output file

	# Part b - Substitution
	vigen_key = generate_key(processed_content, key_content)
	subs_content = substitution(processed_content, vigen_key)
	print(f'\nSubstitution:\n{subs_content}') # Print to the screen

	result = "\n\nSubstitution:\n" + subs_content # temporary variable to save the result
	write_data(result, output_filename) # save to output file
	print(type(subs_content))

	# Part c - Padding
	padded_content = padding(subs_content)
	print(f'\nPadding:')
	print_padded(padded_content, output_filename) # Print to the screen & save to file


# Main
if __name__ == '__main__':
	driver_code()

