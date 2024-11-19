---
title: Arduino OpenCM9.04 SDK ID Change
tags:
- arduino
- dynamixel
- opencm
- xl320
summary: ""
---

## Intro

This code can be used to change the id of an XL-320 servo from 1 to 2.


```c
/*
  Motor : XL320

  DEVICENAME "1" -> Serial1
  DEVICENAME "2" -> Serial2
  DEVICENAME "3" -> Serial3
*/

#include <DynamixelSDK.h>

#define PROTOCOL_VERSION                2.0                

#define DXL_ID                          1                  
#define BAUDRATE                        1000000
#define DEVICENAME                      "1"                


void setup() {
  Serial.begin(115200);
  while(!Serial);

  Serial.println("Start..");

  dynamixel::PortHandler *portHandler = dynamixel::PortHandler::getPortHandler(DEVICENAME);
  dynamixel::PacketHandler *packetHandler = dynamixel::PacketHandler::getPacketHandler(PROTOCOL_VERSION);

  int index = 0;
  int dxl_comm_result = COMM_TX_FAIL;             

  uint8_t dxl_error = 0;
  uint8_t my_id;

  if (portHandler->openPort())
  {
    Serial.print("Succeeded to open the port!\n");
  }
  else
  {
    Serial.print("Failed to open the port!\n");
    Serial.print("Press any key to terminate...\n");
    return;
  }

  if (portHandler->setBaudRate(BAUDRATE))
  {
    Serial.print("Succeeded to change the baudrate!\n");
  }
  else
  {
    Serial.print("Failed to change the baudrate!\n");
    Serial.print("Press any key to terminate...\n");
    return;
  }

      dxl_comm_result = packetHandler->read1ByteTxRx(portHandler, DXL_ID, 3, &my_id);
      if (dxl_comm_result != COMM_SUCCESS)
      {
        packetHandler->getTxRxResult(dxl_comm_result);
      }
      else if (dxl_error != 0)
      {
        packetHandler->getRxPacketError(dxl_error);
      }

      Serial.print("[ID:");      Serial.print(DXL_ID);
      Serial.print(" GoalPos:"); Serial.print(dxl_goal_position[index]);
      Serial.print(" ID:");  Serial.print(my_id);
      Serial.println(" ");


    Serial.print("Press 'c' key to continue!\n");
    while(Serial.available()==0);

    int ch;

    ch = Serial.read();
    if (ch == 'c')
    {
        my_id=2;

        dxl_comm_result = packetHandler->write1ByteTxRx(portHandler, DXL_ID, 3, my_id, &dxl_error);
        if (dxl_comm_result != COMM_SUCCESS)
        {
            packetHandler->getTxRxResult(dxl_comm_result);
        }
        else if (dxl_error != 0)
        {
            packetHandler->getRxPacketError(dxl_error);
        }

    }

  portHandler->closePort();

}

void loop() {
}
```