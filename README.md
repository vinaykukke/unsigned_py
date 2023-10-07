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
- Copy the location of the houdini module and place it in the user settings / Work space Settings (CMD+SHIFT+P && User settings (JSON)) `settings.json` file in vs code, as follows:
  ```
  "python.autoComplete.extraPaths": [
    "/Users/vinaykukke/Applications/Houdini/Houdini19.5.716/Frameworks/Houdini.framework/Versions/19.5/Resources/houdini/python3.9libs/hou.py"
  ],
  "python.analysis.extraPaths": [
    "/Users/vinaykukke/Applications/Houdini/Houdini19.5.716/Frameworks/Houdini.framework/Versions/19.5/Resources/houdini/python3.9libs/hou.py"
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
PYTHONPATH = "/users/vinaykukke/documents/work/unsigned_py" ## If you want to install your own custom modules for houdini
## If you want to install custom modules as well as packages in python at the same time
PYTHONPATH = "/users/vinaykukke/documents/work/unsigned_py:/users/vinaykukke/documents/work/unsigned_py/site-packages"
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