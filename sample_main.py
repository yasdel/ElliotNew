


import zipfile
import io
import requests
import os

from elliot.run import run_experiment

print("Done! We are now starting the Elliot's experiment")
run_experiment("config_files/sample_hello_world_new.yml")




#from elliot.run import run_experiment
#import argparse

#parser = argparse.ArgumentParser(description="Run sample main.")
#parser.add_argument('--type_experiment', type=str, default='baselines')
#parser.add_argument('--dataset', type=str, default='amazon_baby')
#args = parser.parse_args()

#run_experiment("config_files/{0}_{1}.yml".format(args.type_experiment, args.dataset))