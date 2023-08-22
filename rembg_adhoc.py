from rembg import remove, new_session 
from PIL import Image
import os
TRANSFORM_FOLDER = "TRANSFORMS"

#test rembg capabilities without going through the whole process
def remove_bg(filename):
    input_path = filename
    output_path =  filename + ".png"
    print(input_path)
    print(output_path)
    input = Image.open(input_path)
    session = new_session('u2net_cloth_seg')
    output = remove(input, 
        session=session, 
        alpha_matting=True, 
        alpha_matting_foreground_threshold=190,
        alpha_matting_background_threshold=4,
        alpha_matting_erode_size=14,
        )
    print(output)
    output.save(output_path)
    return output_path

remove_bg('foo.png')
