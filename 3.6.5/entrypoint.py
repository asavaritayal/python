import subprocess
import os

# Temporary patch. Won't be required once antenv is built in the kudu image.
os.environ["PYTHONPATH"] = "/home/site/wwwroot/antenv/lib/python3.6/site-packages"

def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print (proc_stdout.decode("utf-8"))

subprocess_cmd('python --version; pip --version;'
                'GUNICORN_CMD_ARGS="--bind=0.0.0.0" gunicorn application:app'
               )