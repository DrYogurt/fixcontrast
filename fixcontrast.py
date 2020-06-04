import matplotlib.pyplot as plt
import numpy as np
import easygui as gui
from PIL import Image
import glob


def fix(image,cutoff_value):
    cutoff = np.full(image.shape,cutoff_value)
    boolarr = image > cutoff
    return boolarr.astype('uint8') * 255

if __name__ == "__main__":
    pull = gui.fileopenbox("Please Select Images to Fix",filetypes=["*.png","*.jpg",".jpg"], multiple=True)
    save = gui.diropenbox("Please Select Save Directory")
    for filename in pull:
        im=Image.open(filename)
        fixed = Image.fromarray(fix(np.array(im),150))
        name = filename.split('/')[-1].split('.jpg')[0] + "_fixed.jpg"
        print("fixing: ", name)
        fixed.save(save+"/"+name)
