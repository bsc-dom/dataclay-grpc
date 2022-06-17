
# For python
python3 -m grpc_tools.protoc \
--proto_path=protos \
--python_out=src/python/dataclay_common/protos \
--grpc_python_out=src/python/dataclay_common/protos \
protos/metadata_service.proto