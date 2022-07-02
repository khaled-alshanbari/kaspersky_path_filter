import os
import re
from tkinter import filedialog


def get_Desktop():
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    return desktop

path = str(filedialog.askopenfilename(initialdir=get_Desktop(), title='Select a file to Extract path')).strip()
with open(path,'r') as file:
    data = file.read()

path_regex = r"(?:\\\\[^\\]+|[a-zA-Z]:)((?:\\[^\\\n]+)+\\)?([^<>:\n]*)"
exe_regex = ".*[A-za-z]{1,}.exe"
dll_regex = ".*[A-za-z]{1,}.dll"
msi_regex = ".*[A-za-z]{1,}.msi"


matches = re.finditer(path_regex, data)
with open(get_Desktop()+"/WhiteList_Filtred.txt",'w+') as file:
    file.write("Paths found in ("+path+")\n\n\n\n")
    for matchNum, match in enumerate(matches, start=1):
        if match.group() != None:
            file.write(match.group())
            file.write("\n\n")
    file.write("\n\n------------------------------------------------\n\n")
    file.write("\n\n\n\nEXE found in (" + path + ")\n\n\n\n")
    matches = re.finditer(exe_regex, data)
    for matchNum, match in enumerate(matches, start=1):
        if match.group() != None:
            file.write(match.group())
            file.write("\n\n")

    file.write("\n\n------------------------------------------------\n\n")
    file.write("\n\n\n\nDLL found in (" + path + ")\n\n\n\n")
    matches = re.finditer(dll_regex, data)
    for matchNum, match in enumerate(matches, start=1):
        if match.group() != None:
            file.write(match.group())
            file.write("\n\n")
    file.write("\n\n------------------------------------------------\n\n")
    file.write("\n\n\n\nMSI found in (" + path + ")\n\n\n\n")
    matches = re.finditer(msi_regex, data)
    for matchNum, match in enumerate(matches, start=1):
        if match.group() != None:
            file.write(match.group())
            file.write("\n\n")







# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.

