import os
import glob
import argparse
import audio_metadata
import json

def extractor(audio, output, file):
    album_art_dir = '{}/album-art'.format(output)
    music_info = []
    id = 0

    if os.path.exists(album_art_dir):
        pass
    else:
        os.makedirs(album_art_dir)
    for music in glob.glob("{}/*.flac".format(audio)):
        tmp_music = { "id": "", "title": "", "album": "", "artist": "", "genre": "", "date": "", "filepath": "", "filesize": "", "albumart": ""}
        file_ = os.path.join(audio, music)
        meta_data = audio_metadata.load(file_)
        img = meta_data["pictures"]
        for pic in img:
            if pic.type == 3:
                album_art_path = os.path.join(album_art_dir, f"{str(id)}.jpg")
                with open(album_art_path, 'wb') as f:
                    f.write(pic.data)

        tmp_music["id"] = str(id)
        tmp_music["title"] = meta_data["tags"]["title"][0] if meta_data["tags"].get("title") else "Track {}".format(id)
        tmp_music["album"] = meta_data["tags"]["album"][0] if meta_data["tags"].get("album") else "Unknown"
        tmp_music["artist"] = meta_data["tags"]["artist"][0] if meta_data["tags"].get("artist") else "Unknown"
        tmp_music["genre"] = meta_data["tags"]["genre"][0] if meta_data["tags"].get("genre") else "Unknown"
        tmp_music["date"] = meta_data["tags"]["date"][0] if meta_data["tags"].get("date") else "Unknown"
        tmp_music["filepath"] = meta_data["filepath"] if meta_data.get("filepath") else "Unknown"
        tmp_music["filesize"] = meta_data["filesize"] if meta_data.get("filesize") else "Unknown"
        try: 
            tmp_music["albumart"] = album_art_path
        except KeyError:
            tmp_music["albumart"] = "Unknown"

        music_info.append(tmp_music)
        id += 1

    print(music_info)
    with open(f'{output}/{file}.json', "w") as outFile:
        json.dump(music_info, outFile)
        print("file saved as {}.json...".format(file))
        outFile.close()

def main():
    parser = argparse.ArgumentParser(description="Flac audio metadata extractor")
    parser.add_argument('-a', '--audio', type=str, help="Path of flac file")
    parser.add_argument('-o', '--output', type=str, help="Output directory")
    parser.add_argument('-f', '--file', type=str, help="JSON output name")
    args = parser.parse_args()
    
    extractor(args.audio, args.output, args.file)

if __name__ == "__main__":
    main()