import os
folder="/Users/albinagurung/Desktop/images"
for count,filename in enumerate(os.listdir(folder)):
    new_name=f"Product_{count+1}.jpg"
    os.rename(os.path.join(folder,filename), 
              os.path.join(folder,new_name)) #os.path.join is used to create the full path for both the old and new file names, ensuring that the files are renamed correctly regardless of the operating system.
print("Files Renamed Successfully!")