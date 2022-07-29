import json
import uuid

from dataclay_common.exceptions.exceptions import *
from dataclay_common.utils.json import UUIDEncoder, uuid_parser


class Session:
    def __init__(self, id, username, default_dataset=None, is_active=True):
        self.id = id
        self.username = username
        self.default_dataset = default_dataset
        self.is_active = is_active

    def key(self):
        return f"/session/{self.id}"

    def value(self):
        return json.dumps(self.__dict__, cls=UUIDEncoder)

    @classmethod
    def from_json(cls, s):
        return cls(**json.loads(s, object_hook=uuid_parser))


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

    def exists_session(self, session_id):
        """ "Returns ture if the session exists, false otherwise"""

        key = f"/session/{session_id}"
        value = self.etcd_client.get(key)[0]
        return value is not None

    def delete_session(self, session_id):
        key = f"/session/{session_id}"
        self.etcd_client.delete(key)
