#!/bin/bash
echo -e  "press 1 to compile proto file \npress 2 to turn off interface \npress 3 to turn on interface \npress 4 to show interface details "
read -r answer
case "${answer}" in
    1)
        echo "compiling proto files"
        python -m grpc_tools.protoc --proto_path=. --python_out=.. --grpc_python_out=.. network_manager.proto
    ;;
    2)
        echo "enter interface name to turn off"
        read -r -a interfaceName
        argumentArray=(--plaintext -proto protos/network_manager.proto -d '{"name" : "'${interfaceName}'"}' localhost:5000 Manager.turn_off_interface)
        grpcurl "${argumentArray[@]}"
    ;;
    3)
        echo "enter interface name to turn on"
        read -r -a interfaceName
        argumentArray=(--plaintext -proto protos/network_manager.proto -d '{"name" : "'${interfaceName}'"}' localhost:5000 Manager.turn_on_interface)
        grpcurl "${argumentArray[@]}"
    ;;
    4)
        echo "enter interface name "
        read -r -a interfaceName
        argumentArray=(--plaintext -proto protos/network_manager.proto -d '{"name" : "'${interfaceName}'"}' localhost:5000 Manager.show_one_interface)
        grpcurl "${argumentArray[@]}"
    ;;
    *)
        echo "enter valid option"
    ;;
esac

