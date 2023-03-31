# Write n 100MB random text files to the File100 directory

import random
import string
import os
import shutil

# Create the folder
os.mkdir('File100')

# Create the files
n=10 # number of files
size=10 # MB
for i in range(n):
    filename = 'File100/' + str(i) + '.txt'
    with open(filename, 'w') as f:
        for j in range(size*1000000):
            f.write(random.choice(string.ascii_letters))
    print('File', i, 'created')
    print('File size:', os.path.getsize(filename), 'bytes')

# Compress the folder
shutil.make_archive('File100', 'zip', 'File100')

# Delete the folder
shutil.rmtree('File100')

