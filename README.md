# relay_server
This project is for gPBL 2021 for relaying data based on the connections using TCP connections and WebSocket respectively.
Two types of the relay are described as follows:


## TCP Connections
`relay_server.py` is the server program that connects multiple TCP connections based on the identifiers. When more than one TCP connections connect this server with the same identifier (ID), this server consider that they join the same channel. After a connection is established between a client and the server, a server should send a type of client and channel name. If a client sends *Sender* type, it can be a sender that can send data using the connection. Besides if a client sends "Receiver" type, it can be a receiver that will receive data sent from the sender. Note that, the sender should be only one while the receiver can be more than one. If two clients send the type as *Sender*, the latter can be a sender.

### Header
relay_server waits the header that can be used to decide whether the connection can be a sender or receiver, and identify the channel.
|  |Num of Bytes|Example|
|-----------|------------|------------|
|client type|1byte|0x1(Sender)｜0x2(Receiver)|
|length of channel name|1byte|ex.)3|
|channel name|channel len|ex.)"abc"|

## Demo
The following run a sender and two receivers. Before running then, you should run the relay_server.py
![demo](https://user-images.githubusercontent.com/52157596/104133039-6bab0e80-53c4-11eb-8b99-6abc4ff7d79a.gif)

This demo consists of two classes that extend one super class using Java language

## Classes
This demo consists of one abstract class called *TCPClient*, and two concrete classes called *SenderClient* and *ReceiverClient*. The followings are class diagrams.


![class](https://user-images.githubusercontent.com/52157596/104190985-3eac3980-5460-11eb-9c7b-51717357f0e4.png)

## フィールド
|フィールド名|初期値|説明|
|-----------|------------|------------|
|HOST|"127.0.0.1"|ローカルサーバのIPアドレス|
|PORT|8888|ローカルサーバのポート|
|CHANNEL|"abc"|チャネル名。チャネル名が同じクライアント同士しかデータのやり取りは行われない。|
|OK_MESSAGE|"OK"|ヘッダーの認証判定に使用される。|
|DISCONNECT_SIGN|"DISCONNECT"|後述のreceive()内でサーバ側からの接続解除が検知された場合の戻り値として使用される。|
|CHAR_CODE|StandardCharsets.US_ASCII|文字コード(ASCII)|
|BUFFER_SIZE|1024|送受信可能な最大バイト数|
|clientType|-|enum列挙型であるClientTypeのオブジェクト。ヘッダーに送信する用として、フィールドidを持つ。|
|socket|-|JavaによるTCP通信を実現する[java.net.Socket](https://docs.oracle.com/javase/jp/8/docs/api/java/net/Socket.html)クラスのインスタンス。|
|in|-|socketのフィールドである入力ストリーム。受信時にソケットからバイトを読み込むために使用。|
|out|-|socketのフィールドである出力ストリーム。送信時にソケットにバイトを書き込むために使用。|

## メソッド
|メソッド|説明|
|-----------|------------|
|createHeader(): byte[]|前述したヘッダーを作成し、バイト配列に変換したものを返す。|
|connect(): void|ソケットの作成・コネクションの確立・ヘッダーをcreateHeader()で作成し、送信。|
|disconnect(): void|接続解除。socketをclose。|
|send(buffer: byte[]): void|バイト配列bufferを送信。|
|receive(): String|実行と同時に受信待ち状態に。サーバから受信が開始されると1バイトずつ読み取り、バイト配列を作成し、ASCIIでデコードした文字列を返す。サーバからの接続解除が検知された時、フィールドDISCONNECT_SIGNを返す。|
|initClientType(): void|SenderClient・ReceiverClientでオーバーライド。フィールドclientTypeの初期化を行う。|
|run(): void|SenderClient・ReceiverClientでオーバーライド。ソケットのコネクション確立後に実行される。前述のアクティビティ図の最後2つのアクションノードが実行される。|


## WebSocket


