# Automated Gear Transmission System

This project aims to design a Cyber-Physical System (CPS) that automates the gear transmission in fuel-based automotive cars.

## Problem Statement

In fuel-based automotive cars, power from the engine is delivered to wheels through gears. When the vehicle is at lower speeds, an appropriate lower gear needs to be engaged; for higher speeds an appropriate higher gear needs to be engaged. While a gear is engaged/disengaged clutch is activated.

You need to design a CPS that automates this gear transmission in accordance with the speed requirement/accelerator-pedal-position/brake requested by the driver in the car. Reverse gear engagement is not required to be automated. The driver after engine ignition, activates this system. The speed of the car is controlled by the driver via accelerator and brake. While a gear is engaged/disengaged, clutch is activated. Furthermore, on reaching threshold speed the transmission to higher or lower gears are triggered, respectively, if accelerator or brake is engaged.

Here is the gear to speed mapping specification:
- Speed in (0,10] : Gear 1
- Speed in (10,20] : Gear 2
- Speed in (20,30] : Gear 3
- Speed greater than 30 : Gear 4

## System Requirements

This system is designed to run on a Raspberry Pi.

## Usage

This system is designed to be easy to use. Here are the steps to get it running:

1. **Connect the GPIO Pins**: Connect the necessary peripherals to the GPIO pins on the Raspberry Pi.
2. **Modify the Code**: If necessary, modify the GPIO pin assignments in the code to match your setup. This should be a trivial task if you are familiar with the Raspberry Pi's GPIO layout.\
3. **File Transfer**: Transfer the `slc.py`, `bdd.csv`, and `control.csv` files to your Raspberry Pi.
4. **Run the Code**: You can then run the script using the following command in the terminal:
    ```sh
    python3 slc.py
    ```

### Understanding the system
For a detailed understanding of the system's operation, refer to the `slides.pdf` file, which contains state diagrams.

### Configuration files
- `bdd.csv`: Binary Decision Diagram (BDD) table
- `control.csv`: control signals

## Demo
https://github.com/gjain-7/Gear-Transmission-System/assets/72644006/2539843f-c446-409f-a20a-b3537ea253b8

## Project Submission

This project is submitted as part of the coursework for _Cyber Physical Systems (CS 426)_. It is a collaborative effort between the following team members:

- Gaurav Jain - [@gjain-7](https://github.com/gjain-7)
- R. Navya Harshitha - [@NavyaHarshitha](https://github.com/NavyaHarshitha)
