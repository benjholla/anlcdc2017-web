# Argonne National Labs 2017 Cyber Defense Competition Web Application
This repository contains Iowa State University's secured code for the CDC web application.

## TODOs
- ~~[fwaf](https://github.com/benjholla/fwaf) Web application firewall integration~~ (not enough time)

## Deployment
This would open port 8080 and map the port 80 in the docker image to the host machines port 8080. Do `-p 80:80` do host on port 80. The `-v` adds the volumes of the SAMBA mounts.

- `sudo docker run -v /var/www/html/IT:/var/www/html/IT -v /var/www/html/SAMBA_share:/var/www/html/SAMBA_share -p 8080:80 benjholla/anlcdc2017-web`

Docker `run` command creates a new docker image of the docker repository tagged as `benjholla/anlcdc2017-web`. Press `ctrl-c` to kill the running container. Type `docker ps -a` to list all containers including stopped containers. Type `docker start <image id of stopped image>` to start the container image. The `docker images` lists all images of containers (a single container can have multiple instances (images)). Each image will have hash id. Type `sudo docker exec -it 7f4a0da28c69 bash` replacing with the proper hash to open the shell to the docker image. Note: if you need to restart apache run `/etc/init.d/apache2 reload` instead of `service apache2 restart` the restart triggers a stop command in the docker image. To transfer files from a docker image do `docker cp foo.txt mycontainer:/foo.txt` (push), or `docker cp mycontainer:/foo.txt foo.txt` (pull).
