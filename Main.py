import tkinter as tk
from tkinter import filedialog
import os.path


root = tk.Tk()
root.withdraw()
base = os.getcwd().replace(os.sep, "/")

file_path = filedialog.askopenfilename()
print(file_path)


converter_file_string = ""
converter_location = "Converter/bin"

for i in range(0, 20):
    current_file = "output" + str(i) + ".mp4"
    if not os.path.exists(base + "/" + converter_location + "/" + current_file):
        break

if file_path != "":
    converter_file_string = r'"' + base + "/" + converter_location + "/" + "ffmpeg.exe" + r'"'\
                            + " -i " + r'"' + file_path + r'"' + " " + r'"' + base + "/"\
                            + converter_location + "/" + current_file + r'"'

    print(converter_file_string)
else:
    quit()


converter_file_full = os.getcwd() + "/" + converter_location + "/" + "convert.bat"

with open(converter_file_full, "w") as f:
    f.write(converter_file_string)


print("converting file")

os.system(converter_file_full)

print("Done")
