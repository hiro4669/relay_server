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
                Socket socket = new Socket("192.168.3.11", 8888);
                PrintWriter pw = new PrintWriter(socket.getOutputStream(), true);
                BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                String line = br.readLine();
                pw.println(line + "received!");
                br.close();
                pw.close();
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
# Run your client app

Run a simple server program (such as C or python) and then run the program.

<img width="908" alt="スクリーンショット 2021-02-09 15 54 55" src="https://user-images.githubusercontent.com/50857020/107686338-70772100-6ce8-11eb-8a96-3fbc7eaa65e6.png">


