FROM php:8-apache-buster
RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"
RUN apt-get update
RUN apt-get install python3 -y 
RUN apt-get install python3-matplotlib -y
COPY src/ /var/www/html/
COPY src/config/php-docker.conf $APACHE_CONFDIR/conf-enabled/docker-php.conf
RUN chown -R www-data:www-data /var/www
