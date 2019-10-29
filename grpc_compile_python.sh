#!/bin/bash

if [[ -z $1 ]]; then
	echo "Usage: bash $0 <pyclay_src_path>"
	exit
fi

PYCLAY_SRC=$1
PROTOS_ROOT="./protos"

for PROTO_FILE in $(find $PROTOS_ROOT -name '*proto')
do
	echo "Compiling $PROTO_FILE"
	python -m grpc.tools.protoc -I=$PROTOS_ROOT --python_out=$PYCLAY_SRC --grpc_python_out=$PYCLAY_SRC $PROTO_FILE
done
