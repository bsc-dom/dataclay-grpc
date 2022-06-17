
# For python
python3 -m grpc_tools.protoc \
--proto_path=. \
--python_out=src/python/dataclay_common \
protos/common_messages.proto \
protos/dataservice_messages.proto \
protos/logicmodule_messages.proto

# Protobuf + grpc
python3 -m grpc_tools.protoc \
--proto_path=. \
--python_out=src/python/dataclay_common \
--grpc_python_out=src/python/dataclay_common \
protos/dataservice.proto \
protos/logicmodule.proto \
protos/metadata_service.proto

# Replace wrong import from pb2_grpc.py
sed -i 's/from protos/from ./g' \
src/python/dataclay_common/protos/*pb2*.py