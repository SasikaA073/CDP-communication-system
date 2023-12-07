import numpy as np
from gnuradio import gr


class enc_blk(gr.sync_block):

    def __init__(self, key=1.0):   
        gr.sync_block.__init__(
            self,
            name='Encryptor',
            in_sig=[np.ubyte],
            out_sig=[np.ubyte]
        )
        
        self.key = key

    def work(self, input_items, output_items):
    
        def encrypt_cesar(arr, shift):                
            encrypted = []
            
            for num in arr:
            # Shift the number by the given amount
                num = num + shift
        
                # If the number is greater than 255, wrap it around to the start
                if num > 255:
                    num = num - 256
        
                # Append the encrypted number to the list
                encrypted.append(num)
    
            return encrypted
        
        enc_arr = encrypt_cesar(input_items[0] , self.key)
        output_items[0][:] = enc_arr
        
        return len(output_items[0])
