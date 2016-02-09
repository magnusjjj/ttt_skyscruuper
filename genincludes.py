import os

rootdir = "C:\\Users\\Magnus\\Desktop\\list\\skyscruuper\\includes"

f = open("includes.txt", "w")

writy = ""

for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		print(subdir[len(rootdir)+1:] + "\\" + file)
		writy += subdir[len(rootdir)+1:] + "\\" + file + "\n"
		writy += os.path.join(subdir, file) + "\n"
		print(os.path.join(subdir, file))

f.write(writy)
f.close()