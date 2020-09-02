#!/usr/bin/env python3
import sys
import os
import subprocess

try:
    from dotenv import load_dotenv
except:
    print("dotenv not installed, installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-dotenv"])
    from dotenv import load_dotenv

try:
    import matplotlib
except:
    print("matplotlib not installed, installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])

try:
    import celluloid
except:
    print("celluloid not installed, installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "celluloid"])

try:
    import flask
except:
    print("flask not installed, installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])

if "FLASK_APP" not in os.environ:
    load_dotenv(dotenv_path="setapp.env",override=True)

subprocess.check_call(["flask","run"])
