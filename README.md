# Subject: 

Design and Development of a micro-services-based Network Configuration Project.

# Details:

The micro-services project is based on **gRPC** and **Protobuf**.
The language pick is: **C++** / **Python**

The gRPC Network Configuration service should provide the following methods: \
-Set Network interface status (up/down)\
-Set Network interface main configuration (DHCP/static)\
-Set Network interface other configuration (MAC@, metric, ...etc)\
-Return list of Network interfaces\
-Return the detailed information about one or all interfaces\
-Set the network route configuration.

# Nice to have:
**Yocto** : Linux build system\
**Project (Yocto)** : Development of Yocto recipe for the project.
# Architecture
[Embedded Device] <-------------------> [Client : Web App , Mobile , Python/C++ ]

# Steps
1) Hands on Protobuf and gRPC
2) Test the hello world gRPC example
3) Develop the proto file for the project (LinuxNetManager.proto)
4) Develop the server API functions
5) Test (grpcurl)
6) (Nice to have): Hands on Yocto , develop the recipe

# Acquired technical skills:
- gRPC
- Protobuf
- Python/C++
- Linux network commands
- Networking (Network interfaces, ...)
- Yocto