proto:
	poetry run python -m grpc_tools.protoc -I./fiber-proto --python_out=./fiber/proto --pyi_out=./fiber/proto ./fiber-proto/types.proto
	poetry run python -m grpc_tools.protoc -I./fiber-proto --python_out=./fiber/proto --pyi_out=./fiber/proto ./fiber-proto/eth.proto
	poetry run python -m grpc_tools.protoc -I./fiber-proto --python_out=./fiber/proto --pyi_out=./fiber/proto --grpc_python_out=./fiber/proto ./fiber-proto/api.proto
