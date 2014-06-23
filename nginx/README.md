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
$ docker build -t marlito/nginx:development .
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

Pushing images
--------------

Before push an image you need start a local registry `registry/README.md`
for instruction how to start a registry.

```
REGISTRY=<LOCAL_IP>
TAG=development
docker tag marlito/nginx:$TAG $REGISTRY:5000/marlito/nginx:$TAG
docker push $REGISTRY:5000/marlito/nginx:$TAG
```
