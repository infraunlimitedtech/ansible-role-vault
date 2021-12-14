Vault
=========

[![Build Status](https://gitlab.infraunlimited.tech/infraOps/ansible/ansible-role-vault/badges/master/pipeline.svg)](https://gitlab.infraunlimited.tech/infraOps/ansible/ansible-role-vault/-/pipelines)
[![Ansible Role](https://img.shields.io/badge/ansible--galaxy-infraunlimitedbot.ansible__role__vault-blue)](https://galaxy.ansible.com/infraunlimitedbot/ansible_role_vault)

This role is wrapper for `ansible-community.ansible-vault` role with some tasks for initial setup. It can be used for:
* init and unseal vault after initial installation (bootstrap phase)
* enable initial user with `userpass_auth` (bootstrap phase)
* setup secrets/PKI engines
* setup file based audit device

Role Variables
--------------
Please see `defaults/main.yml` for all avaliable variables

Dependencies
------------
* ansible >= 2.9

**roles**
* ansible-community.ansible-vault

**modules**
* ansible-modules-hashivault == 4.6.3

Testing
-------
This role tested against three version Vault on centos7 node via Molecule:
* default: default version of ansible-community.ansible-vault
* vault17-full: vault 1.7.x
* vault18-full: vault 1.8.x

Example Playbook
----------------
- hosts: all
  roles:
    - infraunlimited.vault

License
-------
BSD

Author Information
------------------
Infra Unlimited