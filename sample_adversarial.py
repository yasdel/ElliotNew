import zipfile
import io
import requests
import os

from elliot.run import run_experiment
import sys
sys.setrecursionlimit(50000)

print("Done! We are now starting the Elliot's experiment")
run_experiment("config_files/sample_adversarial.yml")
