import logging
import atexit

import grpc
from google.protobuf.empty_pb2 import Empty

from dataclay_common.protos import metadata_service_pb2_grpc
from dataclay_common.protos import metadata_service_pb2
from dataclay_common.protos import common_messages_pb2
from dataclay_common.managers.dataclay_manager import ExecutionEnvironment
from dataclay_common.managers.object_manager import ObjectMetadata

logger = logging.getLogger(__name__)


class MDSClient:
    def __init__(self, hostname, port):
        self.address = f"{hostname}:{port}"
        self.channel = grpc.insecure_channel(self.address)
        self.stub = metadata_service_pb2_grpc.MetadataServiceStub(self.channel)
        atexit.register(self.close)

    def close(self):
        self.channel.close()

    ###################
    # Session Manager #
    ###################

    def new_session(self, username, password, default_dataset):
        request = metadata_service_pb2.NewSessionRequest(
            username=username, password=password, default_dataset=default_dataset
        )
        response = self.stub.NewSession(request)
        return response.id

    def close_session(self, id):
        request = metadata_service_pb2.CloseSessionRequest(id=str(id))
        self.stub.CloseSession(request)

    ###################
    # Account Manager #
    ###################

    def new_account(self, username, password):
        request = metadata_service_pb2.NewAccountRequest(username=username, password=password)
        self.stub.NewAccount(request)

    ###################
    # Dataset Manager #
    ###################

    def new_dataset(self, username, password, dataset):
        request = metadata_service_pb2.NewDatasetRequest(
            username=username, password=password, dataset=dataset
        )
        self.stub.NewDataset(request)

    #####################
    # EE-SL information #
    #####################

    def get_all_execution_environments(self, language, get_external=True, from_backend=False):
        request = metadata_service_pb2.GetAllExecutionEnvironmentsRequest(
            language=language, get_external=get_external, from_backend=from_backend
        )
        response = self.stub.GetAllExecutionEnvironments(request)

        result = dict()
        for id, proto in response.exe_envs.items():
            result[id] = ExecutionEnvironment.from_proto(proto)
        return result

    ##############
    # Federation #
    ##############

    def get_dataclay_id(self):
        response = self.stub.GetDataclayID(Empty())
        return response.dataclay_id

    ################
    # Autoregister #
    ################

    def autoregister_ee(self, id, name, hostname, port, lang):
        request = metadata_service_pb2.AutoRegisterEERequest(
            id=id, name=name, hostname=hostname, port=port, lang=lang
        )
        self.stub.AutoregisterEE(request)

    ###################
    # Object Metadata #
    ###################

    def register_object(self, session_id, object_md):
        request = metadata_service_pb2.RegisterObjectRequest(
            session_id=session_id, object_md=object_md.get_proto()
        )
        self.stub.RegisterObject(request)

    def get_object_from_alias(self, session_id, alias_name, dataset_name):
        request = metadata_service_pb2.GetObjectFromAliasRequest(
            session_id=session_id, alias_name=alias_name, dataset_name=dataset_name
        )
        response = self.stub.GetObjectFromAlias(request)
        return response.object_id, response.class_id, response.hint

    def delete_alias(self, session_id, alias_name, dataset_name):
        request = metadata_service_pb2.DeleteAliasRequest(
            session_id=session_id, alias_name=alias_name, dataset_name=dataset_name
        )
        self.stub.DeleteAlias(request)
