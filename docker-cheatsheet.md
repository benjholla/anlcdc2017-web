# Outside Docker

- `docker run <image>`
- `docker start <name|id>`
- `docker stop <name|id>`
- `docker ps [-a includes stopped containers]`
- `docker rm <container>`
- `docker images`
- `docker build -t my-docker-whale .`
- `docker run -it drupal-lite /bin/bash`
- `sudo docker exec -it d4854b0dbfa2 bash`
- `docker cp foo.txt mycontainer:/foo.txt` (push file)
- `docker cp mycontainer:/foo.txt foo.txt` (pull file)

# Within Docker

- `apt-get update`
- `apt-get install vim nano`

Note: restart apache without killing container (Dockerfile linked service to Docker container lifecycle)

- `/etc/init.d/apache2 reload` and NOT `service apache2 restart`

