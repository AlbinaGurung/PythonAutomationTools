#Image Resizer
from PIL import Image
import os

input_folder="/Users/albinagurung/Desktop/images"
output_folder="/Users/albinagurung/Desktop/"

#loop through the images in the folder
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        path=os.path.join(input_folder,filename)
        img=Image.open(path)
        
        #Maintain the aspect ratio to make the image natural-looking and avoid image stretching or squishing
        # OR width,height=img.size
        new_width=200
        width_percent=new_width/img.size[0]
        new_height=int(img.size[1]*width_percent)
       
        #Display image old and new aspect ratio
        print('Name of image:',filename)
        print('Old aspect ratio:',img.size[0],'*',img.size[1])
        
        img=img.resize((new_width,new_height)) #Re-sizing
        
        print('New aspect ratio:',new_width,'*',new_height)
        
        #make new folder
        os.makedirs(os.path.join(output_folder,"Resized"),exist_ok=True)
        new_path=os.path.join(output_folder,"Resized",filename)   
        img.save(new_path)
print("All images resized!")
