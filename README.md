This repo contains Sublime Text 3 customization, specifically focused on the Python programming language.

## Installation Instructions
1. Installed Sublime Text 3 via Brew or downloaded from https://www.sublimetext.com/3
2. Navigate to Tools > "Command Pallette..." (on Mac, type command+shift+p)
3. Type Install Package Control and select to install.
4. Replace your Sublime Text 3 user packages settings with this repo. On Mac, type the following in your terminal:

    cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages 
    mkdir -p User  
    cd User  
    git clone https://github.com/ZaxR/sublime_python_config.git .  # Note the period

5. Restart Sublime and wait for the packages.settings to be auto-installed (will cause several pop-ups if it's working).
