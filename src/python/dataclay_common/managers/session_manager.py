import json
import uuid

from dataclay_common.exceptions.exceptions import *


class Session:
    def __init__(
        self, username, namespaces=[], datasets=[], default_dataset=None, is_active=True, **kwargs
    ):
        self.id = str(uuid.uuid4())
        self.username = username
        self.namespaces = namespaces
        self.datasets = datasets
        self.default_dataset = default_dataset
        self.is_active = is_active
        self.__dict__.update(kwargs)

    def key(self):
        return f"/session/{self.id}"

    def value(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, s):
        return cls(**json.loads(s))


class SessionManager:
    def __init__(self, etcd_client):
        self.etcd_client = etcd_client

    def put_session(self, session):
        self.etcd_client.put(session.key(), session.value())

    def get_session(self, session_id):
        """Return Session with session_id."""
        key = f"/session/{session_id}"
        value = self.etcd_client.get(key)[0]
        if value is None:
            raise SessionDoesNotExistError(session_id)

        return Session.from_json(value)

    def delete_session(self, session_id):
        key = f"/session/{session_id}"
        self.etcd_client.delete(key)
