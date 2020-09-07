import tkinter as tk
from tkinter import filedialog
import os.path

# this sets working directory and gets the file to convert
root = tk.Tk()
root.withdraw()
base = os.getcwd().replace(os.sep, "/")
file_path = filedialog.askopenfilename()
# print(file_path)


converter_file_string = ""

# this is important, the file structure was downloaded like this
# so I am assuming this is how it was put in the folder
converter_location = "Converter/bin"

for i in range(0, 20):
    # current settings are to convert to an mp4
    current_file = "output" + str(i) + ".mp4"
    if not os.path.exists(base + "/" + converter_location + "/" + current_file):
        break

if file_path != "":
    # added quotes on either side in case there is spaces within the paths
    converter_exe = r'"' + base + "/" + converter_location + "/" + "ffmpeg.exe" + r'"'
    input_file = r'"' + file_path + r'"'
    
    # modify this if you prefer a different output, currently it outputs to the directory of the ffmpeg executable
    output_file = r'"' + base + "/" + converter_location + "/" + current_file + r'"'
    
    converter_file_string = converter_exe + " -i " + input_file + " " + output_file

    # print(converter_file_string)
else:
    quit()


converter_file_full = os.getcwd() + "/" + converter_location + "/" + "convert.bat"

# overwrites the bat file to the new files/settings without extra hastle
with open(converter_file_full, "w") as f:
    f.write(converter_file_string)


print("converting file")

os.system(converter_file_full)

print("Done")
