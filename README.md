marlito
=======

Marlito is a project developed from scratch on distribute infrastructure stack.

Dependencies
------------

This repo uses Vagrant and Virtualbox to create three CoreOS virtual machine.

* [Virtualbox](https://www.virtualbox.org/) 4.3.10 or greater.
* [Vagrant](http://www.vagrantup.com/) 1.6 or greater.

Configuring
-----------

Copy `user-data.sample` to `data-sample`.

```
cp user-data.sample data-sample
```

Generate a new `etcd` token [here](https://discovery.etcd.io/new) and
change `discovery:` option in `data-sample`.

Change `DOCKER_REGISTRY` in `user-data` to point to your
local running `docker-registry` usualy it will be local ip address.

Add your ssh public key in `user-data` changing `path` and `content` as
the example.

```
  - path: /home/core/.ssh/authorized_keys.d/<USERNAME-HERE>
    permissions: 0600
    owner: core
    content: |
      <SSH-RSA-KEY-HERE>

```
Copy `config.rb.sample` to `config.rb`

```
cp config.rb.sample config.rb
```

ssh
---

Add the following to `~/.ssh/config`:

```
Host coreos
  User     core
  HostName 172.17.8.101
  IdentityFile ~/.ssh/id_rsa.pub
```

Add your key:

```
ssh-add ~/.ssh/id_rsa
```

Check if it is correctly loaded:

```
ssh-add -l
```

Starting the cluster
--------------------

It will start three nodes.

```
vagrant up
```

To get in a node use.

```
vagrant ssh marlito-01
vagrant ssh marlito-02
vagrant ssh marlito-03
```

Starting registry
-----------------

You will need a local `docker-registry`.

```
cd registry
fig up -d
```

fleet
-----

Configuring `fleet`.

```
export FLEETCTL_TUNNEL=172.16.8.101
```

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

Reloading user-data
-------------------

Inside a machine run:

```
sudo coreos-cloudinit --from-file /var/lib/coreos-vagrant/vagrantfile-user-data
```
