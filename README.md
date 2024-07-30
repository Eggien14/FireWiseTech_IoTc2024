Welcome to Fire_Wise_Tech, We are one of the 18 teams participating in the Final round of the IoT Challenge 2024.
This project was developed by us over a period of 3 months.

Below are some guidelines for developing and building the system:

1. Node
   
   Project support by Siliconlab chip, so you need to install Simplicity Studio
   All nodes must be flashed with the bootloader-uart-xmodem example if you want to interact with the controller
   We use the EFR32xMG24 controller connected to the following sensors: "MQ2: Smoke sensor"; "LM393: Flame sensor"; "2 buttons"; and "1 bell" as the sensor node - End Device.

     + If you want to test the connection between the node and the Gateway, please use the branch Test_connect_node. If the light on the Node turns green, it means       the node is connected.
     + After that, use the main program of the node Full_sensor_node to start sending data.

2. Gateway

   First you need to build Z3Gateway example for Linux using Simplicity Studio
   After that you need to build and flash ncp-uart-hw example to 1 EFR32 to support Zigbee network
   Gateway using python
   Gateway---RaspberryPi4 brach has auto start Gateway
   
3. Appmobile

   Appmobile will take data from Database (we using Firebse)
