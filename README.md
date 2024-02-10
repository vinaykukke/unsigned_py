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

> NOTE: This must be removed before releaseing the asset to production.

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

## Adding the integrated deadline to houdini / Manual Installation

You can also refer to the thee deadline [installation guide](https://docs.thinkboxsoftware.com/products/deadline/10.3/1_User%20Manual/manual/app-houdini.html#manual-installation).

First, copy the following files and directories to: `%localappdata%\Thinkbox\Deadline[VERSION]\submitters\HoudiniSubmitter` on Windows or `~/Library/Application Support/Thinkbox/Deadline[VERSION]/submitters/HoudiniSubmitter` on macOS or `~/Thinkbox/Deadline[VERSION]/submitters/HoudiniSubmitter` on Linux (where [VERSION] is the major version of Deadline such as 10):

```
<Repository>\submission\Houdini\Client\otls
<Repository>\submission\Houdini\Client\soho
<Repository>\submission\Houdini\Client\DeadlineHoudiniClient.py
<Repository>\submission\Houdini\Client\MainMenuCommon.xml
```

Second, update the MainMenuCommon.xml that was copied by replacing `SUBMITTER_DIR` with `%localappdata%\Thinkbox\Deadline[VERSION]\submitters\HoudiniSubmitter` on Windows, `~/Library/Application Support/Thinkbox/Deadline[VERSION]/submitters/HoudiniSubmitter` on macOS and `~/Thinkbox/Deadline[VERSION]/submitters/HoudiniSubmitter` on Linux.

Third, copy `<Repository>\submission\Houdini\Client\CallDeadlineCommand.py` to `%HOME%\Houdini{version}\python[version]libs` on Windows, `$HOME/Houdini[VERSION]/python[version]libs` on Linux, and `$HOME/Library/Preferences/houdini/[VERSION]/python[version]libs` on macOS. In my case it was:

```
$HOME/Library/Preferences/houdini/20.0/python3.10libs
```

Finally, you need to update your houdini environment. The method for this depends on which version of houdini you are using.

If you are installing the submitter for houdini 17.5 or above, you need to copy `<Repository>\submission\Houdini\client\deadline.json` to `%HOME%\Houdini{version}\packages` on Windows, `$HOME/Houdini[VERSION]/packages` on Linux, and `$HOME/Library/Preferences/houdini/[VERSION]/packages` on macOS.

If you are installing the submitter for houdini 17.0 or earlier, you need to add the following to the houdini.env file located in the Houdini [HOU VERSION] folder located in your user directory. In this file you need to add the following lines:

```
HOUDINI_PATH = "$HOUDINI_PATH;[HOU SUBMITTER DIR];&"
HOUDINI_MENU_PATH = "$HOUDINI_MENU_PATH;[HOU SUBMITTER DIR];&"
```

(where [HOU SUBMITTER DIR] is the directory you copied the files to in the first step of installation.)

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