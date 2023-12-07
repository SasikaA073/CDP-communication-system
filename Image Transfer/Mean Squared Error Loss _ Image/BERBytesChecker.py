import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name="BytesBERChecker",
            in_sig=[np.uint8, np.uint8],  # Two input byte streams
            out_sig=[np.float32]          # Output signature indicating a float value
        )

        self.ber = 0.0  # Initialize BER

    def work(self, input_items, output_items):
        # Convert bytes to binary strings
        binary_text1 = ''.join(format(byte, '08b') for byte in input_items[0])
        binary_text2 = ''.join(format(byte, '08b') for byte in input_items[1])

        # Ensure both input streams have the same length
        if len(binary_text1) != len(binary_text2):
            # Pad the smaller file with zeros to match the length of the larger file
            max_length = max(len(binary_text1), len(binary_text2))
            binary_text1 = binary_text1.ljust(max_length, '0')
            binary_text2 = binary_text2.ljust(max_length, '0')

        # Calculate BER as the bit mismatch ratio
        mismatch_count = sum(c1 != c2 for c1, c2 in zip(binary_text1, binary_text2))
        total_bits = len(binary_text1)
        self.ber = mismatch_count / total_bits

        # Return BER as output
        output_items[0][:] = np.array([self.ber], dtype=np.float32)
        return len(output_items[0])
