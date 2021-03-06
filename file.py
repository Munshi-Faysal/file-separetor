import os,shutil

folders = {
	'audios' : ['.mp3','.wav','.flac'],
    'videos' : ['.mp4','.mkv','.MKV','.flv','.mpeg'],
    'images' : ['.jpg','.jepg','png'],
    'documents' : ['.pdf','.doc','.txt','.xlsx','.rar','.zip','.xls','pptx'],


}


def rename_folder():
	for folder in os.listdir(directory):
		if os.path.isdir(os.path.join(directory,folder))==True:
			os.rename(os.path.join(directory,folder),os.path.join(directory,folder.lower()))


def create_move(extension,file_name):
	fname = False
	for folder_name in folders:
		if '.'+extension in folders[folder_name]:
			if folder_name not in os.listdir(directory):
				os.mkdir(os.path.join(directory, folder_name))

			shutil.move(os.path.join(directory,file_name),os.path.join(directory,folder_name))
			fname = True
			break

	if fname != True:
		if other_name not in os.listdir(directory):
			os.mkdir(os.path.join(directory,other_name))

		shutil.move(os.path.join(directory,file_name),os.path.join(directory,other_name))


directory= input('Enter your folder path: ')
other_name= input("Enter other folder's name: ")
rename_folder()
all_files = os.listdir(directory)
length = len(all_files)
count=1


for i in all_files:
	if os.path.isfile(os.path.join(directory,i))==True:
		create_move(i.split('.')[-1],i)
	print(f'Total files: {length}| Done : {count} | Left : {length-count} ')
	count+=1






