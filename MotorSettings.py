import tkinter as tk

class CommandSettings:
    def __init__(self, img):
        self.img = img

class WaitSettings(CommandSettings):

    def __init__(self, function_to_call, wait_time, img, maxWait=100):
        CommandSettings.__init__(self, img)
        self.opt_frame = None
        self.wait_time = wait_time
        self.maxWait=100


    def draw_settings(self, parent_frame):
        if (self.opt_frame == None):
            self.opt_frame = tk.Frame(parent_frame)

            waitLabel = tk.Label(self.opt_frame, text="Wait Time:")
            waitEntry = tk.Spinbox(self.opt_frame, from_=1, to=self.maxWait)
            waitLabel.grid(row=1,column=0)
            waitEntry.grid(row=1,column=1)
        return self.opt_frame


class MotorSettings(CommandSettings):

    def __init__(self,function_to_call,speed, img, maxSpeed=3):
        CommandSettings.__init__(self,img)
        self.function_to_call = function_to_call
        self.speed = speed
        self.maxSpeed = maxSpeed
        self.opt_frame = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "(Function: {}, speed: {})".format(self.function_to_call, self.speed)

    def draw_settings(self, parent_frame):
        if (self.opt_frame == None):
            self.opt_frame = tk.Frame(parent_frame)

            speedLabel = tk.Label(self.opt_frame, text="Speed:")
            speedEntry = tk.Scale(self.opt_frame, orient=tk.HORIZONTAL, from_=1, to=self.maxSpeed)
            speedEntry.set(self.speed)
            speedLabel.grid(row=1,column=0)
            speedEntry.grid(row=1,column=1)
        return self.opt_frame

    def verify_new_settings(new_settings):
        pass

class ServoSettings(CommandSettings):

    # repeats are the number of times the command is exectued.
    # for example, the command is always something like "Move one posistion to the right"
    def __init__(self, function_to_call, repeats, img, maxRepeats=5):
        CommandSettings.__init__(self,img)
        self.function_to_call = function_to_call
        self.repeats = repeats
        self.maxRepeats = maxRepeats
        self.opt_frame = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "(Function: {}, Repeats: {})".format(self.function_to_call, self.repeats)

    def draw_settings(self, parent_frame):
        if (self.opt_frame == None):
            self.opt_frame = tk.Frame(parent_frame)

            repeatLabel = tk.Label(self.opt_frame, text="Repeats:")
            repeatEntry = tk.Scale(self.opt_frame, orient=tk.HORIZONTAL, from_=1, to=self.maxRepeats)
            repeatEntry.set(self.repeats)
            repeatLabel.grid(row=1,column=0)
            repeatEntry.grid(row=1,column=1)
        return self.opt_frame

    def verify_new_settings(new_settings):
        return True
