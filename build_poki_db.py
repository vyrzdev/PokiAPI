import os
import imghdr
import mongoengine

database_conn_str = ""
mongoengine.connect(database_conn_str)
from src.models import PokiPic

print("Searching current working directory for pictures to add to DB.")

print("Recursive?")
resp = ""
while resp.lower() not in ["y", "n"]:
    resp = input("Y/N- ")

recursive = {"y": True, "n": False}.get(resp.lower())

if recursive:
    file_paths = []
    for dirpath, dirnames, files in os.walk('.', topdown=True):
        for file_name in files:
            file_paths.append(f"{dirpath}/{file_name}")

else:
    file_paths = []
    for entry in os.listdir("."):
        if os.path.isfile(os.path.join(".", entry)):
            file_paths.append(entry)

image_file_paths_and_formats = []
for file in file_paths:
    img_format = imghdr.what(file)
    if img_format is None:
        print(f"Ignored {file} as not image!")
    else:
        print(f"Found image: {file} of format {img_format}")
        image_file_paths_and_formats.append((file, img_format))

for image_path, image_format in image_file_paths_and_formats:
    new_poki_pic = PokiPic()
    new_poki_pic.image.put(open(image_path, "rb"))
    new_poki_pic.format = image_format
    new_poki_pic.save()