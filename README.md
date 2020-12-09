---
title: Flac Metadata Extractor
category: Random
language: python
author: Anis Sarker
---

# Flac metadata extractor

This program is to extract metadata of a flac audio file.

* Load an audio flac file
* Read the metadata
* Extract album-art from the flac file
* Save the metadata in json format. Json file can be use as audio file dataset for media app.

## Prerequisite
* Python
* Install audio_metadata

    `$ pip install -U audio-metadata`

## Usage
Copy the code and save as any name such as music.py

Create a directory inside project folder and name it *dist* to keep the flac files.

**Run**

`$ python music.py`

**Output**

album-arts will be saved in directiry `dist/album-art`.

a `music.json` will be saved inside `dist` diretory.

### **Code**

```python
import os
import audio_metadata
import json


music_dir = 'dist/music'
album_art_dir = 'dist/album-art'
music_info = []
id = 0

if os.path.exists(album_art_dir):
    print("+---------------------------------------------------+")
    print("| dist/album-art directory already exists. skipping |")
    print("+---------------------------------------------------+")
    pass
else:
    os.makedirs(album_art_dir)
    print("+---------------------------------------------------+")
    print("| dist/album-art directory created...               |")
    print("+---------------------------------------------------+")

for music in os.listdir(music_dir):
    print(f"current image\nid: {id}\nfilename: {music}\n{len(music)*'-'}----------\n")

    file_ = os.path.join(music_dir, music)
    meta_data = audio_metadata.load(file_)

    img = meta_data["pictures"]
    for pic in img:
        if pic.type == 3:
            album_art_path = os.path.join(album_art_dir, f"{str(id)}.jpg")
            with open(album_art_path, 'wb') as f:
                f.write(pic.data)

    music_info.append(
        {
            "id": str(id),
            "title": meta_data["tags"]["title"][0],
            "album": meta_data["tags"]["album"][0],
            "artist": meta_data["tags"]["artist"][0],
            "genre": meta_data["tags"]["genre"][0],
            "date": meta_data["tags"]["date"][0],
            "duration": meta_data["tags"]["album"][0],
            "filepath": meta_data["filepath"],
            "filesize": meta_data["filesize"],
            "albumart": album_art_path
        }
    )
    id += 1

with open('dist/music.json', "w") as outFile:
    json.dump(music_info, outFile)
    print("file saved as json...\n")
    outFile.close()
```
