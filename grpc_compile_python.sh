#!/bin/bash

function generateMessagesAndGRPC {
	SERVERNAME=$1
	MESSAGES_NAME="_messages"
	echo "Cleaning $SERVERNAME messages..."
	rm -rf ./pyclay/dataclay/communication/grpc/messages/$SERVERNAME/$SERVERNAME_pb2_grpc.py
	rm -rf ./pyclay/dataclay/communication/grpc/messages/$SERVERNAME/$SERVERNAME_pb2.py
	echo "Compiling $SERVERNAME messages..."
	# Probably for the messages we can remove --grpc_python_out
	python -m grpc.tools.protoc -I=./src/ --proto_path=.  --python_out=./pyclay/src/ --grpc_python_out=./pyclay/src/ ./src/dataclay/communication/grpc/messages/$SERVERNAME/$SERVERNAME$MESSAGES_NAME.proto
	echo "Cleaning $SERVERNAME grpc..."
	rm -rf ./pyclay/dataclay/communication/grpc/generated/$SERVERNAME/$SERVERNAME_messages_pb2_grpc.py
	rm -rf ./pyclay/dataclay/communication/grpc/generated/$SERVERNAME/$SERVERNAME_messages_pb2.py
	echo "Compiling $SERVERNAME grpc..."
	python -m grpc.tools.protoc -I=./src/ --proto_path=. --python_out=./pyclay/src/ --grpc_python_out=./pyclay/src/ ./src/dataclay/communication/grpc/generated/$SERVERNAME/$SERVERNAME.proto
}

echo "Cleaning common messages..."
rm -rf ./pyclay/dataclay/communication/grpc/messages/common/common_messages_pb2_grpc.py
rm -rf ./pyclay/dataclay/communication/grpc/messages/common/common_messages_pb2.py
echo "Compiling common messages..."
python -m grpc.tools.protoc -I=./src/ --proto_path=. --python_out=./pyclay/src/ --grpc_python_out=./pyclay/src/ ./src/dataclay/communication/grpc/messages/common/common_messages.proto


generateMessagesAndGRPC "dataservice"
generateMessagesAndGRPC "logicmodule"

