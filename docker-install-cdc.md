## Installing Docker

- `cat /etc/*-release shows this is Debian wheeze`
- `https://docs.docker.com/engine/installation/linux/debian/#extra-steps-for-wheezy-77`
  - `https://backports.debian.org/Instructions/`
  - `sudo nano /etc/apt/sources.list.d/docker.list`
     - Add: `deb http://ftp.debian.org/debian wheezy-backports main`
	 - Add: `deb https://download.docker.com/linux/debian wheeze stable`
- `sudo apt-get install apt-transport-https ca-certificates curl python-software-properties`
- `sudo apt-get -o Acquire::Check-Valid-Until=false update`
- `sudo apt-get install init-system-helpers`
- `sudo apt-get install -t wheezy-backports linux-image-amd64`
- `sudo apt-get install docker-ce`
- `sudo reboot`
- `sudo usermod -aG docker root`

## Building Web Image
see [docker-install.md](docker-install.md)

## DockerHub

- pull the docker hub container

`sudo docker pull benjholla/anlcdc2017-web`

- run image maps port 80 to port 8080 on host machine

`sudo docker run -p 8080:80 benjholla/anlcdc2017-web`

- quit the stdout stream to get back to cli

ctrl-c to quit stdout stream

- find the image id of the container

`sudo docker ps -a`

`sudo docker start <image name>`

- interact with the bash of the containers image id

`sudo docker exec -it 7f4a0da28c69 bash`
