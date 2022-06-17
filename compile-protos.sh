
# For python
python3 -m grpc_tools.protoc \
--proto_path=. \
--python_out=src/python/dataclay_common \
--grpc_python_out=src/python/dataclay_common \
protos/metadata_service.proto

# replace import path to local
sed -i '0,/from protos/{s/from protos/from ./}' \
src/python/dataclay_common/protos/*_pb2_grpc.py