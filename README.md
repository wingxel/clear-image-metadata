# Clear Image EXIF Information
***
Python script to remove EXIF information form any given image.
***
```shell
python3 clean.py -i /home/usr/folder/img1.png \
  /home/user/folder/img2.jpg /home/user/folder_with_images \
  -d /home/user/Pictures/cleaned --remove --preserve
```
***
## Commandline Options

- **<font size="4">-i</font>** or **<font size="4">--image</font>** : Source image file list.
- **<font size="4">-d</font>** or **<font size="4">--destination</font>** : Folder to save cleaned files.
- **<font size="4">-r</font>** or **<font size="4">--remove</font>** : Delete the source/original file.
- **<font size="4">-p</font>** or **<font size="4">--preserve</font>** : Use the original filenames.

***