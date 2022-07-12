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
        class_id,
        dataset_name,
        execution_environments_id,
        lang,
        owner,
        is_read_only=False,
        alias=None,
    ):
        """
        Args:
            id: Object id.
            class_id: Object's class id.
            dataset_name: Object's dataset name.
            execution_environments_id: List of execution environments where the object is stored
            is_read_only: If object is read only
            alias: Object's alias
            lang: Object's language
            owner: Username of object's owner account
        """
        self.id = id
        self.class_id = class_id
        self.dataset_name = dataset_name
        self.execution_environments_id = execution_environments_id
        self.lang = lang
        self.owner = owner
        self.is_read_only = is_read_only
        self.alias = alias

    def key(self):
        return f"/object/{self.id}"

    def value(self):
        return json.dumps(self.__dict__)


class ObjectManager:

    lock = "lock_object"

    def __init__(self, etcd_client):
        self.etcd_client = etcd_client

    def register_object(self, object_metadata):
        self.etcd_client.put(object_metadata.key(), object_metadata.value())
