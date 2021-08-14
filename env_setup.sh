#! /bin/bash

# to remote ssh tunnel into the docker, use below command:
# ssh -L 8000:localhost:8888 riversome@192.168.1.196

# to fire up docker instance from within the instance:
# sudo docker run --gpus all -it -p 8888:8888 tensorflow/tensorflow:latest-gpu-jupyter /bin/bash

# install shell apps
yes | apt-get update && yes | apt-get upgrade
yes | apt-get install tmux && yes | apt-get install nano
# when inside docker, bash this script
pip install flask
pip install jupyterlab
pip install flask-restplus

# set up github
git config --global user.name "ElvinOuyang"
git config --global user.email "elvin.ouyang@gmail.com"
git config credential.helper store

# execution to fire up the env
tmux new -d -s jupyter_session 'jupyter lab --notebook-dir=/home/LearningFlask --ip 0.0.0.0 --no-browser --allow-root'
