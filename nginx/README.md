marlito-nginx
=============

Dockerfile
----------

Docker nginx server generic image source. This is based on `ubuntu:12.04` image.

Image
-----

Build this repository:

```
$ git clone https://github.com/wiliamsouza/marlito.git
$ cd marlito/nginx/
$ docker build -t marlito/nginx .
```

Container
---------

This image uses volumes and environment variables to control the nginx server
configuration.

Volumes:

* `/etc/nginx/site-available`: Change sites configurations using it.
* `/usr/share/nginx/html`: HTML files goes here.
* `/etc/nginx/conf.d`: Change sites configurations using it.
* `/var/log/nginx`: Access log from the container using it.
* `/srv`: Add your app source code here.

You pass with `-v` docker option. Don't forget to use absolute path here.
