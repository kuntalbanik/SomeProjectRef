import os
# Function to rename multiple files
def main():
	i = 0
	path="."
	for filename in os.listdir(path):
		# print(filename)
		if filename.endswith("_en.srt"):
			new_name = filename[:-7] + ".srt"
			os.rename(filename, new_name)
		# my_dest ="new" + str(i) + ".srt"
		# print(my_dest)
		# my_source =path + filename
		# my_dest =path + my_dest
		# rename() function will
		# rename all the files
		# os.rename(my_source, my_dest)
		# i += 1
# Driver Code
if __name__ == '__main__':
	# Calling main() function
	main()