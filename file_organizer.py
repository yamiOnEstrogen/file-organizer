import os
import sys
import time


def clear():
    os.system("cls" if os.name == "nt" else "clear")


args = sys.argv[1:]


types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".tiff", ".psd", ".raw", ".bmp", ".heif", ".indd", ".svg", "webp"],
    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
    "Audio": [".mp3", ".wav", ".ogg", ".m4a", ".m4b", ".m4p", ".m4r", ".aac", ".aiff", ".wma", ".flac", ".alac"],
    "Documents": [".doc", ".docx", ".pdf", ".odt", ".xls", ".xlsx", ".ods", ".ppt", ".pptx", ".txt", ".rtf", ".tex"],
    "Archives": [".zip", ".7z", ".rar", ".tar", ".gz", ".pkg", ".deb"],
    "Disc": [".iso", ".img", ".dmg", ".toast", ".vcd"],
    "Database": [".sql", ".csv", ".dat", ".db", ".dbf", ".log"],
    "Executables": [".exe", ".apk", ".bat", ".cgi", ".pl", ".com", ".gadget", ".jar", ".msi", ".wsf"],
    "Fonts": [".ttf", ".otf", ".fon", ".fnt"],
    "Presentations": [".key", ".odp", ".pps", ".pptx"],
    "Programming": [".py", ".c", ".class", ".cpp", ".cs", ".h", ".java", ".sh", ".swift", ".vb", ".js", ".php", ".html", ".css", ".scss", ".less", ".json", ".go", ".pl", ".lua", ".rb", ".ts", ".as", ".vb", ".xhtml", ".jsp", ".jspx", ".wss", ".do", ".action", ".pl", ".cgi", ".php4", ".php3", ".phtml", ".py", ".pyc", ".pyo", ".rhtml", ".shtml", ".xml", ".rss", ".svg", ".md"],
    "Spreadsheets": [".ods", ".xls", ".xlsm", ".xlsx"],
    "System": [".bak", ".cab", ".cfg", ".cpl", ".cur", ".dll", ".dmp", ".drv", ".icns", ".ico", ".ini", ".lnk", ".msi", ".sys", ".tmp", ".pem"],
    "Web": [".asp", ".aspx", ".cer", ".cfm", ".csr", ".css", ".dcr", ".htm", ".html", ".js", ".jsp", ".php", ".rss", ".xhtml", ".cgi", ".pl", ".py", ".xhtml", ".rss", ".xml", ".js", ".jsp", ".jspx", ".wss", ".do", ".action", ".pl", ".cgi", ".php4", ".php3", ".phtml", ".py", ".pyc", ".pyo", ".rhtml", ".shtml", ".xml", ".rss", ".svg"],
    "Disk Image": [".bin", ".dmg", ".iso", ".toast", ".vcd"],
    "Shortcut": [".lnk", ".url"],
    "Torrent": [".torrent"],
    "Settings": [".cfg", ".ini", ".prf", ".env", ".properties", ".settings", ".theme", ".plist", ".reg", ".sif"],
    "Web Browser": [".bookmark", ".crdownload"],
    "Unity": [".unitypackage", ".vrm"],
}

if len(args) > 0 and args[0] == "--list":
    for type in types:
        print(type + ": " + str(types[type]))
    sys.exit()

def get_files(path):
    files = []
    for file in os.listdir(path):
        if file != os.path.basename(__file__):
            files.append(file)
    return files

clear()
print("Enter the path to the folder you want to organize: ")
path = input()


if not os.path.exists(path):
    print("The path does not exist")
    sys.exit()

files = get_files(path)



print("Are you sure you want to organize the files in this folder? (y/n)")
choice = input()

if choice.lower() == "y":
    print("Organizing files...")
    intial_file_count = len(files)
    files_organized = 0

    for file in files:
        if file != os.path.basename(__file__):
            for type in types:
                if file.endswith(tuple(types[type])):
                    if not os.path.exists(path + "/" + type):
                        os.mkdir(path + "/" + type)
                    os.rename(path + "/" + file, path + "/" + type + "/" + file)
                    files_organized += 1
                    print(str(files_organized) + " / " + str(intial_file_count))
                    time.sleep(1)
                    break

    print("Done!")

elif choice.lower() == "n":
    print("Exiting...")
    sys.exit()

else:
    print("Invalid input please try again [y/n]")
    sys.exit()