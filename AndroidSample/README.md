# Install Android　Studio
 Go to https://developer.android.com/studio/index.html

* Click “Download ANDROID STUTIO”
* Suitable OS is selected automatically
 
# Open Android Studio
 Click “Create New Project”
 
 <img width="770" alt="スクリーンショット 2021-02-09 15 08 37" src="https://user-images.githubusercontent.com/50857020/107322980-d1380b00-6ae8-11eb-991c-5c3602f671e2.png">
 
 Click “Empty Acticity”
 
 <img width="892" alt="スクリーンショット 2021-02-09 15 13 13" src="https://user-images.githubusercontent.com/50857020/107323457-a5695500-6ae9-11eb-9df6-7a948a443bc7.png">
 
# Decide followings
* Name → “HelloAndroid”
* Save location → Favorite place

 <img width="889" alt="スクリーンショット 2021-02-09 15 24 45" src="https://user-images.githubusercontent.com/50857020/107324221-09404d80-6aeb-11eb-98ea-d6265c27fcde.png">

# Sample application

* "MainActivity.java" controls application behavior such as Object declaration.
* "activity_main.xml" manages the GUI-like appearance of the application.

<img width="1073" alt="スクリーンショット 2021-02-09 15 28 52" src="https://user-images.githubusercontent.com/50857020/107324512-89ff4980-6aeb-11eb-93da-1849fb96d83f.png">

# Change  View id

You can set ID on TextView and set the content text. In this case, set it as "Text".

<img width="971" alt="スクリーンショット 2021-02-09 15 38 26" src="https://user-images.githubusercontent.com/50857020/107325492-283fdf00-6aed-11eb-83e9-7cf875e5891b.png">

# Add a button

* Drag & drop _Button_
* Add a constraint

<img width="970" alt="スクリーンショット 2021-02-09 15 45 44" src="https://user-images.githubusercontent.com/50857020/107325897-e7949580-6aed-11eb-9418-d2116d9f22fe.png">

# Set onClick attribute

Change onClick attribute to “ChangeTxt”

<img width="267" alt="スクリーンショット 2021-02-09 15 49 55" src="https://user-images.githubusercontent.com/50857020/107326268-79040780-6aee-11eb-9078-d8b09ecf1c0f.png">

# Open MainActivity.java

Add “ChangeTxt”

```bash
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void ChangeTxt(View view){
        TextView tv = (TextView)findViewById(R.id.Text);
        tv.setText("Hello World !");
        Log.d("debug", "Hello");
    }

}
```
# Run your app 

<img width="908" alt="スクリーンショット 2021-02-09 15 54 55" src="https://user-images.githubusercontent.com/50857020/107326749-4eff1500-6aef-11eb-9c2d-9212c48ace11.png">
 
 Select  a device
 * Nexus 5X
 
 <img width="255" alt="スクリーンショット 2021-02-09 16 07 09" src="https://user-images.githubusercontent.com/50857020/107327709-e4e76f80-6af0-11eb-8d93-08f14e522443.png">

# Sample

![アセット 1](https://user-images.githubusercontent.com/50857020/107327559-a94ca580-6af0-11eb-9488-6e87ad3eb4e2.png)





