'Programs to manipulate file system using recursion'
'Author: Harsh Vardhan(harshvardhan.mse@gmail.com)'
'First commit: Dec 04, 2016'

import os

####Function 1 (Base function)
#Get the direct children of the path
#Input: root = path of the root directory
#Output: list of all files and folders which are direct children of the root directory, in alphabetically sorted order 
def getDirList(root):
    try:
        dirlist = os.listdir(root)
        dirlist.sort()
        return dirlist
    except:
        return('Invalid input(s)')

#Examples
#getDirList('/home/ubuntu') 'For Ubuntu users. Warning: Long list. Please edit root to directory having less files to the deepest subdirectory.'
#getDirList('C:/Users/') 'For Windows users. Warning: Long list. Please edit root to directory having less files to the deepest subdirectory.'


####Function 2
#Collect paths (without hierarchy) for all files belonging to given root directory, to the deepest subdirectory directory level
#Input: root = path of the root directory
#Output: single list consisting of all file paths inside the given root directory, without any file system hierarchy
def flattenFileList(root):
    try:
        flatFileNames = []
        dirlist = getDirList(root)
        for item in dirlist:
            completePath = os.path.join(root, item)
            if(os.path.isdir(completePath)):
                flatFileNames.extend(flattenFileList(completePath))
            else:
                flatFileNames.append(completePath)
        return flatFileNames
    except:
        return('Invalid input(s)')

#Examples
#flattenFileList('/home/ubuntu') 'For Ubuntu users. Warning: Long list. Please edit root to directory having less files to the deepest subdirectory.'
#flattenFileList('C:/Users/') 'For Windows users. Warning: Long list. Please edit root to directory having less files to the deepest subdirectory.'

    
####Function 3
#Recursively create file inside all directories and subdirectories till deepest levels, of a given root
#Input: root = path of the root directory
#Output: all the directories and subdirectories to the deepest level, of the given root directory, has a file trash.txt created inside
def litter(root):
    try:
        dirlist = getDirList(root)
        for item in dirlist:
            completePath = os.path.join(root, item)
            if(os.path.isdir(completePath)):
                if(not(os.path.isfile(completePath + "/trash.txt"))):
                    f = open(completePath + "/trash.txt", "w")
                    f.close()
                    print("File created >  " + str(completePath) + "/trash.txt")
                litter(completePath)
    except:
        return('Invalid input(s)')

#Examples
#litter('/path/to/dummy/directory/') 'Warning: May create files inside your important directory. Use dummy directory instead.'
    
####Function 4
#Recursively clean files of selected name, inside all directories and subdirectories till deepest levels, of a given root
#Input: root = path of the root directory
#Input: filename = name of the file that has to be removed from all directories and subdirectories of the root
#Output: all the directories and subdirectories to the deepest level, of the given root directory, has a file trash.txt deleted frome
def cleanup(root, filename):
    try:
        dirlist = getDirList(root)
        for item in dirlist:
            completePath = os.path.join(root, item)
            if(os.path.isdir(completePath)):
                if(os.path.isfile(completePath + "/" + filename)):
                    os.remove(completePath + "/" + filename)
                    print("File Removed >  " + completePath + "/" + filename)
                cleanup(completePath, filename)
    except:
        return('Invalid input(s)')
    
#Examples
#cleanup('/path/to/dummy/directory/', 'trash.txt') 'Warning: May delete files inside your important directory. Use dummy directory instead.'
