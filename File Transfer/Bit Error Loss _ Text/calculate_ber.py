import argparse

def calculate_bit_error_rate(input_text1, input_text2):
    # Convert text to binary strings
    binary_text1 = ''.join(format(ord(char), '08b') for char in input_text1)
    binary_text2 = ''.join(format(ord(char), '08b') for char in input_text2)

    # Ensure both input streams have the same length
    if len(binary_text1) != len(binary_text2):
        # Pad the smaller text with zeros to match the length of the larger text
        max_length = max(len(binary_text1), len(binary_text2))
        binary_text1 = binary_text1.ljust(max_length, '0')
        binary_text2 = binary_text2.ljust(max_length, '0')

    # Calculate BER as the bit mismatch ratio
    mismatch_count = sum(c1 != c2 for c1, c2 in zip(binary_text1, binary_text2))
    total_bits = len(binary_text1)
    ber = mismatch_count / total_bits
    return ber

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate Bit Error Rate (BER) between two text files.')

    parser.add_argument('input_file_path1', type=str, nargs='?', default='input.txt', help='Path to the first input text file')
    parser.add_argument('input_file_path2', type=str, nargs='?', default='output.txt', help='Path to the second input text file')

    args = parser.parse_args()

    # Read text from input files
    with open(args.input_file_path1, 'r') as file1, open(args.input_file_path2, 'r') as file2:
        text1 = file1.read()
        text2 = file2.read()

    bit_error_rate = calculate_bit_error_rate(text1, text2)
    print(f"Bit Error Rate (BER): {bit_error_rate}")
