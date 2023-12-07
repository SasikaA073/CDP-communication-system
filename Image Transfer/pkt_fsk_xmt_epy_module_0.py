# this module will be imported in the into your flowgraph


import numpy as np
from gnuradio import gr
from gnuradio import blocks

class MyFlowgraph(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self)
        
        # Create the file chooser widget
        self.file_chooser = blocks.file_chooser("Select Image", False)
        
        # Connect the file chooser output to the parameter setter block
        self.connect(self.file_chooser, (self.setter, 0))

        # Create your embedded Python block
        self.python_block = ImageLossCalculator("default_path")  # Provide a default path
        
        # Connect blocks within your flowgraph
        self.connect((self.setter, 0), (self.python_block, 0))

fg = MyFlowgraph()
fg.run()
    

