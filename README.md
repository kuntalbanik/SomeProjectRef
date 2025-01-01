# BackendDev
Backend development practice

## Ref. gitignore files
https://github.com/github/gitignore/tree/main

## Create Virtual env
python -m venv /env  # env1 envname

Activate the env command => . env/Scripts/activate

#### virtualenv note
Note : Don't create the source code is inside the virtual environment, that is, in the same directory that holds bin/, lib/, and pyvenv.cfg

use this project like folder structure


## pip commands
pip freeze >> requirements.txt

pip install -r requirements.txt


## Python formatter for vscode
Black Formatter
## black formatter settings
<!-- "pip install black"  on your activated virtualenv -->
<!-- settings for windows. change it for linux as required  -->
<!-- Press <ctrl> + <shift> + p  -> Preferences: Open workspace settings (JSON) -> paste the below settings in to it -> change the virtualenv path and .exe accordingly -->

{
    "black-formatter.importStrategy": "fromEnvironment",
    "black-formatter.interpreter": ["${workspaceFolder}\\env\\Scripts\\python.exe"],
    "black-formatter.path": ["${workspaceFolder}\\env\\Scripts\\black.exe"],
    "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true,
    "editor.rulers": [
        88,
        120
      ]
  }
}
