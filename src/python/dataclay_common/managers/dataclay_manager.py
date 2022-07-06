import json
import uuid

from dataclay_common.protos import common_messages_pb2


class ExecutionEnvironment:
    def __init__(self, id, hostname, name, port, language):
        # TODO: Create new uuid if id is none
        self.id = id
        self.hostname = hostname
        self.name = name
        self.port = port
        self.language = language

    def key(self):
        return f'/executionenvironment/{self.id}'

    def value(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, s):
        value = json.loads(s)
        exe_env = cls(value['id'],
                      value['hostname'],
                      value['name'],
                      value['port'],
                      value['language'])
        return exe_env

    @classmethod
    def from_proto(cls, proto):
        exe_env = cls(proto.id,
                      proto.hostname,
                      proto.name,
                      proto.port,
                      proto.language)
        return exe_env

    # TODO: Improve it with __getattributes__ and interface
    def get_proto(self):
        return common_messages_pb2.ExecutionEnvironment(
            id=self.id,
            hostname=self.hostname,
            name=self.name,
            port=self.port,
            language=self.language)


class DataclayManager:

    lock = 'lock_dataclay'

    def __init__(self, etcd_client):
        self.etcd_client = etcd_client

    def put_ee(self, exe_env):
        """Put execution environment to etcd"""

        self.etcd_client.put(exe_env.key(), exe_env.value())

    def get_all_execution_environments(self):
        """Get all execution environments"""

        prefix = '/executionenvironment/'
        values = self.etcd_client.get_prefix(prefix)
        exe_envs = dict()
        for value, metadata in values:
            key = metadata.key.decode().split('/')[-1]
            exe_envs[key] = ExecutionEnvironment.from_json(value)
        return exe_envs

    def exists_ee(self, id):
        """"Returns true if the execution environment exists"""

        key = f'/executionenvironment/{id}'
        value = self.etcd_client.get(key)[0]
        return value is not None

    def new_execution_environment(self, exe_env):
        """Creates a new execution environment. Checks that the it doesn't exists"""

        with self.etcd_client.lock(self.lock):
            if self.exists_ee(exe_env.id):
                raise Exception(f'ExecutionEnvironment {exe_env.id} already exists!')
            self.put_ee(exe_env)
