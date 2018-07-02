import subprocess
import glob
import os

HOME_SITE="/home/site/wwwroot"

# Temp patch. Remove when Kudu script is available.
os.environ["PYTHONPATH"] = HOME_SITE + "/antenv/lib/python3.6/site-packages"

def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print (proc_stdout.decode("utf-8"))

## Check for custom startup command
def custom_check():
    return None

## Django check: If 'wsgi.py' is provided, identify as Django. 
def check_django():
    wsgi_modules = glob.glob(HOME_SITE+'/**/wsgi.py', recursive=True)
    if len(wsgi_modules)==0:
        return None
    else:
        return wsgi_modules[0][1:-3].replace('/','.')
    return None

## Flask check: If 'application.py' is provided or a .py module is present, identify as Flask.
def check_flask():
    
    py_modules = glob.glob(HOME_SITE+'/*.py')
    if len(py_modules) == 0:
        return None
    for module in py_modules: 
        if module[-14:] == 'application.py':
            return 'application:app'

    return py_modules[0][len(HOME_SITE)+1:-3].replace('/','.')+':app'

def start_server():
    
    cmd = custom_check()
    if cmd is not None: 
        subprocess_cmd(
                'GUNICORN_CMD_ARGS="--bind=0.0.0.0" ' + cmd
               )
        return

    cmd = check_django()
    if cmd is not None:
        subprocess_cmd(
                'GUNICORN_CMD_ARGS="--bind=0.0.0.0" gunicorn ' + cmd
               )

    cmd = check_flask()
    if cmd is not None:
        subprocess_cmd(
                'GUNICORN_CMD_ARGS="--bind=0.0.0.0" gunicorn ' + cmd
               )

subprocess_cmd('python --version; pip --version;'
                'source antev/bin/activate'
               )
start_server()