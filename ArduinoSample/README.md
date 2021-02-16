# Arduino

## Install Arduino IDE
First, go to https://www.arduino.cc/en/software

![スクリーンショット 2021-02-09 151855](https://user-images.githubusercontent.com/52157596/107323749-2aed0500-6aea-11eb-9e56-1ba9fd5ad7bf.png)

Install Arduino IDE according to your OS.

## Setup Arduino IDE
This environment is based on Arduino IDE version 1.8.8.
Let's set up the Arduino IDE to run the Arduino.

### Set "Additional Boards Manager URLs"
First, go to **File> Preferences** in your Arduino IDE.

![スクリーンショット 2021-02-09 153215](https://user-images.githubusercontent.com/52157596/107324809-03973780-6aec-11eb-8f3b-55697ce53d6a.png)

Enter the URL shown below in the "Additional Boards Manager URLs" field in the yellow section of the above figure.
This URL also depends on the board you are using.

If you are using an ESP8266 board,
`http://arduino.esp8266.com/stable/package_esp8266com_index.json`

If you are using an ESP32 board,
`https://dl.espressif.com/dl/package_esp32_index.json`

When you have finished filling out the "Additional Boards Manager URLs", click the OK button.

### Install Bord
Go to **Tools> Board> Boards Manager** as shown in the following figure.

![スクリーンショット 2021-02-09 155713](https://user-images.githubusercontent.com/52157596/107326865-81107700-6aef-11eb-9019-56fb30720b35.png)

Search and install a board like the one shown below.
This board also depends on the board you are using.

If you are using an ESP8266 board,
`esp8266 by ESP8266 Community`

If you are using an ESP32 board,
`esp32 by Espressif Systems`

![スクリーンショット 2021-02-09 160453](https://user-images.githubusercontent.com/52157596/107327509-94701200-6af0-11eb-907a-df64e8aaacb5.png)


### Configure Bord
Go to **Tools> Board** as shown in the following figure to display the list of boards.

![スクリーンショット 2021-02-09 160904](https://user-images.githubusercontent.com/52157596/107327853-28da7480-6af1-11eb-8dab-60904e218c38.png)

And Select a bord shown below.

If you are using an ESP8266 board,
`Generic ESP8266 Module`

If you are using an ESP32 board,
`ESP32 Dev Module`

And configure the board settings according to the table below.

|    |    |
| ---- | ---- |
|  Flash Mode  |  QIO  |
|  Flash Frequency  |  40MHz  |
|  CPU Frequency  |  80MHz(Wifi/BT)  |
|  Flash Size  |  2MB(16Mb)  |
|  Upload Speed  |  115200  |

### Select the Port
Finally, select and configure the port.
Go to **Tools> Port** as shown in the following figure
This port depends on the board you are using.

![スクリーンショット 2021-02-09 162250](https://user-images.githubusercontent.com/52157596/107329189-29740a80-6af3-11eb-8489-05c13d983166.png)

## execution
Press the button shown in the figure below to write the program to the Arduino and make it work.

![スクリーンショット 2021-02-09 162718](https://user-images.githubusercontent.com/52157596/107329616-bd45d680-6af3-11eb-92b4-e9ee8343bcc1.png)
