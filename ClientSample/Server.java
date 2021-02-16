import java.io.IOException;
import java.io.DataInputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {

  public static void main(String[] args) {
    try{
      //サーバーのポート番号を指定
      ServerSocket svSock = new ServerSocket(8888);

      //アクセスを待ち受け
      Socket sock = svSock.accept();

      //受信ストリームの取得(DataInputStreamでラップ)
      DataInputStream in = new DataInputStream(sock.getInputStream());

      //int型データを受信
      int intData = in.readInt();

      //String型データを受信
      String strData = in.readUTF();

      //double型データを受信
      double dblData = in.readDouble();

      System.out.println("「"+intData+"」received.");
      System.out.println("「"+strData+"」received.");
      System.out.println("「"+dblData+"」received.");

      //受信ストリームの終了
      in.close();

      //サーバー終了
      svSock.close();

    }catch(IOException e){
      e.printStackTrace();
    }
  }
}
