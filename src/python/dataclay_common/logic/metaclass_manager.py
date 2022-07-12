import json
import logging

logger = logging.getLogger(__name__)


# TODO: Extend class to generic with key(), value(), ...
class Metaclass:
    def __init__(self):
        pass

    @classmethod
    def from_json(cls, value):
        metaclass = cls(
            value["username"],
            password=value["password"],
            role=value["role"],
            namespaces=value["namespaces"],
            datasets=value["datasets"],
        )
        return metaclass

    def key(self):
        return f"/metaclass/{self.id}"

    def value(self):
        return json.dumps(self.__dict__)


class MetaclassManager:
    def __init__(self, etcd_client):
        self.etcd_client = etcd_client

    def get_metaclass(self, id):
        # Get metaclass from etcd and checks that it exists
        key = f"/metaclass/{id}"
        value = self.etcd_client.get(key)[0]
        if value is None:
            raise Exception(f"Metaclass {id} does not exists!")

        return Metaclass.from_json(value)
