# relay_server
This project is for gPBL 2021 for relaying data based on the connections using TCP connections and WebSocket respectively.
Two types of the relay are described as follows:


## TCP Connections
`relay_server.py` is the server program that connects multiple TCP connections based on the identifiers. When more than one TCP connections connect this server with the same identifier (ID), this server consider that they join the same channel. After a connection is established between a client and the server, a server should send a type of client and channel name. If a client sends *Sender* type, it can be a sender that can send data using the connection. Besides if a client sends "Receiver" type, it can be a receiver that will receive data sent from the sender. Note that, the sender should be only one while the receiver can be more than one. If two clients send the type as *Sender*, the latter can be a sender.

### Header
relay_server waits the header that can be used to decide whether the connection can be a sender or receiver, and identify the channel.

[relay_server](https://github.com/hiro4669/relay_server/)/relay_server.pyでは、コネクション確立直後にヘッダー受信待ち状態になります。サーバは、クライアントからこのヘッダーを受信し、クライアントタイプ(SenderかReceiverか)を識別し、チャネルを決定します。ヘッダー情報の詳細は以下の通りになります。
|  |型|例|
|-----------|------------|------------|
|client type|1byte|0x1(Sender)｜0x2(Receiver)|
|length of channel name|4byte|ex.)3|
|channel name|channel len|ex.)"abc"|

## WebSocket


