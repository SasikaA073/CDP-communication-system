from PIL import Image
import os

def detect_bladeRF():
    pass
    return True




class ImageFile:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)

    def get_image_resolution(self):
        width, height = self.image.size
        return f"{width}x{height} px"
    
    def get_image_size(self):
        return str(int(os.stat(self.image_path).st_size // 1000)) + " KB"
    
    def get_image_path(self):
        return self.image_path
