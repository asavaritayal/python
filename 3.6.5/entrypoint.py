import subprocess
import os

HOME_SITE="/home/site/wwwroot"

# Temporary patch. Won't be required once antenv is built in the kudu image.
os.environ["PYTHONPATH"] = "/home/site/wwwroot/antenv/lib/python3.6/site-packages"

def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print (proc_stdout.decode("utf-8"))

## Check for custom gunicorn config
def custom_check():
    return None

## Django check
# If manage.py is present in the current or a subdirectory, find wsgi object and identify as Django. 
def check_django():
    return None

## Flask check
# If application.py is provided or only a single module is present, identify as Flask.
def check_flask():
    if os.path.exists(HOME_SITE + "/application.py"):
        return 'application'
    else:
        return None

app_module = check_flask()

subprocess_cmd('python --version; pip --version;'
                'GUNICORN_CMD_ARGS="--bind=0.0.0.0" gunicorn ' + app_module + ':app'
               )