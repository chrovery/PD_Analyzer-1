
<details>
<summary><font size=5>Table of Contents</font> </summary>

- [1. Power Deivery Protocol Introduction](#1-power-deivery-protocol-introduction)
- [2. Overview:](#2-overview)
  - [2.1. Hardware](#21-hardware)
  - [2.2. Software](#22-software)
  - [2.3. Firmware](#23-firmware)
- [3. Overview of the GUI](#3-overview-of-the-gui)
  - [3.1. Message View](#31-message-view)
  - [3.2. RawData View](#32-rawdata-view)
- [4. Prototype of the PD Analyzer](#4-prototype-of-the-pd-analyzer)
  - [4.1. PIN Connection](#41-pin-connection)
  - [4.2. Capture PD package data](#42-capture-pd-package-data)
    - [4.2.1 Connection Check](#421-connection-check)
    - [4.2.2 Capture Data](#422-capture-data)
- [5. Firmware HEX](#5-firmware-hex)
- [6. GUI Tool](#6-gui-tool)

</details>

***

# 1. Power Deivery Protocol Introduction
USB has evolved from a data interface capable of supplying limited power to a primary provider of power with a data interface. Today many devices charge or get their power from USB ports contained in laptops, cars, aircraft or even wall sockets. Users need USB to fulfill their requirements not only in terms of data but also to provide power to, or charge, their devices simply, often without the need to load a driver, in order to carry out “traditional” USB functions.   

USB Power Delivery is designed to enable the maximum functionality of USB by providing more flexible power delivery along with data over a single cable. Also it enables alternative modes of operation by providing the mechanisms to discover, enter and exit Alternate Modes. The specification also enables discovery of cable capabilities such as supported speeds and current levels.   

The USB Power Delivery specification defines how USB Devices may negotiate for more current and/or higher or lower voltages over the USB cable (using VBUS or CC wire as the communications channel). And defines mechanisms to discover, enter and exit Modes defined either by a standard or by a particular vendor. And also defines the mechanisms to discover the capabilities of cables which can communicate using Power Delivery.   

Silabs has released the reference design for usb Type-c. Since more and more customers adopt our reference design, it's essential to investigate the Power Delivery specification, and implement a universal Type-C PD Analyzer base on our certified PD library.   

# 2. Overview:

The USB Power Delivery Analyzer (PD analyzer) base on EFM8BB3 can monitor the PD package data on the Control Channel lines CC1 and CC2, and don’t need intrusive the original system. It can aid to analyze the behavior of the whole USB Power Delivery System to promote the development of new USB PD product or troubleshoot the issue of the PD system.   

The system architecture of PD analyzer connectors be illustrated in figure as below. The PD analyzer be connected to analysis computer through a USB-to-Uart Bridge for data transfer. The target device should connect the Analyzer’s type-c receptacle, and the plug of Analyzer should connect to another type-c device, typically, it is a source port.   

<div align="center">
  <img src="files/blockdiagram.jpg">  
</div> 

## 2.1. Hardware
The prototype of the PD Analyzer will be implemented with EFM8BB31F64G STK board.   

## 2.2. Software
The GUI tool be implemented with python + QT which be supposed compatible with major system. And packages the python programs into stand-alone executables with Pyinstaller.   

## 2.3. Firmware
The firmware be implemented base on Silabs' certified PD library   

**Main function of the PD protocol analyzer**

1. PD data import / export / save
2. PD data capture   
* connect / disconnect the analyzer
* run / stop / pause the PD capture, the version1 will support captured data analysis, but not online analysis.
* data buffer size if adjustable, the data will be overwroten if overflow
3. PD data analysis
* can show raw data, decoded from BMC
* show message view data
* show policy layer data
* can mark the data for checking
4. About & Help
* Will provide some user guide for how to use the tool
* The tool is releasable under Silabs' control

# 3. Overview of the GUI
As below is the main perspective of the PD analyzer GUI, it comprises the following elements:
* Menu bar
* A message view window which list all of the captured PD package data.
* A Raw Data view window

## 3.1. Message View
The message view window be consist of a list that displaying all USB protocol elements. The analysis software lists PD package on the left side of the display. Each PD package includes the SOP, Message ID, Number of Data Objects and Message Type information, also the payload and absolute time of each PD package be expressed in the view. And the PD package transfer direction is indicated with an arrow.   

## 3.2. RawData View
The Raw Data View will show more information about the selected power delivery package. In addition to the basic PD package information be provided by Message view, this display view allows the user to check the raw data (5B encoded) of each package, and all of the detailed information will be listed, also a brief description about each control message or data message be added to help the user understand the meaning of the PD package further.   

<div align="center">
  <img src="files/guiView.png">  
</div> 

# 4. Prototype of the PD Analyzer
The USB Power Delivery Analyzer (PD analyzer) device be implemented with EFM8BB3. EFM8BB3 has a Configurable Logic block which be consisted of multiple Configurable Logic Units (CLUs). CLUs are flexible logic functions which may be used for a variety of digital functions, such as replacing system glue logic, aiding in the generation of special waveforms, or synchronizing system event triggers. The USB PD analyzer adopt the CLU as a BMC decoder, the module can decode the BMC code independently of the CPU, has the benefit of reducing the workload of the CPU.   

The PD analyzer device be consisted of three parts, EFM8BB3 STK board, CP210x USB-to-Uart bridge, a Type-C receptacle and plug connector. As below is the top view and bottom view of the PD Analyzer device.   

<div align="center">
  <img src="files/connect_with_efm8bb3.jpg">  
</div> 
<div align="center">
  <img src="files/connect_with_cp210x.jpg">  
</div> 

## 4.1. PIN Connection
The P0.1 of STK board should connect to GND for a reference GND. And P1.1 P1.2 is the input channel of CC pin, please connect them with the Type-c connector's A5 and B5 pin. Also we should connect the P1.7 and P2.0 to the Rx and Tx pin of CP210x for data transaction.   

## 4.2. Capture PD package data
### 4.2.1 Connection Check
Ensure that the PD Analyzer device is connected to the analysis computer and the power is on.   
Launch the PD Analyzer application by double clicking “PD Analyzer.exe”
At the main window, click the Capture -> Connect menu to create the connection between Analyzer device and computer. The Connect menu will become disabled if connection be established, otherwise a warning message window will be popped to info the connection failed. And please reset the analyzer device and try to connect it again.   

### 4.2.2 Capture Data
After ensuring the connection, please start to capture the PD package by clicking the Capture -> Run. And then connect the target Type-c device with the receptacle of the connector, and the plug of the connector should be connected to other Type-c source. For a quick demo, plug the USB Type-C power adapter into the receptacle, and plug the connector into the Macbook.   

The overview of the PD Analyzer be illustrated as below.   

<div align="center">
  <img src="files/prototype.jpg">  
</div> 

# 5. Firmware HEX
Uploaded the PD Analyzer firmware project base on EFM8BB3 as attachement, please just program the the PD_Analyzer.hex to EFM8BB31F64G to make it a PD Analayzer device.   

And then refer to sector "PIN Connection" for how to connect the EFM8BB3 STK and CP210x.   

# 6. GUI Tool
Attachement GUI_Tool.zip is the stand-alone executables GUI tool which can run in the Windows PC without installing.   
