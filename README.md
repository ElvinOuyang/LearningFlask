# LearningFlask
 repository for learning to build flask api

## Quick Start on Setup

### If the GPU / Docker is hosted in a remote server, use below command to SSH into the server:

**Local Server**:
```bash
ssh -L 127.0.0.1:8000:localhost:8888 username@000.000.000.000 # local server IP address
```
**Remote Server**:
```bash
ssh -R 127.0.0.1:8000:localhost:8888 username@id.server.com # remote server public url
```

### Once inside the server running docker, locate to the folder you wish to mount to container

### Run below code to fire up a jupyter scipy notebook container:
```bash
# from linux / mac
docker run -it --user root -p 8888:8888 -p 6006:6006 -p 8000:8000 -v "$PWD":/home jupyter/tensorflow-notebook:python-3.8.8 /bin/bash
# from windows powershell
docker run -it --user root -p 8888:8888 -p 6006:6006 -p 8000:8000 -v ${pwd}:/home jupyter/tensorflow-notebook:python-3.8.8 /bin/bash
```
Once the container is set up, you will now access the bash terminal of the docker container

### Pull this repository into the docker container:
`git` has already been installed in the container. Run below command from within the container terminal:

```bash
git clone https://github.com/ElvinOuyang/LearningFlask.git
```
After you've entered your credentials, the repo should be available at `/home/` folder.

### Set up the environment for running the package:

Follow below command to relocate to the repository:

```bash
cd /home/LearningFlask
```

Then run below bash script to finish the env set up:

```bash
source ./env_setup.sh
```

At the end of the script, a jupyter lab server will be up and running. Since the SSH port tunneling has been established, you should be able to access the server from your local browser at `localhost:8888`.
