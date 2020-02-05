# Walk a directory tree and archive every file except the .txt and .py ones.

import zipfile, os

os.chdir("/Users/ramteechua/Desktop/Desktop-Files/test")

# Put absolute path here.
directory = "/Users/ramteechua/Desktop/Desktop-Files/test/hello-world-fun-folder"

zip_file_name = os.path.basename(directory) + ".zip"
example_zip = zipfile.ZipFile(zip_file_name, "w")

for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:

        # Doesn't add files zip if it ends with the text inputted.
        if filename.endswith(".py") or filename.endswith(".txt"):
            pass
        else:
            example_zip.write(os.path.join(dirpath, filename), arcname=filename)

example_zip.close()
print("Done.")

