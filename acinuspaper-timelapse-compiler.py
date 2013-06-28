'''
Script to 'latexmk' every revision of the acinus-paper.
'''

import os
import subprocess
import glob

# Setup
SaveToDirectory = os.path.join('c:\\', 'Users', 'haberthu', 'Desktop',
    'Dropbox', 'Work', 'AcinusPaperTimeLapse')

# Get SVN info from remote repository
(Output, Error) = subprocess.Popen(('svn', \
                                    'info',\
                                    'http://code.ana.unibe.ch/svn/' + \
                                    'AcinusPaper'),
                                    stdout=subprocess.PIPE,
                                    shell=True).communicate()

# Do some string manipulation to find the highest revision number
# The 'Output' above contains 'Revision: $RevisionNumber', thus find the first
# occurrence of 'Revision' in Output, and use the two digits that come after it
# If we have more than 99 revisions 2 will need to be changed to 3. :)
MaxRevision = int(Output[Output.find('Revision') + len('Revision: '):
                         Output.find('Revision') + len('Revision: ') + 2])

#~ silent = True
#~ # Go into each folder and 'latexmk' this thing
#~ for Revision in range(1, MaxRevision + 1):  # from 1 to MaxRev, not between
    #~ Directory = os.path.join(SaveToDirectory,
                            #~ 'PaperRevision' + "%02d" % Revision)
    #~ print 'Latexmk-ing revision', Revision
    #~ os.chdir(Directory)
    #~ nirvana = open("NUL", "w")
    #~ # compile even with errors (for some revisions we're missing the images)
    #~ subprocess.call('latexmk -pdf -silent *.tex', stdout=nirvana,
                    #~ stderr=nirvana,shell=True)
    #~ # cleanup after compilation
    #~ subprocess.call('latexmk -c *.tex', stdout=nirvana, stderr=nirvana,
                    #~ shell=True)
    #~ nirvana.close()

silent = True
# Go into each folder and make a montage of the PDF
# Commandline call based on one of wiki pages http://is.gd/rpQHVk and help from
# http://is.gd/ArtPrA
# > montage -density 300 album.pdf -mode Concatenate -tile 2x1 -quality 80
# >-resize 800 two_page.jpg
for Revision in range(1, MaxRevision + 1):  # from 1 to MaxRev, not between
    Directory = os.path.join(SaveToDirectory,
                            'PaperRevision' + "%02d" % Revision)
    print 'Compiling all pages of Revision', Revision, 'into a mosaic'
    os.chdir(Directory)
    subprocess.call('montage -density 300 *.pdf -mode Concatenate -tile' +\
                    ' 16x9 -resize 4096 out-' + str(Revision) + '.jpg',
                    shell=True)
