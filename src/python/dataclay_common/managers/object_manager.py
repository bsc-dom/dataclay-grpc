import json
import uuid

from dataclay_common.protos import common_messages_pb2
from dataclay_common.protos.common_messages_pb2 import LANG_NONE
from dataclay_common.exceptions.exceptions import *


class ObjectMetadata:
    def __init__(
        self,
        id,
        alias_name,
        dataset_name,
        class_id,
        execution_environment_ids,
        language,
        owner,
        is_read_only=False,
    ):
        self.id = id
        self.alias_name = alias_name
        self.dataset_name = dataset_name
        self.class_id = class_id
        self.execution_environment_ids = execution_environment_ids
        self.language = language
        self.owner = owner
        self.is_read_only = is_read_only

    def key(self):
        return f"/object/{self.id}"

    def value(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_proto(cls, proto):
        object_md = cls(
            proto.id,
            proto.alias_name,
            proto.dataset_name,
            proto.class_id,
            list(proto.execution_environment_ids),
            proto.language,
            proto.owner,
            proto.is_read_only,
        )
        return object_md

    def get_proto(self):
        return common_messages_pb2.ObjectMetadata(
            id=str(self.id),
            alias_name=self.alias_name,
            dataset_name=self.dataset_name,
            class_id=str(self.class_id),
            execution_environment_ids=self.execution_environment_ids,
            language=self.language,
            owner=self.owner,
            is_read_only=self.is_read_only,
        )

    @classmethod
    def from_json(cls, s):
        value = json.loads(s)
        object_md = cls(
            value["id"],
            value["alias_name"],
            value["dataset_name"],
            value["class_id"],
            value["execution_environment_ids"],
            value["language"],
            value["owner"],
            value["is_read_only"],
        )
        return object_md


class Alias:
    def __init__(self, name, dataset_name, object_id):
        """Return an instance of an Alias"""
        self.name = name
        self.dataset_name = dataset_name
        self.object_id = object_id

    def key(self):
        return f"/alias/{self.dataset_name}/{self.name}"

    def value(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, s):
        value = json.loads(s)
        alias = cls(value["name"], value["dataset_name"], value["object_id"])
        return alias


class ObjectManager:

    lock = "lock_object"

    def __init__(self, etcd_client):
        self.etcd_client = etcd_client

    def register_object(self, object_metadata):
        self.etcd_client.put(object_metadata.key(), object_metadata.value())

    def put(self, o):
        self.etcd_client.put(o.key(), o.value())

    def get_alias(self, alias_name, dataset_name):
        # Get dataset from etcd and checks that it exists
        key = f"/alias/{dataset_name}/{alias_name}"
        value = self.etcd_client.get(key)[0]
        if value is None:
            raise AliasDoesNotExistError

        return Alias.from_json(value)

    def get_object_md(self, object_id):
        # Get dataset from etcd and checks that it exists
        key = f"/object/{object_id}"
        value = self.etcd_client.get(key)[0]
        if value is None:
            raise ObjectDoesNotExistError

        return ObjectMetadata.from_json(value)

    def new_alias(self, alias):
        """Creates a new alias and checks that the alias doesn't exists"""

        with self.etcd_client.lock(self.lock):
            if self.etcd_client.get(alias.key())[0] is not None:
                raise AliasAlreadyExistError
            self.put(alias)
