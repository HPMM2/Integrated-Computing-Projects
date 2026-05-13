<div align="center">

# 🖥️ Integrated Computing — UANL
![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=white&labelColor=00bcd4&color=0097a7)
![Arduino](https://img.shields.io/badge/Arduino-white?style=flat&logo=arduino&logoColor=white&labelColor=00bcd4&color=0097a7)
![Raspberry Pi](https://img.shields.io/badge/Raspberry_Pi-white?style=flat&logo=raspberrypi&logoColor=white&labelColor=00bcd4&color=0097a7)
![UANL](https://img.shields.io/badge/UANL-white?style=flat&logoColor=white&labelColor=00bcd4&color=0097a7)
![Status](https://img.shields.io/badge/Status-Complete-white?style=flat&logoColor=white&labelColor=00bcd4&color=0097a7)

> ⚠️ Code, comments and documentation are written in Spanish as part of my university coursework.

Collection of lab practices and final project from my Integrated Computing course at UANL, built with Arduino and Raspberry Pi using Python.

</div>

---

## 📁 Contents

### 🔹 Practices

| # | Practice | Hardware | Description |
|---|----------|----------|-------------|
| 01 | **LED Sequencer** | Arduino | Sequential LED animation with start/stop and acceleration buttons, implemented with and without arrays |
| 02 | **Binary Counter** | Raspberry Pi | 8-bit binary counter displayed on 8 LEDs via GPIO, counting from 0 to 255 |
| 03 | **Graphic Volume Controller** | Arduino + Raspberry Pi | Potentiometer-based volume controller mapped to a 7-segment display and LED bar via serial communication |
| 04 | **Alarm System** | Raspberry Pi | PIR motion sensor triggering LED sequences and a buzzer with button controls using `gpiozero` |
| 05 | **Power Supply Indicator** | Arduino + Raspberry Pi | Voltage sensor monitoring power supply level, lighting an LED when voltage is low |
| 06 | **Charge & Temperature Detector** | Arduino + Raspberry Pi | DHT11 temperature sensor with LED indicator triggering when a threshold is exceeded |
| 07 | **RAM & CPU Monitor** | Arduino + Raspberry Pi | `psutil`-based system monitor with LED indicators for CPU and RAM usage, tested with the `stress` tool |

### 🔹 Final Project — PIA

**LED Light Therapy System for Alzheimer's Patients**

A Raspberry Pi-powered WS2812B LED strip therapy system designed to support Alzheimer's treatment through 40Hz light stimulation. The system features a full-screen `tkinter` GUI with an animated logo intro, adjustable light type (warm/natural), intensity levels and a countdown timer.

| Document | Description |
|----------|-------------|
| **Initial Proposal** | Project justification, market analysis and component list |
| **Mid-Course Report** | System design, layout, component specs and future work |
| **Final Report** | Full development log, testing findings, wiring diagram and conclusions |
| **`PROYECTO.py`** | Final source code with WS2812B LED control, tkinter GUI and threading |

---



## 🛠️ Built With

![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=white&labelColor=00bcd4&color=0097a7)
![Arduino](https://img.shields.io/badge/Arduino-white?style=flat&logo=arduino&logoColor=white&labelColor=00bcd4&color=0097a7)
![Raspberry Pi](https://img.shields.io/badge/Raspberry_Pi-white?style=flat&logo=raspberrypi&logoColor=white&labelColor=00bcd4&color=0097a7)

---


## 📄 License

This project is licensed under the [MIT License](./LICENSE).
