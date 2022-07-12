import logging
import atexit

import grpc
from google.protobuf.empty_pb2 import Empty

from dataclay_common.protos import metadata_service_pb2_grpc
from dataclay_common.protos import metadata_service_pb2
from dataclay_common.protos import common_messages_pb2
from dataclay_common.managers.dataclay_manager import ExecutionEnvironment

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

    def register_objects(self, reg_infos, backend_id, lang):
        objects_info = []
        for reg_info in reg_infos:
            object_info = common_messages_pb2.ObjectRegisterInfo(
                object_id=str(reg_info.object_id),
                class_id=str(reg_info.class_id),
                session_id=str(reg_info.store_session_id),
                dataset_name=str(reg_info.dataset_id),
                alias=reg_info.alias,
            )
            objects_info.append(object_info)

        request = metadata_service_pb2.RegisterObjectsRequest(
            objects_info=objects_info, backend_id=str(backend_id), lang=lang
        )
        response = self.stub.RegisterObjects(request)

        # result = list()
        # for oid in response.objectIDs:
        #     result.append(Utils.get_id(oid))
        # return result
