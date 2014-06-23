Registry
========

It is [docker-registry](https://github.com/dotcloud/docker-registry)
used for hosting/delivering of repositories and images for containers.

It can be stared in your local development box using local storage during
development and inside your cluster using s3 for storage on production.

Getting code
------------

```
git clone https://github.com/wiliamsouza/marlito.git
```

Running locally
---------------

```
mkdir -p ~/.containers/marlito/registry/volumes/data
```

```
cd marlito/registry
fig up -d
```

[fig](http://orchardup.github.io/fig/) is used to facilitate start and stop
of the docker containers.

Pushing images
--------------

Before push an image you need to build one, see `api/README.md`
or `nginx/README.md` for instruction how to build a `development`
image and how to push it to registry.
