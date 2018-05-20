On Mac, replace your ~/Library/Application Support/Sublime Text 3/Packages/User folder contents with this repo to auto-install all plugins and settings. You’ll need to restart Sublime for everything to take effect.

Sublime Text 3 can be installed view Brew or downloaded from https://www.sublimetext.com/3

You’ll need to restart Sublime for it to auto-install all plugins and settings.

cd ~/Library/Application Support/Sublime Text 3/Packages/
mkdir -p User
cd User
git clone https://github.com/ZaxR/sublime_python_config.git .
*Note the period in the last line*
