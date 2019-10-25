#!/bin/bash

###########################################################################################################
#
# This script requires a local installation of:
#         protobuf >= 3.5.0
#         grpc-java >= 1.10.0                                                                              
#
#         https://github.com/grpc/grpc-java/blob/master/COMPILING.md#how-to-build-code-generation-plugin  
#                                                                                                         
###########################################################################################################

PLUGIN_PATH="/opt/grpc-java/compiler/build/exe/java_plugin/protoc-gen-grpc-java"

PROTOC_VERSION="libprotoc 3.7.1"
PROTOC_CUR_VERSION=`protoc --version`
if [ "$PROTOC_VERSION" != "$PROTOC_CUR_VERSION" ]; then

cat<<EOF
	$PROTOC_CUR_VERSION is different than expected $PROTOC_VERSION. 

	You can download required version from Google GitHub:
	
	export PROTOC_ZIP=protoc-3.6.1-linux-x86_64.zip
	curl -OL https://github.com/google/protobuf/releases/download/v3.6.1/\$PROTOC_ZIP
EOF
	exit -1
fi

function generateMessagesAndGRPC {
	SERVERNAME=$1
	MESSAGES_NAME="_messages"
	PROTOC_PARAMS="--plugin=protoc-gen-grpc-java=$PLUGIN_PATH --proto_path=./src/ --java_out=./src/ --grpc-java_out=./src/"
	
	echo "Cleaning $SERVERNAME messages..."
	rm -rf ./src/dataclay/communication/grpc/messages/$SERVERNAME/*.java
	
	echo "Compiling $SERVERNAME messages..."
	protoc $PROTOC_PARAMS "./src/dataclay/communication/grpc/messages/$SERVERNAME/$SERVERNAME$MESSAGES_NAME.proto"
	
	echo "Cleaning $SERVERNAME grpc..."
	rm -rf ./src/dataclay/communication/grpc/generated/$SERVERNAME/*.java
	
	echo "Compiling $SERVERNAME grpc..."
	protoc $PROTOC_PARAMS "./src/dataclay/communication/grpc/generated/$SERVERNAME/$SERVERNAME.proto"
}

function cleanGrpcCode {
	echo "Cleaning GRPC code..."
	pushd src/dataclay/communication/grpc

	# comment bad code
	#for i in `grep -l "private static abstract class" -r .`; do sed -i 's/private static abstract class/\/\*private static abstract class/g' $i; done
	#for i in `grep -l "private static volatile" -r .`; do sed -i 's/private static volatile/\*\/private static volatile/g' $i; done

	# comment setdescriptor referencing previously commented wrong code
	#for i in `grep -l setSchemaDescriptor -r . `; do sed -i 's/\.setSchemaDescriptor/\/\/\.setSchemaDescriptor/g' $i; done

	# add supress warnings
	for i in `ls generated/*/*.java messages/*/*java`; do sed -i 's/public final class/@SuppressWarnings(\"all\")\npublic final class/' $i; done

	popd
}

if [ "$#" -ne 1 ]; then
	echo ""
	echo "**"
	echo "** GRPC plugin path not specified. Using default: "
	echo "** $PLUGIN_PATH"
	echo "**"
	echo ""
else 
	PLUGIN_PATH=$1
fi



echo "Cleaning common messages..."
rm -rf ./src/dataclay/communication/grpc/messages/common/*.java
echo "Compiling common messages..."
protoc --proto_path=./src/ --plugin=protoc-gen-grpc-java=$PLUGIN_PATH --java_out=./src/ ./src/dataclay/communication/grpc/messages/common/common_messages.proto

generateMessagesAndGRPC "dataservice"
generateMessagesAndGRPC "logicmodule"

cleanGrpcCode
