import os
import shutil

print("========= Automatic File Organizer =========")

path = input("Enter folder path: ")

files = os.listdir(path)

for file in files:

    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
        folder = path + "/Images"

    elif file.endswith(".pdf"):
        folder = path + "/PDFs"

    elif file.endswith(".docx") or file.endswith(".txt"):
        folder = path + "/Documents"

    elif file.endswith(".mp3"):
        folder = path + "/Music"

    elif file.endswith(".mp4"):
        folder = path + "/Videos"

    else:
        folder = path + "/Others"

    if not os.path.exists(folder):
        os.mkdir(folder)

    source = path + "/" + file
    destination = folder + "/" + file

    if os.path.isfile(source):
        shutil.move(source, destination)

print("Files Organized Successfully!")