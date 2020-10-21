
from sys import argv
from pathlib import Path
from PIL import Image
 

input_folder = argv[1]
output_folder = argv[2] 
try:
	input_folder_length = len(input_folder)
	Path(input_folder).mkdir(exist_ok=True)
	Path(output_folder).mkdir(exist_ok=True)
	path_list = Path(input_folder).glob("**/*.jpg")
	for path in path_list:
		path_in_string = str(path)
		pic_name = path_in_string[input_folder_length:-4]
		img = Image.open(path_in_string)
		img.save(f"{output_folder}/{pic_name}.png")
		print(pic_name)		
except ValueError as err:
	print(err) 
except IndexError:
	print('enter both input and output file name') 
