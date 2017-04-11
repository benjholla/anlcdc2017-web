http://www.techrepublic.com/article/how-to-install-docker-on-ubuntu-16-04/

1. `sudo apt-get update`
2. `sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D`
3. `sudo nano /etc/apt/sources.list.d/docker.list`
   and add `"deb https://apt.dockerproject.org/repo ubuntu-xenial main"`
4. `sudo apt-get update`
5. `sudo apt-get install linux-image-extra-$(uname -r) linux-image-extra-virtual`
6. `sudo apt-get install docker-engine`

Note: alternate setup used for Debian OS given in CDC, see: [docker-install-cdc.md](docker-install-cdc.md)

7. `sudo usermod -aG docker $USER`

8. `mkdir ~/Desktop/drupal; cd ~/Desktop/drupal`
9. `touch Dockerfile`
10. Paste in contents in Dockerfile:
    
Dockerfile:

    FROM php:7.0-apache
	# from https://www.drupal.org/requirements/php#drupalversions
    
    
    RUN a2enmod rewrite
    
    # install the PHP extensions we need
    RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev libpq-dev \
    	&& rm -rf /var/lib/apt/lists/* \
    	&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
    	&& docker-php-ext-install gd mbstring pdo pdo_mysql pdo_pgsql zip
    
    WORKDIR /var/www/html
    
    # https://www.drupal.org/node/3060/release
    ENV DRUPAL_VERSION 7.54
    ENV DRUPAL_MD5 3068cbe488075ae166e23ea6cd29cf0f
    
    RUN curl -fSL "https://ftp.drupal.org/files/projects/drupal-${DRUPAL_VERSION}.tar.gz" -o drupal.tar.gz \
    	&& echo "${DRUPAL_MD5} *drupal.tar.gz" | md5sum -c - \
    	&& tar -xz --strip-components=1 -f drupal.tar.gz \
    	&& rm drupal.tar.gz \
    	&& chown -R www-data:www-data sites

11. `sudo docker build -t drupal .`
12. `sudo docker run -p 80:80 drupal`
13. Configure Drupal by visiting `http://localhost`
    - install with SQLite
    - install mysql just to do the porting...
    - `apt-get install mysql-server`, `service mysql restart`, `mysql -u root -ppassword, create database drupal;`, `mysql -u username -p drupal < drupal.db`, add mysql db entry to `sites/default/settings.php` from anlcdc settings version
    - install `https://www.drupal.org/project/dbtng_migrator` -> `https://ftp.drupal.org/files/projects/dbtng_migrator-7.x-1.4.tar.gz`, enable module

## Commands

- https://github.com/dumblob/mysql2sqlite
mysqldump -u root -ppassword drupal > drupal.sql

- https://www.drupal.org/docs/7/backing-up-and-migrating-a-site/migrating-a-site
``sed -E -e "/^INSERT INTO \`(cache|watchdog|sessions)/d" < drupal.sql > drupal-stripped.sql``

- `./mysql2sqlite drupal-stripped.sql | sqlite3 drupalsqlite3.db`

- swap out sqlite files...need to change group and owner though...

- `sudo docker commit <running image id>`
- `sudo docker images <look for id of untagged image>`
- `sudo docker tag <untagged image id> benjholla/anlcdc2017-web:latest`
- `sudo docker commit benjholla/anlcdc2017-web:latest`
- `sudo docker login`
- `sudo docker push benjholla/anlcdc2017-web`

- `sudo docker run -v /var/www/html/IT:/var/www/html/IT -v /var/www/html/SAMBA_share:/var/www/html/SAMBA_share -p 8080:80 benjholla/anlcdc2017-web`

- `sudo docker run -v /host/directory:/container/directory`
- `sudo docker run -p 8080:80 benjholla/anlcdc2017-web`
