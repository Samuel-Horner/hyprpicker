# hyprpicker
A simple python cli to select wallpapers with hyprpaper.

### Usage
``` BASH
python hyprpicker.py [-h] [-p PREVIEW] [-q] [-d DIRECTORY]
```
### Options
- -p, --preview
The command used to preview the image. The most basic example is:
``` BASH
python hyprpicker.py --preview echo
```
Defaults to `kitten icat --use-window-size 200,200,2000,2000`. If you are using a lower resolution monitor, this will need to be adjusted.
See [here](https://sw.kovidgoyal.net/kitty/kittens/icat/) for the icat documentation.
- -q, --quit-on-set
If present, the picker will quit when you set a wallpaper.
- -d, --directory
The target directory containing wallpapers. Defaults to `~/pics/wallpapers`