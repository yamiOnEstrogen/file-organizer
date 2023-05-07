import os


files = ["this_is_a_zip_file.zip", "text.txt", "music.mp3", "Video.mp4", "Python.py", "javascript_file.js"]

def createfile(file):
    f = open(file, "w+")
    f.close()


for file in files:
    if os.path.exists(file):
        os.remove(file)
        print("Sorry, the file " + file + " already exists")
    else:
        createfile(file)