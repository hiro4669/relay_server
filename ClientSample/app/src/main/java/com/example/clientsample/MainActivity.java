package com.example.clientsample;

import androidx.appcompat.app.AppCompatActivity;

import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void ClickEvent(View view){
        TextView tv = (TextView) findViewById(R.id.Text);
        DoTask doTask = new DoTask(tv);
        doTask.execute();
        Log.d("debug","push");
    }

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
}