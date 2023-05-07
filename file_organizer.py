import os
import sys
import time
import requests
import datetime

version = "1.0.2"
args = sys.argv[1:]

def getActions():
        print("Choose a action:")

        actions = []
        for folder in os.listdir("logs"):
            for file in os.listdir("logs/" + folder):
                if file == "actions.txt":
                    actions.append(datetime.datetime.fromtimestamp(int(folder)).strftime("%d/%m/%Y %H:%M:%S"))

        for i in range(len(actions)):
            print(str(i + 1) + ". " + actions[i])

        action = input("Action: ")

        if action.isdigit():
            action = int(action)
            for folder in os.listdir("logs"):
                for file in os.listdir("logs/" + folder):
                    if file == "actions.txt":
                        if datetime.datetime.fromtimestamp(int(folder)).strftime("%d/%m/%Y %H:%M:%S") == actions[action - 1]:
                            act = open("logs/" + folder + "/actions.txt", "r")
                            print(act.read())
                            act.close()
                            sys.exit()

        


def createactions(actions):
    timestamp = str(int(time.time()))
    if not os.path.exists("logs"):
        os.mkdir("logs")
    if not os.path.exists("logs/" + timestamp):
        os.mkdir("logs/" + timestamp)
    
    act = open("logs/" + timestamp + "/actions.txt", "w+")

    for action in actions:
        act.write("[ " + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " ] " + action + "\n")

    act.close()
        



def check_for_updates():
    response = requests.get("https://api.github.com/repos/0xhylia/file-organizer/releases/latest")
    if response.status_code == 200:
        json = response.json()
        if json["tag_name"] != version:
            return "There is a new version available. You can download it from https://github.com/0xhylia/file-organizer/releases/latest"
        else:
            return True
    else:
        return "There was an error checking for updates. Please try again later."



def clear():
    os.system("cls" if os.name == "nt" else "clear")





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


if len(args) > 0 and args[0] == "--actions":
    getActions()

def get_files(path):
    files = []
    for file in os.listdir(path):
        if file != os.path.basename(__file__):
            if not os.path.isdir(file):
                if not os.path.splitext(file)[1]:
                    continue
                files.append(file)
                
    return files


things_did = []

def main():

    if check_for_updates() != True:
        print(check_for_updates())
        sys.exit()
    clear()
    print("Welcome to File Organizer!")
    print("Version: " + version)
    print("Author: 0xhylia")
    print("Github: https://github.com/0xhylia/file-organizer")
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
                        things_did.append("Moved " + file + " to " + type + " folder")
                        break

        print("Done!")
        createactions(things_did)

    elif choice.lower() == "n":
        print("Exiting...")
        sys.exit()

    else:
        main()


if __name__ == "__main__":
    main()