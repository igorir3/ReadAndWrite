import os

FolderMain = " "
FolderCurrent = " "
FolderMain = os.getcwd()
idid = 0

FolderCurrent = input("Folder for writing: ")
fileinputname = input("File name: ")
filename = FolderMain + "\\" + fileinputname + ".txt"
textfile = open(filename, "w")

files = os.listdir(FolderCurrent)

while idid != len(files):
	text = str(idid + 1) + " - " + files[idid]
	textfile.write(text)
	textfile.write("\n")
	print("{idnum} - {Name}".format(idnum = idid + 1, Name = files[idid]))
	idid = idid + 1
exit = input("Done!")