generate-stubs:
	python -m grpc_tools.protoc -I ./protos --python_out=src/ --grpc_python_out=src/ ./protos/log.proto

generate-secondary-stubs:
	python -m grpc_tools.protoc -I ./protos --python_out=src/ --grpc_python_out=src/ ./protos/msg_replication.proto
