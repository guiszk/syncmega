import os
from mega import Mega

mega = Mega()

m = mega.login("login", "password") #change to personal credentials
files = m.get_files()

def difference(list1, list2):
   dif = [i for i in list1 + list2 if i not in list1 or i not in list2]
   return dif

megafolder = m.find('folder') #mega folder to upload to
localfolder = '~/folder' #local folder to sync

megafiles = [files[i]['a']['n'] for i in files if files[i]['a']['n'].endswith('m4a')]
localfiles = [i for i in os.listdir(localfolder) if i.endswith('m4a')]
dif = difference(megafiles, localfiles)

if(len(dif) > 0):
    for i in dif:
        m.upload(os.path.join(localfolder, i), megafolder[0])
