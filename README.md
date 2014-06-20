marlito
=======

Marlito is a project developed from scratch on distribute infrastructure stack.

CoreOS
------

This repo uses Vagrant and Virtualbox to create three CoreOS virtual machine.

Dependencies:

* [Virtualbox](https://www.virtualbox.org/) 4.3.10 or greater.
* [Vagrant](http://www.vagrantup.com/) 1.6 or greater.


NFS:

It needs nfs.

Create a folder to share.

```
mkdir -p ~/.containers
```

For info on how to install and configure it on a
[fedora box](http://blog.bak1an.so/blog/2014/03/23/fedora-vagrant-nfs/)

Starting:

```
vagrant up
vagrant ssh marlito-01
vagrant ssh marlito-02
vagrant ssh marlito-03
```

Service
-------

```
fleetctl list-machines
MACHINE         IP              METADATA
b3dac926...     172.17.8.101    -
```

```
fleetctl load api.service
Job api.service loaded on b3dac926.../172.17.8.101
```

```
fleetctl list-units
UNIT            STATE   LOAD    ACTIVE          SUB     DESC           MACHINE
api.service     loaded  loaded  inactive        dead    marlito-api    b3dac926.../172.17.8.101
```

```
fleetctl start api.service
Job api.service launched on b3dac926.../172.17.8.101
```

```
fleetctl list-units
UNIT            STATE           LOAD    ACTIVE          SUB             DESC            MACHINE
api.service     launched        loaded  activating      start-pre       marlito-api     b3dac926.../172.17.8.101
```
