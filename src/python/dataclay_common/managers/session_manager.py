import json
import uuid

from dataclay_common.exceptions.exceptions import *


class Session:
    def __init__(self, username, namespaces=[], datasets=[], default_dataset=None, is_active=True):
        self.id = str(uuid.uuid4())
        self.username = username
        self.namespaces = namespaces
        self.datasets = datasets
        self.default_dataset = default_dataset
        self.is_active = is_active

    def key(self):
        return f"/session/{self.id}"

    def value(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, s):
        value = json.loads(s)
        session = cls(
            value["username"],
            value["namespaces"],
            value["datasets"],
            value["default_dataset"],
            value["is_active"],
        )
        return session


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
            raise SessionDoesNotExistError

        return Session.from_json(value)

    def delete_session(self, id):
        key = f"/session/{id}"
        self.etcd_client.delete(key)
