import json
import logging

from passlib.hash import bcrypt

from dataclay_common.exceptions.exceptions import *

logger = logging.getLogger(__name__)


# TODO: Extend class to generic with key(), value(), ...
class Account:
    def __init__(
        self, username, password=None, role="NORMAL", namespaces=[], datasets=[], **kwargs
    ):
        # TODO: Remove namespaces from account?
        self.username = username
        if password is not None:
            self.hashed_password = bcrypt.hash(password)
        self.role = role
        self.namespaces = namespaces
        self.datasets = datasets
        self.__dict__.update(kwargs)

    @classmethod
    def from_json(cls, s):
        return cls(**json.loads(s))

    def verify(self, password, role=None):
        if not bcrypt.verify(password, self.hashed_password):
            return False
        if role is not None and self.role != role:
            return False
        return True

    def key(self):
        return f"/account/{self.username}"

    def value(self):
        return json.dumps(self.__dict__)


class AccountManager:

    lock = "lock_account"

    def __init__(self, etcd_client):
        self.etcd_client = etcd_client

    def put_account(self, account):
        self.etcd_client.put(account.key(), account.value())

    def get_account(self, username):
        # Get account from etcd and checks that it exists
        key = f"/account/{username}"
        value = self.etcd_client.get(key)[0]
        if value is None:
            raise AccountDoesNotExistError(username)

        return Account.from_json(value)

    def exists_account(self, username):
        """ "Returns ture if the account exists"""

        key = f"/account/{username}"
        value = self.etcd_client.get(key)[0]
        return value is not None

    def new_account(self, account):
        """Creates a new account. Checks that the username doesn't exists"""

        with self.etcd_client.lock(self.lock):
            if self.exists_account(account.username):
                raise AccountAlreadyExistError(account.username)
            self.put_account(account)
