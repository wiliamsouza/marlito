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

Before push a image you need to build one, see `api/README.md`
for instruction how to build a `development`image.

```
REGISTRY=172.17.8.101
TAG=development
docker tag marlito/api:$TAG $REGISTRY:5000/marlito/api:$TAG
docker push $REGISTRY:5000/marlito/api:$TAG
```

DEBUG

```
docker run --name marlito-registry --rm -p 5000:5000 \
    -e SETTINGS_FLAVOR=local -e STANDALONE=true \
    -e DISABLE_TOKEN_AUTH=true -e STORAGE_PATH=/mnt/data \
    -e SQLALCHEMY_INDEX_DATABASE=sqlite:////mnt/data/docker-registry.db \
    -v /home/wiliam/.containers/marlito/registry/volumes/data:/mnt/data \
    registry:0.7.3
```
