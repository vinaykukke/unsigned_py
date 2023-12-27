# Setting up houdini with VS Code

Follow [artice](https://jurajtomori.wordpress.com/2018/02/20/houdini-tip-using-hou-module-in-visual-studio-code/) for more info.
See [Video](https://www.youtube.com/watch?v=HldzZ5ikZhc&ab_channel=CGchameleon)

- First install the latest version of houdini
- Download the [Houdini Expression Editor](http://cgtoolbox.com/houdini-expression-editor/)
- Extract and move to the houdini lib folder on your system, mine is at `~/Library/Preferences/houdini/19.5`.
- Open the `houdini.env` and add the following:
  ```
  HOUDINI_MMB_PAN = 0 ## This allows you to PAN the scene without a center mouse button on a MAC
  HOUDINI_PATH = "/Users/vinaykukke/Library/Preferences/houdini/19.5/HoudiniExt;&" ## This is the path of the Expression editior you just moved in the previous step
  ```
- Open the python shell in houdini and type the following:
  ```
  // This will display the location of the houdini module
  hou.__file__
  ```
- Copy the location of the houdini module and place it in the Work space Settings by creating a `.vscode` folder and placing a `settings.json` file, with that add as follows:
  ```
  "python.autoComplete.extraPaths": [
    "/Applications/Houdini/Houdini19.5.716/Frameworks/Houdini.framework/Versions/19.5/Resources/houdini/python3.9libs/hou.py"
  ],
  "python.analysis.extraPaths": [
    "/Applications/Houdini/Houdini19.5.716/Frameworks/Houdini.framework/Versions/19.5/Resources/houdini/python3.9libs/hou.py"
  ],
  "python.autoComplete.preloadModules": ["hou"] // This is invalid but just place it anyways, there will be no errors
  ```
- Once that is done locate the `hython` executable and set its path as the interpreter for python in vs-code (CMD+SHIFT+P && Python: Select Interpreter) and the enter the path for my system it is in `/Applications/Houdini/Houdini19.5.716/Frameworks/Houdini.framework/Versions/19.5/Resources/bin/hython`. This will give you autocomplete in vs-code for houdini

# Installing third party libraries with houdini

If there are any problems please refer the official houdini [documentation](https://www.sidefx.com/docs/houdini/hom/locations.html#disk)

- Check the version of python installed in houdini and in the system - they both have to match
- All the external packaged installed will have to be installed for the version of python you find above
- Move to the houdini lib folder on your system, mine is at `~/Library/Preferences/houdini/19.5`.
- Open the `houdini.env` and add the following:
```
PYTHONPATH = "/usr/local/lib/python3.11/site-packages" ## If you want to install external modules such as numpy
HOUDINI_MMB_PAN = 0
HOUDINI_PATH = "/Users/vinaykukke/Library/Preferences/houdini/19.5/HoudiniExt;&"
PYTHONPATH = "/Users/vinaykukke/Documents/Work/unsigned_py/tools"
HOUDINI_TOOLBAR_PATH = "/Users/vinaykukke/Documents/Work/unsigned_py/tools/houdini/settings/toolbar;&"
HOUDINI_VEX_PATH = "/Users/vinaykukke/Documents/Work/unsigned_py/tools/houdini/vex;&"
HOUDINI_LMINFO_VERBOSE = 0
JOB = "/Users/vinaykukke/Documents/Work/unsigned_projects"
```
- Open houdini
- You can cross check that your module has been added in houdini by doing the following in the python shell:

```python
import sys
print(sys.path) ## This should include the path to your module
```
- Once you have linked to your module you can then create a `__init__.py` file in the module location

# Instant Update for Script / HMR

To get this feature, its as simply as adding a small script in the tool
```python
import importlib
import unsigned_py as upy

# Reload the unsigned_py module to get the latest changes
importlib.reload(upy);
upy.create_new_tool()
```
# List all houdini paths
A short cut to list all the paths houdini uses to store and look up things. You can use this in the houdini python shell
```python
import hou

hou.houdiniPaths()
```

# Making a wrapper for houdini

For windows run this script to run houdini with a custom wrapper. `NOTE: Please make sure to change the paths`

```batch
set PYTHONPATH=%cd%\tools
set EVE_ROOT=%cd%

"C:\Users\kko8\AppData\Local\Programs\Python\Python310\python.exe" %cd%\tools\pm\project_manager.py
```

For MacOS we need to do the same with a shell script called `project_manager.sh`

```bash
# First give the script permission to execute
chmod +x project_manager.sh
```

# Unsinged CLI - MacOS
To use the CLI in a linux env, you should add the following to the `.zshrc / .bashrc` - so that the required `unsigned.sh` file is loaded for every terminal session

```bash
source /Users/vinaykukke/Documents/Work/unsigned_py/unsigned.sh
```

Then you can use it in the cli as follows:
> NOTE: This will create all the required folders in the parent dir of `unsigned_py`

```bash
unsigned init # This will create all the required folders in the parent dir of unsigned_py
```

# Unsinged CLI - Windows
To use in windows environment you can do the following:

```batch
cd unsigned_py
:: This will create all the required folders in the parent dir of unsigned_py 
unsigned.bat init
```

# Installing 3rd party packages into houdini
Navigate to `/Users/vinaykukke/Library/Preferences/houdini/19.5/` and look for the `packages` folder - if it doesn't exist the create one. Move all you folders to this directory and restart houdini.
> This is where houdini will look for 3rd party packages you have installed 

# Incase of License Issues OR License Server issues
You can start or stop the license server by using these commands

```bash
# To stop the license server: 
sudo launchctl unload /Library/LaunchDaemons/com.sidefx.sesinetd.plist
# To start the license server: 
sudo launchctl load -w /Library/LaunchDaemons/com.sidefx.sesinetd.plist
```

# Adding a nonexistant version of houdini into Thinkbox Deadline Monitor

## Adding the houdini version to the plugins tab in  deadline
Go here find the `Houdini.param` file

```bash
cd /Applications/Thinkbox/DeadlineRepository10/plugins/Houdini/
```

and the path to the `hython` executable and then add the path to the `simtracker.py` which in my case is `/Applications/Houdini/Houdini20.0.547/Frameworks/Houdini.framework/Versions/20.0/Resources/houdini/python3.10libs/simtracker.py`. It should look something like this:

```
[Houdini20_0_Hython_Executable]
Label=Houdini 20.0 Hython Executable
Category=Render Executables
CategoryOrder=0
Type=multilinemultifilename
Index=15
Default=/Applications/Houdini/Houdini20.0.547/Frameworks/Houdini.framework/Versions/20.0/Resources/bin/hython
Description=The path to the hython executable. It can be found in the Houdini bin folder.

[Houdini20_0_SimTracker]
Label=Houdini 20.0 Sim Tracker File
Category=HQueue Simulation Job Options
CategoryOrder=1
Type=multilinemultifilename
Index=11
Default= /Applications/Houdini/Houdini20.0.547/Frameworks/Houdini.framework/Versions/20.0/Resources/houdini/python3.10libs/simtracker.py
Description=The path to the simtracker.py file that is used when distributing HQueue sim jobs. This file can be found in the Houdini install.
```

First enter the `power user mode` by clicking `tools/power user mode` Now you should be able to find your `Houdini 20.0` in the `tools/configure plugin/houdini` section

## Adding the integrated deadline to houdini
In order to add the `submit to deadline` item in the render tab, the fooling needs to be done:

- Goto: `/Applications/Thinkbox/DeadlineRepository10/submission/Houdini/Installers` and install the submitter for the supported version of houdini
- Goto: `/Users/vinaykukke/Library/Preferences/houdini/19.5/packages` and copy the `deadline.json` file to the version of houdini you wish to be using it in. This will give you the integrated deadline menu item.