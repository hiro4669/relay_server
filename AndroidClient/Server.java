import java.io.IOException;
import java.io.DataInputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {

  public static void main(String[] args) {
    try{
      //Specify the port number of the server
      ServerSocket svSock = new ServerSocket(8888);

      //Wait for access
      Socket sock = svSock.accept();

      //Get the Input stream (wrapped in DataInputStream)
      DataInputStream in = new DataInputStream(sock.getInputStream());

      //Receive int type data
      int intData = in.readInt();

      //Receive String type data
      String strData = in.readUTF();

      //Receive double type data
      double dblData = in.readDouble();

      System.out.println("「"+intData+"」received.");
      System.out.println("「"+strData+"」received.");
      System.out.println("「"+dblData+"」received.");

      //End of Input stream
      in.close();

      //Server Termination
      svSock.close();

    }catch(IOException e){
      e.printStackTrace();
    }
  }
}
