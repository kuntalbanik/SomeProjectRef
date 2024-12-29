# BackendDev
Backend development practice

## Ref. gitignore files
https://github.com/github/gitignore/tree/main

## Create Virtual env
virtualenv -p python3 env1  # env1 envname

Activate the env command => . env1/bin/activate

## pip commands
pip freeze >> requirements.txt

pip install -r requirements.txt



##
## autopep8 ref
Open your command palette with Shift + Ctrl + P. Type in Preferences: Open Workspace Settings. 


{
    "python.pythonPath": "${workspaceFolder}/backend/env/bin/python3",
    "python.venvPath": "${workspaceFolder}/backend/env",
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Path": "flake8",
    "python.linting.flake8Args": ["--ignore", "E501"],
    "python.linting.pylintEnabled": true,
    "python.linting.pylintPath": "pylint",
    "python.linting.pylintArgs": ["--load-plugins", "pylint_django"]
}