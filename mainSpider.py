########################################################################################################################
# Author: Enders Kong                                                                                                  #
# This is a quick and dirty search program that can either search by file name, extension, or contents in .docx and    #
# .txt files depending on args passed in. Very slow and inefficient currently.                                         #
########################################################################################################################


# Use the following strings for the following modes:
#   byname: searches for files by name
#   intext: searches in .txt and .docx files for a substring
#   byext: searches by file extension
# The search_string arg is what to search by
# The drive arg points it at a drive

# !!!!!WINDOWS ONLY CURRENTLY!!!!!
# for linux set currpath to os.path.join(os.sep, 'usr', 'lib')

# TODO: make it not asstastically slow
# TODO: add finer controls, and add generalizations for search_string

from docx import Document
import os
import argparse

# note: this will go through every file you have. do not put on systems with large number of files. will take a while to
# finish searching.
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", type = str, help = "Use the following strings for the following modes:\n\tbyname: searches for files by name\n\tintext: searches in .txt and .docx files for a substring\n\tbyext: searches by file extension")
    parser.add_argument("search_string", type = str, help = "String to search by.")
    parser.add_argument("drive", type = str, help = "Drive to search")
    args = parser.parse_args()
    currpath = os.path.join(args.drive, os.sep, 'sourcedir')
    # search by name
    if (args.mode == "byname"):
        # go through every dir reachable from a root of currpath
        for root, dirs, files in os.walk(currpath):
            # walk through files in dir
            for name in files:
                # if name exists or is part of a file name spit out file path
                subsstrExists = str(name).find(args.search_string)
                if (subsstrExists != -1):
                    print(root + "/" + str(name))
    # searches by file extension
    if (args.mode == "byext"):
        for root, dirs, files in os.walk(currpath):
            for name in files:
                if name.endswith(args.search_string):
                    print(root + "/" + str(name))
    # searches inside .docx and .txt files
    if (args.mode == "intext"):
        for root, dirs, files in os.walk(currpath):
            for name in files:
                if name.endswith(".docx"):
                    # for storing strings of paragraphs
                    docTextList = []
                    # open .docx file at current position in dir
                    currDoc = Document(os.path.join(root, name))
                    for paragraph in currDoc.paragraphs:
                        docTextList.append(paragraph.text)
                    # condense to single string
                    docText = " ".join(docTextList)
                    subsstrExists = docText.find(args.search_string)
                    if (subsstrExists != -1):
                        print(root + "/" + str(name))
                # essentially the same but for .txt files
                elif name.endswith(".txt"):
                    txtTextList = []
                    currTxt = open(name, "r")
                    for line in currTxt:
                        txtTextList.append(line)
                    txtText = " ".join(txtTextList)
                    subsstrExists = txtText.find(args.search_string)
                    if (subsstrExists != -1):
                        print(root + "/" + str(name))