'''
Using Pandas to process the entire bird file by using chunks and not reading 
it all into memory at once. Then write it to a new file.
'''

from helper import clean_regions, clean_bird_chunks