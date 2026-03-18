#Downloads Manager Professional version 2 (folders inside folder)
import os
folder="/Users/albinagurung/Downloads"
# folder2="Downloads/Video"
# for file_name in os.listdir(folder2):
#     old_path=os.path.join(folder2,file_name)
#     new_path=os.path.join(folder,file_name)
#     os.rename(old_path,new_path)
# os.rmdir(folder2)

file_types={
    "Images":[".jpg",".png",".jpeg"],
    "Audio":[".mp3",".wav"],
    "Video":[".mp4",".mov",".avi"],
    "Documents":[".pdf",".txt",".docx",".xlsx"]
    }
for filename in os.listdir(folder):
    old_path=os.path.join(folder,filename)
    if os.path.isfile(old_path):
        moved=False
        for folder_name,extensions in file_types.items():
            for extension in extensions:
                if filename.lower().endswith(extension):
                    #make a new folder
                    outer_folder=os.path.join(folder,folder_name)
                    os.makedirs(outer_folder,exist_ok=True)
                    inner_folder=os.path.join(outer_folder,extension.strip("."))
                    os.makedirs(inner_folder,exist_ok=True)
                    #rename the file 
                    new_path=os.path.join(inner_folder,filename)
                    os.rename(old_path,new_path)
                    moved=True
                    break
            
         #move unknown files to others folder
        if moved is not True:
                new_folder=os.path.join(folder,"Others")
                os.makedirs(new_folder,exist_ok=True)
                new_path=os.path.join(new_folder,filename)
                os.rename(old_path,new_path)
                
print("Files Organized Successfully!")
                
