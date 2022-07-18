import json
import uuid

from dataclay_common.protos import common_messages_pb2
from dataclay_common.protos.common_messages_pb2 import LANG_NONE


class ExecutionEnvironment:
    def __init__(self, id, name, hostname, port, language, dataclay_id):
        # TODO: Create new uuid if id is none
        self.id = id
        self.name = name
        self.hostname = hostname
        self.port = port
        self.language = language
        self.dataclay_id = dataclay_id

    def key(self):
        return f"/executionenvironment/{self.id}"

    def value(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, s):
        return cls(**json.loads(s))

    @classmethod
    def from_proto(cls, proto):
        exe_env = cls(
            proto.id,
            proto.name,
            proto.hostname,
            proto.port,
            proto.language,
            proto.dataclay_id,
        )
        return exe_env

    # TODO: Improve it with __getattributes__ and interface
    def get_proto(self):
        return common_messages_pb2.ExecutionEnvironment(
            id=self.id,
            name=self.name,
            hostname=self.hostname,
            port=self.port,
            language=self.language,
            dataclay_id=self.dataclay_id,
        )


class DataclayManager:

    lock = "lock_dataclay"

    def __init__(self, etcd_client):
        self.etcd_client = etcd_client

    def put_ee(self, exe_env):
        """Put execution environment to etcd"""

        self.etcd_client.put(exe_env.key(), exe_env.value())

    def get_all_execution_environments(self, lang=None):
        """Get all execution environments"""

        prefix = "/executionenvironment/"
        values = self.etcd_client.get_prefix(prefix)
        exe_envs = dict()
        for value, metadata in values:
            key = metadata.key.decode().split("/")[-1]
            exe_env = ExecutionEnvironment.from_json(value)
            if lang is None or lang == LANG_NONE or exe_env.language == lang:
                exe_envs[key] = exe_env
        return exe_envs

    def exists_ee(self, id):
        """ "Returns true if the execution environment exists"""

        key = f"/executionenvironment/{id}"
        value = self.etcd_client.get(key)[0]
        return value is not None

    def new_execution_environment(self, exe_env):
        """Creates a new execution environment. Checks that the it doesn't exists"""

        with self.etcd_client.lock(self.lock):
            if self.exists_ee(exe_env.id):
                raise Exception(f"ExecutionEnvironment {exe_env.id} already exists!")
            self.put_ee(exe_env)
