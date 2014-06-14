#!/usr/bin/env python
import os
import sys,subprocess

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notes.settings")
    #subprocess.call(["source", "/home/suhail/Envs/noteenv/bin/activate"])
    activate_env="/home/suhail/Envs/noteenv/bin/activate_this.py"
    #if not 'OPENSHIFT_DATA_DIR' in os.environ:execfile(activate_env, dict(__file__=activate_env))
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
