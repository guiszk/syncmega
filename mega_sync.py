import os
from mega import Mega
import sys

if(len(sys.argv) < 2):
    print(f"{sys.argv[0]} <local path> <remote path> <*file extension>")
    sys.exit(1)

mega = Mega()

m = mega.login("login", "password") #change to personal credentials
files = m.get_files()

def difference(list1, list2):
   dif = [i for i in list1 + list2 if i not in list1 or i not in list2]
   return dif

localfolder = sys.argv[1]
megafolder = m.find(sys.argv[2])

if(len(sys.argv) > 2):
    #only include files with matching extensions
    fileext = [i for i in sys.argv[3].split('.') if len(i) > 1][0]
    megafiles = [files[i]['a']['n'] for i in files if files[i]['a']['n'].endswith(fileext)]
    localfiles = [i for i in os.listdir(localfolder) if i.endswith(fileext)]
else:
    #all files
    megafiles = [files[i]['a']['n'] for i in files]
    localfiles = [i for i in os.listdir(localfolder)]
dif = difference(megafiles, localfiles)

if(len(dif) > 0):
    for i in dif:
        m.upload(os.path.join(localfolder, i), megafolder[0])
