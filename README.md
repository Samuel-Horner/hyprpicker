# hyprpicker
A simple python cli to select wallpapers with hyprpaper.

### Usage
``` BASH
python hyprpicker.py [BACKEND]... [OPTIONS]...
```
### Backend
The wallpaper backend to pass the image to. Current options are:
    - `swww`
    - `hyprpaper`
### Options
- -p, --preview
The command used to preview the image. The most basic example is:
``` BASH
python hyprpicker.py --preview echo
```
Defaults to `kitten icat --use-window-size WINDOW_DIMENSIONS*0.75`.
See [here](https://sw.kovidgoyal.net/kitty/kittens/icat/) for the icat documentation.
- -q, --quit-on-set
If present, the picker will quit when you set a wallpaper.
- -d, --directory
The target directory containing wallpapers. Defaults to `~/pics/wallpapers`
