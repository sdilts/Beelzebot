import tkinter as tk

class CommandSettings:
    def __init__(self, img):
        self.img = img




class MotorSettings(CommandSettings):

    def __init__(self,function_to_call,speed, wait, img, maxSpeed=3):
        CommandSettings.__init__(self,img)
        self.function_to_call = function_to_call
        self.wait = wait
        self.speed = speed
        self.maxSpeed = maxSpeed
        self.opt_frame = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "(Function: {}, Wait: {}, speed: {})".format(self.function_to_call, self.wait, self.speed)

    def draw_settings(self, parent_frame):
        if (self.opt_frame == None):
            self.opt_frame = tk.Frame(parent_frame)
            waitLabel = tk.Label(self.opt_frame, text="Wait time (ms):")
            waitEntry = tk.Spinbox(self.opt_frame)

            waitLabel.grid(row=0,column=0)
            waitEntry.grid(row=0,column=1)

            speedLabel = tk.Label(self.opt_frame, text="Speed:")
            speedEntry = tk.Scale(self.opt_frame, orient=tk.HORIZONTAL, from_=1, to=self.maxSpeed)
            speedLabel.grid(row=1,column=0)
            speedEntry.grid(row=1,column=1)
        return self.opt_frame

    def verify_new_settings(new_settings):
        pass

class ServoSettings(CommandSettings):

    # repeats are the number of times the command is exectued.
    # for example, the command is always something like "Move one posistion to the right"
    def __init__(self, function_to_call, repeats, img, maxRepeats=3):
        CommandSettings.__init__(self,img)
        self.function_to_call = function_to_call
        self.repeats = repeats
        self.opt_frame = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "(Function: {}, Repeats: {})".format(self.function_to_call, self.repeats)

    def verify_new_settings(new_settings):
        return True
