"""
Script to show all wallpapers, display previews, and uses hyprpaper to set the wallpaper
To display previews terminal must be kitty or set other previewer
Recommended to alias python path/to/hyprpicker.py to something like wallpaper 
"""

import os
import argparse
import kb_input
import fzf_wrapper

wallpapers = []
# Defaults
preview = "kitten icat --use-window-size 200,200,2000,2000"
dir = "~/pics/wallpapers"

def print_wallpapers(choice):
    output = "\x1b[H\x1b[2J"
    for i, e in enumerate(wallpapers): output += f"{e} " if i != choice else f"\x1b[1;47m{e}\x1b[0m "
    print(output)
    print("h/a - left, l/d - right, f - fuzzy, s/enter - set, q - quit")
    os.system(f"{preview} {dir}/{wallpapers[choice]}")

def set_wallpaper(choice):
    paper = f"{dir}/{wallpapers[choice]}"
    print(f"Setting wallpaper to {paper}")
    os.system("hyprctl hyprpaper unload all")
    os.system(f"hyprctl hyprpaper preload \"{paper}\"")
    os.system(f"hyprctl hyprpaper wallpaper \", {paper}\"")

def fuzzy_get_wallpaper(choice):
    fzf = fzf_wrapper.FzfPrompt()
    res = fzf.prompt(wallpapers) # fzf_options="--preview 'kitten icat dir/{}'" -- TODO - make preview work
    if len(res) == 0: return choice # If <C-c> is pressed
    choice = wallpapers.index(res[0])
    return choice

def main(quit_on_set):
    kb = kb_input.KBHit()
    choice = 0
    print_wallpapers(choice)
    while True:
        if kb.kbhit():
            c = kb.getch()
            if c == "h" or c == "a":
                if choice != 0: choice -= 1
                print_wallpapers(choice)
            elif c == "l" or c == "d":
                if choice != len(wallpapers) - 1: choice += 1
                print_wallpapers(choice)
            elif c == "f":
                choice = fuzzy_get_wallpaper(choice)
                print_wallpapers(choice)
            elif c == "s" or c == "\n":
                set_wallpaper(choice)
                if quit_on_set: break
            elif c == "q":
                break

    os.system("clear")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--preview", type= str, help = f"Command that is run to preview the image, defaults to '{preview} $FILE'")
    parser.add_argument("-q", "--quit-on-set", help = "Quits the program when setting a wallpaper.", action = "store_true")
    parser.add_argument("-d", "--directory", type = str, help = f"The directory that wallpapers are located in. Defaults to {dir}.")
    args = parser.parse_args()

    if args.directory: dir = args.directory
    if args.preview: preview = args.preview 

    wallpapers = os.listdir(os.path.expanduser(dir)) # Gets wallpapers
    if len(wallpapers) == 0:
        print("No wallpapers found.")
        exit()

    main(args.quit_on_set)