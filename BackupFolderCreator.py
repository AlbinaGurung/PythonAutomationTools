#Folder backup 
import shutil
import os
from datetime import datetime

source = "/Users/albinagurung/Desktop/important_files"
backup_folder = "backup"

date = datetime.now().strftime("%Y-%m-%d")

destination = os.path.join(backup_folder, f"backup_{date}")

shutil.copytree(source, destination)

print("Backup created:", destination)

#Note: Shutil is defined inside the python installation itself.
#shutil.copytree():copies the entire directory or folder to another location
#shutil.copy():copies just a file
#shutil.move():move files
#shutil.rmtree():for deleting the folder
#shutil.make_archive():create zip folders
#move vs copy: move takes the file to the new location with out leaving the original file in the source.
# copy will simply create a copy of the original file
# and also leaves the original file in the source.
#shutil.move():can also rename files.
