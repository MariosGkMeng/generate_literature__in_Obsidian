
from dataclasses import fields
from genericpath import exists
from math import nan
from os import listdir
import os
from os.path import isfile, join
import sys


# USER PARAMETERS ==============================================================================================================================
D = dict({
        
        'fields_dataview':     ['year:: ',\
                                'place:: ',\
                                'topic:: #Topic/Exosceletons',\
                                'type:: #📕🕹/type-of-file--example--PhD-Thesis ',\
                                'date-downl:: ',\
                                'has_external_note:: ',\
                                'difficulty:: ',\
                                'percentage-read:: <progress max=100 value=0> </progress>',\
                                'keyw:: #🔑/Some-keyword ',\
                                'proj:: #🧪/Project-Name ' ,\
                                'comm::',\
                                'citation_style_1::'],
        
                    '📂':       dict({ 'trigger': 'CMD__GET_PUB.md',
                                      'pdf-files': 'Literature\\Notes'}),
                    
    'trigger-file-fields':      ['pub', 'path']
})
# ==============================================================================================================================


# \==================================================
# Print fields 
# All the dataview fields that the user wants to have automatically
tmp1 = '\n'.join(D['fields_dataview']) + '\n'
# \==================================================

# Get the path of the file that triggers this python script =====================================================================================
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
    # file_path = sys._MEIPASS
    pth00 = os.path.dirname(sys.executable)
elif __file__:
    pth00 = os.path.dirname(__file__)
# ==========================================================================================================================================================================

# Parse the .md file that triggers the command
pth0 = pth00 + '\\' + D['📂']['trigger']
file1 = open(pth0, 'r', encoding='UTF8')
Lines = file1.readlines()
file1.close()
flds = D['trigger-file-fields']

vals = dict()

for ln in Lines:
    for f in flds:
        ftmp = f+':: '
        if f+':: ' in ln:
            vals[f] = ln.replace(ftmp, '')
            if "pub" in f:
                vals[f] = vals[f].replace('[[', '').replace(']]', '').replace('p', '')

            vals[f] = (vals[f]).replace('\n', '')

            
# Path that contains the .pdf files           
literature_path = vals['path']

# \==================================================

# Get list of files in the path
only_files = [f for f in listdir(literature_path) if isfile(join(literature_path, f))]

# Create list of all .pdf files that start with a number followed by either:
#       1. a dot: e.g.: "145. XXXXX.pdf"
#       2. the prefix "fr", a number and then a dot (e.g.: "145fr12. XXXXX.pdf", 
#          indicating that pdf 145 was downloaded because it was cited in 145)
pdfNum = []
for f in only_files:
    if '.' in f:
        idx = f.find('.')
        fdot = f[:idx]
        if fdot.isnumeric():
            pdfNum.append(fdot)
        elif 'fr' in fdot:
            ftmp = fdot.split('fr')
            if ftmp[0].isnumeric(): 
                pdfNum.append(ftmp[0])
        else:
            pdfNum.append(nan)
   
# Current publication number and corresponding .pdf file
pubno = vals['pub']    
flnm = only_files[pdfNum.index(pubno)]
pub_title = flnm[flnm.find('.')+1:]

ff1=flnm.replace(pubno+'. ', '')
ff1=ff1.replace(pubno+'.', '').replace('.pdf','')

# write px.md \==================================================\==================================================\==================================================\==================================================
Lines0 = []
Lines0.append('#pub/p' + pubno + '\n'*2)

# Append link to pdf that opens in explorer
Lines0.append('l:: [🔗](<file:///' + literature_path + '\\' + flnm + '>)'+ '\n'*2)

# Append title to fields
tmp1 = 'title:: ' + ff1 + '\n' + tmp1
Lines0.append(tmp1)

# Append wiki-like-link to pdf
Lines0.append('## [[' + flnm + ']]'+ '\n'*2)

# Write file to:
filewr = pth00 + '\\Literature\\Notes' + '\\p' + pubno + '.md'
if not exists(filewr):
    filemd = open(filewr, 'w', encoding='UTF8')
    filemd.writelines(Lines0)
    filemd.close()
# \==================================================\==================================================\==================================================\==================================================\==================================================

