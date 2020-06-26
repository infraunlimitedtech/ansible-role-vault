Vault
=========

Requirements
------------

Vault after deploy needed to be initialized.
```
VAULT_ADDR=http://127.0.0.1:8200 ansible-playbook ./misc/vault/init/bootstrap.yml -e 'vault_admin_password=password'
```
VAULT_ADDR=http://127.0.0.1:8200 vault login -method=userpass username=spigell
VAULT_ADDR=http://127.0.0.1:8200 vault write auth/userpass/users/spigell password=adsfasfffawfaf


ansible-playbook ./misc/vault/pki/create-int-ca.yml -e 'ca=openvpn'

ansible-playbook ./misc/vault/openvpn/openvpn-secret.yml


Role Variables
--------------

Much hardcoded

Dependencies
------------

roles

brianshumate.vault

modules

ansible-modules-hashivault


Example Playbook
----------------

- hosts: all
  roles:
    - { role: infraunlimited.vault, tags: vault }

License
-------

BSD

Author Information
------------------

Infra Unlimited