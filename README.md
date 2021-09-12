[//]: # ( vim: set ft=markdown : )

# Ansible project skeletor

Template hierarchy for Ansible projects

## Install Ansible & Python requirements

```sh
pip install -U -r requirements-VERSION.txt
```

## Install Ansible roles

```sh
ansible-galaxy role install -r requirements.yml
```

## Install Ansible collections

```sh
ansible-galaxy collection install -r requirements.yml
```

## Setup your inventory

See: [ansible-inventory-skeletor](https://github.com/sh0shin/ansible-inventory-skeletor) for an example inventory.

```sh
git clone https://github.com/sh0shin/ansible-inventory-skeletor.git inventories/skeletor
```
