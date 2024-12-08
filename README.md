
# Smart Parking System Using Raspberry Pi

## Team Members:
- **Joshua Mercado**
- **Johnathan Pham**
- **Sukruti Mallesh**
- **Karina Yeager**

---

## Project Overview

Parking on college campuses is a persistent challenge, often resulting in wasted time, fuel, and increased frustration for students and staff. This project aims to solve this issue by developing a **Smart Parking System** that leverages **Raspberry Pi** and sensors to monitor parking spots in real-time. The system improves parking efficiency by providing precise, real-time availability data and directing users to open parking spots through a mobile app or a display screen.

---

## Objectives

- Eliminate the hassle of searching for parking spots by providing **real-time, spot-specific availability data**.
- Improve **traffic flow** and **user experience** on campus.
- Offer a **scalable and cost-effective** solution for campus parking challenges.

---

## Features

### **1. Sensor-Based System for High Accuracy**
- **Individual Spot Sensors:** Each parking spot is equipped with sensors to detect occupancy status (vacant/occupied).
- **Real-Time Data Collection:** Data from all sensors is collected and processed by a Raspberry Pi, keeping track of the availability of all spots in real-time.
- **Detailed Parking Spot Display:** Displays the exact number of available spots on a screen at the parking lot entrance and integrates with a mobile app for remote access.

### **2. Mobile App Integration**
- Users can see a **real-time map of the parking lot** with vacant spots highlighted.
- Directs users to open spots, reducing unnecessary driving.

### **3. Data Analytics**
- Provides detailed usage patterns to optimize parking layouts and monitor peak usage times.

---

## Advantages

- **High Precision:** Monitors individual parking spots, ensuring highly accurate data.
- **User-Friendly:** Users know the exact availability before arriving, saving time.
- **Data-Driven:** Offers insights to improve parking lot management.
- **Scalability:** Adapts easily to multi-level or complex parking structures.

---

## Competitor Comparison

| Feature              | ParkMe         | ParkWhiz      | SmartPark      | **Smart Parking System** |
|----------------------|----------------|---------------|----------------|--------------------------|
| **Real-Time Spot Monitoring** | ✗              | ✗             | ✓              | **✓**                    |
| **Cost-Effectiveness**        | Moderate        | Moderate       | High           | **High**                 |
| **Focus on College Campuses** | ✗              | ✗             | ✗              | **✓**                    |
| **Mobile App Integration**    | ✓              | ✓             | ✓              | **✓**                    |

---

## Hardware Components

- **Raspberry Pi**: Central controller for processing and aggregating sensor data.
- **Ultrasonic Sensors**: Detect parking spot occupancy.
- **LCD Screen**: Displays available spots at the parking lot entrance.
- **Other Components**: Wires, breadboards, resistors, and power supply.

---

## Software Components

### **Python Script**
The system's core logic is written in Python. The script:
- Monitors ultrasonic sensors to detect spot occupancy.
- Calculates distances to determine parking status.
- Displays results on an LCD in real-time.

### **Mobile App**
(Optional) A simple app to visualize parking lot maps and guide users to available spots.

---

## Installation & Usage

1. **Set up the hardware:**
   - Connect ultrasonic sensors to the Raspberry Pi.
   - Connect the LCD screen using I2C.
   - Ensure all wiring matches GPIO pin assignments in the script.

2. **Prepare the Raspberry Pi:**
   - Install required Python libraries:
     ```bash
     sudo pip install RPi.GPIO RPLCD
     ```
   - Verify the I2C address of the LCD using:
     ```bash
     sudo i2cdetect -y 1
     ```

3. **Run the Python Script:**
   - Save the script as `parking_sensor.py`.
   - Execute the script:
     ```bash
     python3 parking_sensor.py
     ```

4. **Test the System:**
   - Verify real-time data on the LCD and adjust the sensor thresholds as needed.

---

## Future Enhancements

- Integration with cloud storage for remote monitoring.
- Enhanced mobile app features, such as push notifications for availability updates.
- Addition of solar panels for a sustainable energy source.

---