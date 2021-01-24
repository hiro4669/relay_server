# relay_server
This project is for gPBL 2021 for relaying data based on the connections using TCP connections and WebSocket respectively.
Two types of the relay are described as follows:


## TCP Connections
`relay_server.py` is the server program that connects multiple TCP connections based on the identifiers. When more than one TCP connections connect this server with the same identifier (ID), this server consider that they join the same channel. In one channel, the first connection can be a sender that send any data, then others will be receivers that receive the data sent from the sender.



## WebSocket


