import os

def main(start_path='.'):
	for root, dirs, files in os.walk(start_path):
		for file in files:
			filename = os.path.join(root, file)
			if filename.endswith("_en.srt"):
				# print(filename)
				new_name = filename[:-7] + ".srt"
				os.rename(filename, new_name)
	

if __name__ == '__main__':
	# Calling main() function
	# Specify the directory path you want to start from
	directory_path = './'
	main(directory_path)




# Old code
# Function to rename multiple files
# def main():
#	i = 0
#	path="."
#	for filename in os.listdir(path):
		# # # print(filename)
#		if filename.endswith("_en.srt"):
#			new_name = filename[:-7] + ".srt"
#			os.rename(filename, new_name)
		# my_dest ="new" + str(i) + ".srt"
		# print(my_dest)
		# my_source =path + filename
		# my_dest =path + my_dest
		# rename() function will
		# rename all the files
		# os.rename(my_source, my_dest)
		# i += 1
# Driver Code
# if __name__ == '__main__':
	# Calling main() function
	# main()