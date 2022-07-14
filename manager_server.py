from codecs import unicode_escape_decode
from concurrent import futures
import importlib
import logging
import grpc
import network_manager_pb2
import network_manager_pb2_grpc
import subprocess

class Manager(network_manager_pb2_grpc.ManagerServicer):

    def turn_off_interface(self, request, context):
        subprocess.run(["sudo","ifconfig",request.name,"down"])
        print(f"turning interface {request.name} off")
        return network_manager_pb2.InterfaceResponse(message=f"hi , interface {request.name} is off")


    def turn_on_interface(self, request, context):
        subprocess.run(["sudo","ifconfig",request.name,"up"])
        print(f"turning interface {request.name} on")
        return network_manager_pb2.InterfaceResponse(message=f"hi , interface {request.name} is on")

    def show_one_interface(self, request, context):
        nmcli_output = subprocess.check_output(["ip", "link", "show", request.name]).decode("utf-8")
        print(nmcli_output)
        return network_manager_pb2.InterfaceResponse(message=nmcli_output.replace("\n",""))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    network_manager_pb2_grpc.add_ManagerServicer_to_server(Manager(),server)
    server.add_insecure_port('localhost:5000')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()