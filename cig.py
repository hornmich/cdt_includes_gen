"""
    Eclipse CDT settings file generator for automated includes list definition.
 
"""
import os


def folders(root, fileSuffixes) :
    """
        Get a set of directories that contain files with given extensions.
        
        The directories are with absolute paths.

        root -- root directory to recursively search from
        fileSuffixes -- list of file extensions to search for
    """
    folders = set()
    for path, subFolders, files in os.walk(root):
        files = [fileName for fileName in files if os.path.splitext(fileName)[1] in fileSuffixes]
        if files:
            folders.add(path)

    return folders

def generateXML(outFileName, CIncludes, CppIncludes):
    """
        Generate Eclipse CDT settings XML file with C and C++ includes.

        outFileName -- name of the output XML file.
        CIncludes -- List of directories containing C header files
        CppIncludes -- Liest of directories containing C++ header files
    """
    
    sections = [("C++", CppIncludes), ("C", CIncludes)]

    with open(outFileName, 'w') as outFile: 
        outFile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        outFile.write('<cdtprojectproperties>\n')
        outFile.write('<section name="org.eclipse.cdt.internal.ui.wizards.settingswizards.IncludePaths">\n')
        
        for name, lst in sections:
            if lst:
                outFile.write ('<language name="' + name +' Source File">\n') 
                for directory in lst:
                    outFile.write('<includepath>' + directory + '</includepath>' + '\n')
                outFile.write('</language>\n')
        outFile.write('</section>\n')
        outFile.write('</cdtprojectproperties>\n')  
