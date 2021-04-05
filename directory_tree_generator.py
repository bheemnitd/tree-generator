import os
from docopt import *
from colr import color
import os
from PIL import Image, ImageDraw, ImageFont

colors = ['#f891a0', '#6389df']

def tree_generator(path, files_and_folders):

	for files in os.walk(path):
		
		print("\n")
		for file in files:
			files_and_folders+=color("\n|--"+path+file, colors[0])

	return(files_and_folders)



def directory(path):

	for dirs in path:
			path+=dir+"/"
			files_and_folders+=color("\n+--"+path, colors[1])		
			tree_generator(path, files_and_folders)



files_and_folders=""			

#paste your path here
tree_structure = tree_generator("/home/sam/Desktop/my doc/", files_and_folders)
print(tree_structure)
   