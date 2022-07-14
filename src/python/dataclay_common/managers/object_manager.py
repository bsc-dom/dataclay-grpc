import json
import uuid

from dataclay_common.protos import common_messages_pb2
from dataclay_common.protos.common_messages_pb2 import LANG_NONE


class ObjectRegisterInfo:
    def __init__(self, object_id, class_id, session_id, dataset_name, alias):
        # TODO: Create new uuid if id is none
        self.object_id = object_id
        self.class_id = class_id
        self.session_id = session_id
        self.dataset_name = dataset_name
        self.alias = alias

    @classmethod
    def from_proto(cls, proto):
        object_reg_info = cls(
            proto.object_id,
            proto.class_id,
            proto.session_id,
            proto.dataset_name,
            proto.alias,
        )
        return object_reg_info

    def get_proto(self):
        return common_messages_pb2.ObjectRegisterInfo(
            object_id=self.object_id,
            class_id=self.class_id,
            session_id=self.session_id,
            dataset_name=self.dataset_name,
            alias=self.alias,
        )


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


class ObjectManager:

    lock = "lock_object"

    def __init__(self, etcd_client):
        self.etcd_client = etcd_client

    def register_object(self, object_metadata):
        self.etcd_client.put(object_metadata.key(), object_metadata.value())

    def put(self, o):
        self.etcd_client.put(o.key(), o.value())
