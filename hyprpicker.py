"""
Script to show all wallpapers (in ~/pics/wallpapers), display previews, and uses hyprpaper to set the wallpaper
To display previews terminal must be kitty
Recommended to alias python -m hyprpicker to something like wallpaper 
"""

import os
import argparse
from pathlib import Path
import kb_input
import fzf_wrapper

wallpapers = []
default_preview = "kitten icat --use-window-size 200,200,2000,2000"

def print_wallpapers(choice, preview):
    output = "\x1b[H\x1b[2J"
    for i, e in enumerate(wallpapers): output += f"{e} " if i != choice else f"\x1b[1;47m{e}\x1b[0m "
    print(output)
    print("h/a - left, l/d - right, f - fuzzy, s/j/k - set, q - quit")
    os.system(f"{preview} ~/pics/wallpapers/{wallpapers[choice]}")

def set_wallpaper(choice):
    paper = f"~/pics/wallpapers/{wallpapers[choice]}"
    print(f"Setting wallpaper to {paper}")
    os.system("hyprctl hyprpaper unload all")
    os.system(f"hyprctl hyprpaper preload \"{paper}\"")
    os.system(f"hyprctl hyprpaper wallpaper \", {paper}\"")

def fuzzy_get_wallpaper(choice, preview):
    fzf = fzf_wrapper.FzfPrompt()
    res = fzf.prompt(wallpapers) # fzf_options="--preview 'kitten icat ~/pics/wallpapers/{}'" -- TODO - make preview work
    if len(res) == 0: return choice # If <C-c> is pressed
    choice = wallpapers.index(res[0])
    print_wallpapers(choice, preview)
    return choice

def main(preview, quit_on_set):
    kb = kb_input.KBHit()
    choice = 0
    print_wallpapers(choice, preview)
    while True:
        if kb.kbhit():
            c = kb.getch()
            if c == "h" or c == "a":
                if choice != 0: choice -= 1
                print_wallpapers(choice, preview)
            elif c == "l" or c == "d":
                if choice != len(wallpapers) - 1: choice += 1
                print_wallpapers(choice, preview)
            elif c == "f":
                choice = fuzzy_get_wallpaper(choice, preview)
            elif c == "s" or c == "j" or c == "k":
                set_wallpaper(choice)
                if quit_on_set: break
            elif c == "q":
                break

    os.system("clear")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--preview", type= str, help = "Command that is run to preview the image, defaults to 'kitten icat --use-window-size 200,200,2000,2000 {file}'")
    parser.add_argument("-q", "--quit-on-set", help = "Quits the program when setting a wallpaper.", action = "store_true")
    args = parser.parse_args()

    wallpapers = os.listdir(Path.home() / "pics" / "wallpapers") # Gets wallpapers
    if len(wallpapers) == 0:
        print("No wallpapers found.")
        exit()

    print(args.quit_on_set)
    main(args.preview if args.preview else default_preview, args.quit_on_set)