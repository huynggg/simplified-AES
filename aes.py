# Name: Huy Anh Nguyen
# Class: CSCE 3550.001
# Date: 10/27/2021
# Project 2: Simplified AES system
# Description: Implementation of a simplified version of AES encryption system. 

import re

# ------------------------- # 
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

# Function to convert string to matrix of 4x4
def string_to_matrix(content):
	matrix = []
	temp = []
	for i in range(0, len(content)):
		k = i + 1
		temp.append(content[i])
		if k % 4 == 0:
			matrix.append(temp)
			temp = []
	return matrix

# Function to shift element(s) by row position
def shift_by_position(content, position):
	temp = [0,0,0,0]
	if (position == 0):
		temp[0] = content[0]
		temp[1] = content[1]
		temp[2] = content[2]
		temp[3] = content[3]
	if (position == 1):
		temp[0] = content[1]
		temp[1] = content[2]
		temp[2] = content[3]
		temp[3] = content[0]
	if (position == 2):
		temp[0] = content[2]
		temp[1] = content[3]
		temp[2] = content[0]
		temp[3] = content[1]
	if (position == 3):
		temp[0] = content[3]
		temp[1] = content[0]
		temp[2] = content[1]
		temp[3] = content[2]
	return temp

# Function to shift the matrix
def shifting(content):
	position = 0
	temp = []
	for i in range(len(content)):
		if position > 3:
			position = 0
		temp.append(shift_by_position(content[i],position))
		position += 1
	return temp

# Function to print shifted content/matrix
def print_shifted(content, file_name):
	file = open(file_name, "a")
	file.write("Shifting:")
	for i in range(len(content)):
		if i % 4 == 0:
			print("\n", end='')
			file.write("\n")
		for j in range(4):
			print(content[i][j], end='')
			file.write(content[i][j] + "")
		print("\n",end='')
		file.write("\n")

# Function to convert a single character to binary, 
# also check for Parity Bit condition
def string_to_binary(content):
	temp = format(ord(content), '08b')
	counter = 0
	result = []
	result[:0] = temp
	for i in result:
		if i == "1":
			counter+=1
	if counter % 2 != 0:
		result[0] = "1"
	result = ''.join(map(str,result))
	return result

# Function to convert a string of binary 
# to its hexadecimal value
def binary_to_hexa(content):
	# convert binary to int
    num = int(content, 2)
    # convert int to hexadecimal
    hex_num = format(num, 'x')
    return(hex_num)

# Parity Bit function
def parity_bit(content):
	for i in range(len(content)):
		for j in range(4):
			content[i][j] = binary_to_hexa(string_to_binary(content[i][j]))
	return content

# Function to print/write parity bit matrix
def print_parity_bit(content, file_name):
	file = open(file_name, "a")
	file.write("\nParity Bit:\n")
	for i in range(len(content)):
		for j in range(4):
			print(content[i][j] + " ", end='')
			file.write(content[i][j] + " ")
		print("\n",end='')
		file.write("\n")

# --------------------------- #
# Driver code
def driver_code():
	# variables to save user's inputs
	input_filename = input("Enter the name of the input plaintext file: ")
	key_filename = input("Enter the name of the input key file: ")
	output_filename = input("Enter the name of the output ciphertext file: ")

	# variables to save inputs
	input_content = read_data(input_filename)
	key_content = read_data(key_filename)

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


	# Part c - Padding
	padded_content = padding(subs_content)
	print(f'\nPadding:')
	print_padded(padded_content, output_filename) # Print to the screen & save to file
	
	# Part d - Shifting 
	padded_content = string_to_matrix(padded_content) # Convert string to a matrix
	shifted_content = shifting(padded_content)
	print(f'Shifting:', end='')
	print_shifted(shifted_content, output_filename) # Print to the screen & save to file
	
	# Part e - Parity Bit
	parity_bit_content = parity_bit(shifted_content)
	print(f'\nParity Bit:')
	print_parity_bit(parity_bit_content,output_filename)

		


# Main
if __name__ == '__main__':
	driver_code()

