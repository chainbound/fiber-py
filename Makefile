proto:
	poetry run python -m grpc_tools.protoc -I./fiber-proto --python_out=./fiber/ --pyi_out=./fiber/ ./fiber-proto/types.proto
	poetry run python -m grpc_tools.protoc -I./fiber-proto --python_out=./fiber/ --pyi_out=./fiber/ ./fiber-proto/eth.proto
	poetry run python -m grpc_tools.protoc -I./fiber-proto --python_out=./fiber/ --pyi_out=./fiber/ --grpc_python_out=./fiber/ ./fiber-proto/api.proto