import os, re

rootdir = './Downloads/'
patterninit = r".+?(?=-modifi)"
patternext = r".+?-modifi..+?(..+)"
list_modifie = []

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if re.search(patterninit, file):
            filetmp = re.match(patterninit, file).group(0) + re.match(patternext, file).group(1)
            list_modifie.append(filetmp)

for elt in list_modifie:
    os.remove(rootdir + elt)