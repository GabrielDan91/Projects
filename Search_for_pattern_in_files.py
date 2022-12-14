# import zipfile
import os
import re
import time
# zip_file = zipfile.ZipFile("C:\\Users\\gabid\Desktop\\unzip_me_for_instructions.zip", "r")
# zip_file.extractall("C:\\Users\\gabid\\PycharmProjects\\Projects\\Diverse\\Modules_adv\\Homework")

path_fold = "C:\\Users\\gabid\\PycharmProjects\\Projects\\Diverse\\Modules_adv\\Homework\\extracted_content"
start_time = time.time()

for sub_forders, folder, files in os.walk(path_fold):
    # we iterate through os.walk
    for file in files:
        # we iterate through files generated by os.walk

        file_path = os.path.join(sub_forders, file)
        # we generate the absolute path of the files

        with open(file_path, 'r') as f: # we open the files in read mode
            for line in f.readlines(): # we iterate through file, and we generate a list with those lines
                pattern = re.compile(r'\d{3}-\d{3}-\d{4}')  # we establish the pattern of the thing that we are looking for
                results = re.findall(pattern, line)  # we search for the pattern in the lines of the folders
                for result in results: # condition to display only the find pattern
                    if len(results) > 0:
                        print(result)

end_time = time.time()
elapsed_time = end_time-start_time
print(f"The procesing time was: {elapsed_time}")
