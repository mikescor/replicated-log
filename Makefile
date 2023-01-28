build:
	docker-compose up -d --build

master-stubs:
	python -m grpc_tools.protoc -I ./protos --python_out=src/ --grpc_python_out=src/ ./protos/log.proto

secondary-stubs:
	python -m grpc_tools.protoc -I ./protos --python_out=src/ --grpc_python_out=src/ ./protos/msg_replication.proto

master-client:
	python src/master_client.py

secondary-client:
	python src/secondary_client.py

master-logs:
	docker logs replicated-log-master-1 -f

s1-logs:
	docker logs replicated-log-secondary-one-1 -f

s2-logs:
	docker logs replicated-log-secondary-two-1 -f
