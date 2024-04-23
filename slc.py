import csv
import time
import gpiozero as gz # type: ignore


class BDD_Entry:
    def __init__(self, N_type, N_index, successor0, successor1):
        self.N_type: str = N_type
        self.N_index: int = N_index
        self.successor0: int = successor0
        self.successor1: int = successor1


class Control_Entry:
    def __init__(self, control, imm_transition):
        self.control: tuple = control  # this is a vector
        self.imm_transition: bool = imm_transition


class Controller:
    def __init__(self, plant, BDDTable, control_memory):
        self.i: int = 0
        self.plant: Car = plant
        self.BDDTable: list[BDD_Entry] = BDDTable
        self.control_memory: list[Control_Entry] = control_memory

    def process_variables(self, y):
        return [
            None,
            y[0],
            y[1],
            y[2] == 0,
            y[2] < 10,
            y[2] < 20,
            y[2] < 30,
            y[3]==1,
            y[3]==2,
            y[3]==3,
            y[3]==4,
            y[3]==0,
        ]

    # SLC state machine driver
    def transition(self, x):
        while True:
            state = 0
            index = self.BDDTable[self.i].N_index

            if self.BDDTable[self.i].N_type == "x":
                if x[index] == 0:
                    self.i = BDDTable[self.i].successor0
                else:
                    self.i = BDDTable[self.i].successor1

            else:
                state = 1
                if control_memory[index].control is not None:
                    self.plant.set_actuator_values(control_memory[index].control)

                self.i = BDDTable[self.i].successor1

            if state and not control_memory[index].imm_transition:
                break


    def control_loop(self):
        while True:
            y = self.plant.get_sensor_values()
            x = self.process_variables(y)
            self.transition(x)
            time.sleep(0.01)


class Car:
    acceleration_rate = 0.025
    deceleration_rate = 0.001
    braking_rate = 0.04
    accelerator_btn = gz.Button(16)
    brake_btn = gz.Button(20)
    gear_led = [gz.LED(6), gz.LED(19), gz.LED(13), gz.LED(26)]
    clutch_led = gz.LED(21)

    def __init__(self):
        self.speed = 0
        self.gear = 0
        self.is_acc_pressed = False
        self.is_brake_pressed = False

    def get_sensor_values(self):
        # read actual sensor values
        self.is_brake_pressed = self.brake_btn.is_pressed # this is not a sensor but we are simulating it
        self.is_acc_pressed = self.accelerator_btn.is_pressed
        return 1, self.is_acc_pressed, self.speed, self.gear

    # simulation
    def set_actuator_values(self, u):
        # set clutch
        if u[0] == 1 and u[1] == 0:
            self.clutch_led.on()
            time.sleep(0.25)
        elif u[0] == 0 and u[1] == 1:
            self.clutch_led.off()

        # set gear
        if u[2] == 1:
            self.gear = u[3]
            #self.gear_led[self.gear-1].on()

        for i in range(4):
            if i == self.gear-1:
                self.gear_led[i].on()
            else:
                self.gear_led[i].off()

        # set speed
        if self.brake_btn.is_pressed:
            self.speed -= self.braking_rate
        elif self.accelerator_btn.is_pressed:
            self.speed += self.acceleration_rate
        else:
            self.speed -= self.deceleration_rate
        self.speed = max(0, self.speed)
        
        print(f"\rGear: {self.gear}. Speed: {self.speed:.2f}", end="", flush=True)


# populate BDD Table
BDDTable: list[BDD_Entry] = []
with open('bdd.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        entry = (row[1], int(row[2]), int(row[3]) if row[3]!="-" else None, int(row[4]))
        BDDTable.append(BDD_Entry(*entry))

# populate control memory
control_memory: list[Control_Entry] = []
with open('control.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:
        entry = (tuple(map(int, row[1:5])), row[5]=="1")
        control_memory.append(Control_Entry(*entry))


car = Car()
controller = Controller(car, BDDTable, control_memory)
controller.control_loop()
