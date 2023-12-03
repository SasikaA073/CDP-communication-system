import numpy as np
from gnuradio import gr


class dec_blk(gr.sync_block):

    def __init__(self, key=1.0):   
        gr.sync_block.__init__(
            self,
            name='Decryptor',
            in_sig=[np.ubyte],
            out_sig=[np.ubyte]
        )
        
        self.key = key

    def work(self, input_items, output_items):
    
        def decrypt_cesar(arr, shift):                
            decrypted = []
            
            for num in arr:
                # Unshift the number by the given amount
                num = num - shift
        
                # If the number is less than 0, wrap it around to the end
                if num < 0:
                    num = num + 256
        
                # Append the decrypted number to the list
                decrypted.append(num)
    
            return decrypted
        
        dec_arr = decrypt_cesar(input_items[0] , self.key)
        output_items[0][:] = dec_arr
        
        return len(output_items[0])
