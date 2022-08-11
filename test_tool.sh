#!/bin/bash
echo -e  "press 1 to compile proto file \npress 2 to turn off interface \npress 3 to turn on interface \npress 4 to show interface details\npress 5 to show all interfaces details\npress 6 to list availabe interfaces\npress 7 to add a new route"
read -r answer
case "${answer}" in
    1)
        echo "compiling proto files"
        python -m grpc_tools.protoc --proto_path=protos/ --python_out=. --grpc_python_out=. protos/network_manager.proto
    ;;
    2)
        echo "enter interface name to turn off"
        read -r interfaceName
        argumentArray=(--plaintext -proto protos/network_manager.proto -d '{"name" : "'${interfaceName}'"}' localhost:5000 Manager.turn_off_interface)
        grpcurl "${argumentArray[@]}"
    ;;
    3)
        echo "enter interface name to turn on"
        read -r interfaceName
        argumentArray=(--plaintext -proto protos/network_manager.proto -d '{"name" : "'${interfaceName}'"}' localhost:5000 Manager.turn_on_interface)
        grpcurl "${argumentArray[@]}"
    ;;
    4)
        echo "enter interface name "
        read -r interfaceName
        argumentArray=(--plaintext -proto protos/network_manager.proto -d '{"name" : "'${interfaceName}'"}' localhost:5000 Manager.show_one_interface)
        grpcurl "${argumentArray[@]}"
    ;;
    5)
    grpcurl --plaintext -proto protos/network_manager.proto -d '{ }' localhost:5000 Manager.show_all_interfaces
    ;;
    6)
    grpcurl --plaintext -proto protos/network_manager.proto -d '{ }' localhost:5000 Manager.list_interfaces
    ;;
    7)
	echo "enter route ip"
	read -r route
	argumentArray=(--plaintext -proto protos/network_manager.proto -d '{"message" : "'${route}'"}' localhost:5000 Manager.add_network_route)
	grpcurl "${argumentArray[@]}"
    ;;
    *)
        echo "enter valid option"
    ;;
esac

