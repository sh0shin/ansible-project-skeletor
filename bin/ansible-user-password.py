#!/usr/bin/env python
# vim: set ft=python :

from passlib.hash import sha512_crypt
from passlib.hash import bcrypt
import getpass

password = getpass.getpass()

print('sha512_crypt: ' + sha512_crypt.using(rounds=5000).hash(password))
print('bcrypt_blowfish: ' + bcrypt.using(rounds=8).hash(password))
