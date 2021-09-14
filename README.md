---
title: Flac Metadata Extractor
category: Random
language: python
author: Anis Sarker
---

# Flac metadata extractor

This program is use to extract metadata of a flac file.

* Load an audio flac file
* Read the metadata
* Extract album-art from the flac file
* Save the metadata in json format. Json file can be use as audio file dataset for media app.

## Prerequisite
* Python
* Install audio_metadata

    `$ pip install -U audio-metadata`

## Run

`$ python music.py --audio '/path/to/files' --output '/path/to/output' --file some_name`


## Usage

```
music.py [-h] [-a AUDIO] [-o OUTPUT] [-f FILE]

Flac audio metadata extractor

optional arguments:
  -h, --help            show this help message and exit
  -a AUDIO, --audio AUDIO
                        Path of flac file
  -o OUTPUT, --output OUTPUT
                        Output directory
  -f FILE, --file FILE  JSON output name
```