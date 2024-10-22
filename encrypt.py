import os
import cv2
import time
import Image as i
import reshape as res
import diffusion as dif
import confusion as con
from PIL import ImageTk, Image

def encrypt(filepath, destination_path, key):
    im_original = i.Image(filepath, i.Type.ORIGINAL, cv2.imread(filepath), key)
    print(im_original.filename)
    print(im_original.dimension)

    path = os.path.join('.', 'images')

    # Reshape the image into square
    start_time = time.perf_counter()
    im_reshaped = i.Image(path+"\\reshaped\\"+im_original.filename.split('.')[0]+".png", i.Type.RESHAPED, res.squareImage(im_original), key)
    elapsed_time = time.perf_counter() - start_time
    print(f"Elapsed time: {elapsed_time:0.4f} seconds")
    # Save the output of reshape
    # cv2.imwrite(im_reshaped.filepath, im_reshaped.matrix)
    
    # Begin confusion
    start_time = time.perf_counter()
    im_confused = i.Image(path+"\\confused\\"+im_original.filename.split('.')[0]+".png", i.Type.CONFUSED, con.generateArnoldMap(im_reshaped), key)
    elapsed_time = time.perf_counter() - start_time
    print(f"Elapsed time: {elapsed_time:0.4f} seconds")
    # Save the output of confusion
    # cv2.imwrite(im_confused.filepath, im_confused.matrix)

    # Begin diffusion
    # start_time = time.perf_counter()
    im_diffused = i.Image(destination_path+"\\"+im_original.filename.split('.')[0]+".png", i.Type.ENCRYPTED, dif.pixelManipulation(im_confused), key)
    # elapsed_time = time.perf_counter() - start_time
    # print(f"Elapsed time: {elapsed_time:0.4f} seconds")
    cv2.imwrite(im_diffused.filepath, im_diffused.matrix)