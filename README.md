# relay_server
This project is for gPBL 2021 for relaying data based on the connections using TCP connections and WebSocket respectively.
Two types of the relay are described as follows:


## TCP Connections
`relay_server.py` is the server program that connects multiple TCP connections based on the identifiers. When more than one TCP connections connect this server with the same identifier called *Channel*, this server consider that they join the same channel. After a connection is established between a client and the server, a server should send a type of client and channel name. If a client sends *Sender* type, it can be a sender that can send data using the connection. Besides if a client sends "Receiver" type, it can be a receiver that will receive data sent from the sender. Note that, the sender should be only one while the receiver can be more than one. If two clients send the type as *Sender*, the latter can be a sender.

### Header
relay_server waits the header that can be used to decide whether the connection can be a sender or receiver, and identify the channel.
|  |Num of Bytes|Example|
|-----------|------------|------------|
|client type|1byte|0x1(Sender)｜0x2(Receiver)|
|length of channel name|1byte|ex.)3|
|channel name|channel len|ex.)"abc"|

### Demo
The following run a sender and two receivers. Before running then, you should run the relay_server.py
![demo](https://user-images.githubusercontent.com/52157596/104133039-6bab0e80-53c4-11eb-8b99-6abc4ff7d79a.gif)

This demo consists of two classes that extend one super class using Java language

### Classes
This demo consists of one abstract class called *TCPClient*, and two concrete classes called *SenderClient* and *ReceiverClient*. The followings are class diagrams.


![class](https://user-images.githubusercontent.com/52157596/104190985-3eac3980-5460-11eb-9c7b-51717357f0e4.png)

### Fields
|Field Name|Initial Value|Descriptions|
|-----------|------------|------------|
|HOST|"127.0.0.1"|IP Address|
|PORT|8888|Port Number|
|CHANNEL|"abc"|Channel Name|
|OK_MESSAGE|"OK"|Used if the header can be accepted or not|
|DISCONNECT_SIGN|"DISCONNECT"|Used when the server disconnects the connection as a return value from *receive()*|
|CHAR_CODE|StandardCharsets.US_ASCII|ASCII code|
|BUFFER_SIZE|1024|Maxmum length of byte to be sent and received|
|clientType|-|Client type|
|socket|-|An instance of Socket class|
|in|-|java.io.InputStream|
|out|-|java.io.OutputStream|

### Methods
|Methods|Descriptions|
|-----------|------------|
|createHeader(): byte[]|Creates a header and return it as bytes|
|connect(): void| Connects to the relay_server|
|disconnect(): void|Disconnects the connection|
|send(buffer: byte[]): void|send bytes to the server|
|receive(): String|Receive data from the server, then create byte array as ASCII. When the server disconnects this connection, this method return DISCONNECT_SIGN field value|
|initClientType(): void|Initialize Client. This method should be overwritten by sub classes|
|run(): void|This method is invoked after establishing the connection. This method should be overwritten by sub classes.|


## WebSocket


