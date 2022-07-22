from codecs import unicode_escape_decode
from concurrent import futures
from doctest import OutputChecker
from email import message
import importlib
import logging
import grpc
from tempita import sub
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
        return network_manager_pb2.InterfaceResponse(message=nmcli_output.replace("\n"," "))

    def show_all_interfaces(self, request, context):
        nmcli_output = subprocess.check_output(["ip", "link", "show"]).decode("utf-8")
        print(nmcli_output)
        return network_manager_pb2.InterfaceResponse(message=nmcli_output.replace("\n"," "))

    def list_interfaces(self, request, context):
        output=subprocess.getoutput('nmcli device status | tail -n +2')
        print(output)
        return network_manager_pb2.InterfaceResponse(message=output.replace("\n"," "))

    def set_configuration_dhcp(self, request, context):
        subprocess.run(["nmcli","device","modify",request.name,"ipv4.method","auto"])
        return network_manager_pb2.ConfigResponse(message=f"interface {request.name} is set to dhcp.")

    def set_configuration_static(self, request, context):
        subprocess.run(["nmcli","device","modify",request.interface,"ipv4.method","manual","ipv4.addresses",request.ipv4_address,"gw4",request.ipv4_gateway,"ipv4.dns",request.ipv4_dns])
        return network_manager_pb2.ConfigResponse(message=f"interface {request.interface} is set to static.")

    def add_network_route(self, request, context):
        process=subprocess.Popen(["sudo","ip","route","add",request.destination,"via",request.route,"dev",request.interface],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout,stderr=process.communicate()
        return_code=process.returncode
        if(return_code==0):
            ouput="network route added"
        else:
            output=stderr
        return network_manager_pb2.ConfigResponse(message=output)
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    network_manager_pb2_grpc.add_ManagerServicer_to_server(Manager(),server)
    server.add_insecure_port('localhost:5000')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()