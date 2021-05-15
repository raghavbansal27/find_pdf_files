#! python3
# find_pdfs.py Program that walks through a folder tree and searches for files with
#                          extension .pdf and print absolute file of that path and print the file
#                          using printer
import os
from path_file import path
from sys import platform

PATH = path


def filePath(folder):
    pdf_files = []
    os.path.abspath(folder)
    for folderName, subFolders, filesname in os.walk(folder):
        for files in filesname:
            if files.endswith('.pdf'):
                pdf_files.append(os.path.join(folderName, files))

    return pdf_files, len(pdf_files)


print("Finding pdfs...")
pdf_files, num = filePath(PATH)

print("Found {} pdfs".format(num))
for pdf in pdf_files:
    print(pdf)

if platform == "linux" or platform == "linux2":
    print("\nPrinting files...")
    for pdf in pdf_files:
        try:
            command = "lp " + pdf
            os.system(command)
        except:
            print("Printer error...")

elif platform == "win32":
    print("\n\nPrinting files...")
    ask = input("Want to use default printer? [y/n]:")
    counter = 1
    if ask == 'y' or ask == 'Y':
        for pdf in pdf_files:
            try:
                command = 'PDFtoPrinter.exe "'+ pdf + '" '
                os.system(command)
                print("Printed ", counter, "pdfs")
                counter += 1
            except:
                print("Printer error...")
    elif ask == 'n' or ask == "N":
        printer_name = input("Enter printer name: ")
        for pdf in pdf_files:
            try:
                command = 'PDFtoPrinter.exe "'+ pdf + '" "' + printer_name + '"'
                os.system(command)
                print("Printed ", counter, "pdfs")
                counter += 1
            except:
                print("Printer error...")
