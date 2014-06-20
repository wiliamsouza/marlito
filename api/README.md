marlito-api
===========

API server

Dockerfile
-----------

Docker api server image source. This is based on `ubuntu:12.04` image.

Image
-----

You can `pull` a ready to use image from Docker
[index](https://index.docker/u/wiliamsouza/) running:

```
$ docker pull wiliamsouza/marlito-api
```

Or build this repository:

```
$ git clone https://github.com/wiliamsouza/marlito.git
$ cd api/
$ docker build -t marlito/api:development .
```
For instructions to upload this `development` image for private registry
look in `registry/README.md`.

Container
---------

This image uses environment variables to control the api server configuration.

Environment variable:

* `HOST`: Set to `${COREOS_PRIVATE_IPV4}` by `systemd` service unit and is the
          ip address of `etcd` on `coreos` box.

You pass with `-e` docker option.

Shell access:

```
$ docker run --rm -p 8000:8000 -i \
-t marlito-api /bin/bash
```

The command above will start a container give you a shell. Don't
forget to start the service running the `startup &` script.

Usage:

```
$ docker run --name api -p 8000:8000 -d marlito-api
```

The command above will start a container and return its ID.
