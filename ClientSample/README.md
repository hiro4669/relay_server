# MainActivity.java
```bash
private static class DoTask extends AsyncTask<Integer, String ,String> {
        private TextView textView;
        public DoTask(TextView textView){
            this.textView = textView;
        }

        @Override
        protected String doInBackground(Integer... integers) {
            try{
                Log.d("debug","connected");
                Socket socket = new Socket("IP-Address", 8888);
                /*PrintWriter pw = new PrintWriter(socket.getOutputStream(), true);
                BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                String line = br.readLine();
                pw.println(line + "received!");
                br.close();
                pw.close();
                socket.close();*/

                //送信ストリームの取得(DataOutputStreamでラップ)
                DataOutputStream out = new DataOutputStream(socket.getOutputStream());

                //送信データ
                int intData = 100;
                String strData = "String";
                double dblData = 3.14;

                //int型送信
                out.writeInt(intData);

                //String型送信
                out.writeUTF(strData);

                //double型送信
                out.writeDouble(dblData);

                System.out.println("Send Prototype");

                //送信ストリームを表示
                out.close();

                //終了
                socket.close();
                return "Connected!!";
            }catch (Exception e){
                Log.d("debug","error");
                e.printStackTrace();
                return "error";
            }
        }
        @Override
        protected void onPostExecute(String str){
            //Setup precondition to execute some task
            textView.setText(str);
            Log.d("debug",str);
        }
    }
```
 
# Add DoTask(MainActivity.java)
 ```bash
 public void ClickEvent(View view){
        TextView tv = (TextView) findViewById(R.id.Text);
        DoTask doTask = new DoTask(tv);
        doTask.execute();
        Log.d("debug","push");
    }
 ```
 # Add a permittion(app/manifests/AndroidManifest.xml)
 
 ```bash
    …
     </activity>
    </application>
    <uses-permission android:name="android.permission.INTERNET"/>
</manifest>

 ```
# Run server(java)
 ```bash
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

      //受信データの表示
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

 ```
 
# Run your client app

Run a simple server program (such as C or python) and then run the program.

<img width="908" alt="スクリーンショット 2021-02-09 15 54 55" src="https://user-images.githubusercontent.com/50857020/107686338-70772100-6ce8-11eb-8a96-3fbc7eaa65e6.png">


