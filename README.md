Vault
=========
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