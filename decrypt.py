import os
import cv2
import time
import Image as i
import reshape as res
import diffusion as dif
import confusion as con
from PIL import ImageTk, Image

def decrypt(filepath, destination_path, key):
    im_encrypted = i.Image(filepath, i.Type.ENCRYPTED, cv2.imread(filepath, cv2.IMREAD_UNCHANGED), key)
    print(im_encrypted.filename)

    path = os.path.join('.', 'images')
    
    # Begin undiffusion
    im_undiffused = i.Image(path+"\\undiffused\\"+im_encrypted.filename.split('.')[0]+".png", i.Type.UNDIFFUSED, dif.pixelManipulation(im_encrypted), key)
    # Save the output of undiffusion
    # cv2.imwrite(im_undiffused.filepath, im_undiffused.matrix)

    # Begin unconfusion
    start_time = time.perf_counter()
    im_unconfused = i.Image(path+"\\unconfused\\"+im_encrypted.filename.split('.')[0]+".png", i.Type.UNCONFUSED, con.reconstructArnoldMap(im_undiffused), key)
    elapsed_time = time.perf_counter() - start_time
    print(f"Elapsed time: {elapsed_time:0.4f} seconds")
    # Save the output of unconfusion
    # cv2.imwrite(im_unconfused.filepath, im_unconfused.matrix)

    # Reshape crop border
    start_time = time.perf_counter()
    im_decrypted = i.Image(destination_path+"\\"+im_encrypted.filename.split('.')[0]+".png", i.Type.DECRYPTED, res.cropBorder(im_unconfused), key)
    elapsed_time = time.perf_counter() - start_time
    print(f"Elapsed time: {elapsed_time:0.4f} seconds")
    cv2.imwrite(im_decrypted.filepath, im_decrypted.matrix)