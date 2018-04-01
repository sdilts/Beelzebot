import tkinter as tk
from tkinter.font import Font


class CommandSettings:
    def __init__(self, img):
        self.img = img
        self.frame_width = 100

    def gen_command(self):
        pass


def foo(phrase):
    print(phrase)

class TalkSettings(CommandSettings):
    def __init__(self, img, root):
        CommandSettings.__init__(self, img)
        self.function_to_call = foo
        self.opt_frame = None
        self.root = root
        self.tkvar = None

    def gen_command(self):
        print("Command: ", self.function_to_call)
        return lambda: self.function_to_call(self.tkvar.get())

    def draw_settings(self, parent_frame):
        if(self.opt_frame == None):
            self.opt_frame = tk.Frame(parent_frame, width = self.frame_width)
            talkLabel = tk.Label(self.opt_frame, text="Say:")
            options = [
                "It's a cold day in hell", 
                "Go to Heaven for the climate, Hell for the company",
                "Maybe this world is another planet's Hell",
                "If you live long enough, something will kill you",
                "Death and taxes are inevitable",
                "Would you like to strike a deal?"
                ]
            self.tkvar = tk.StringVar(self.root)
            self.tkvar.set(options[5])
            self.popupMenu = tk.OptionMenu(self.opt_frame, self.tkvar, *options)
            talkLabel.grid(row=1, column=0)
            self.popupMenu.grid(row=2, column = 0)
        return self.opt_frame

class WaitSettings(CommandSettings):

    def __init__(self, function_to_call, wait_time, img, maxWait=100):
        CommandSettings.__init__(self, img)
        self.function_to_call = function_to_call
        self.opt_frame = None
        self.wait_time = wait_time
        self.maxWait=100

    def gen_command(self):
        print("Command: ", self.function_to_call, "wait: ", self.waitEntry.get())
        return lambda: self.function_to_call(float(self.waitEntry.get()))

    def draw_settings(self, parent_frame):
        if (self.opt_frame == None):
            self.opt_frame = tk.Frame(parent_frame, width=self.frame_width)

            waitLabel = tk.Label(self.opt_frame, text="Wait Time:")
            self.waitEntry = tk.Spinbox(self.opt_frame, from_=.25, to=self.maxWait,
                                        increment=.25, width=4,
                                        format='%.2f', font = Font(family = 'Helvetica', size = 36))
            waitLabel.grid(row=1,column=0)
            self.waitEntry.grid(row=1,column=1)
        return self.opt_frame

class StopSettings(CommandSettings):

    def __init__(self, function_to_call, wait_time, img, maxWait=100):
        CommandSettings.__init__(self, img)
        self.function_to_call = function_to_call
        self.opt_frame = None
        self.wait_time = wait_time
        self.maxWait=100

    def gen_command(self):
        print("Command: ", self.function_to_call, "stop or turn")
        return lambda: self.function_to_call()

    def draw_settings(self, parent_frame):
        if (self.opt_frame == None):
            self.opt_frame = tk.Frame(parent_frame, width=self.frame_width)
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


    def gen_command(self):
        print("Command: ", self.function_to_call, "Speed: ", self.speedEntry.get())
        return lambda: self.function_to_call(self.speedEntry.get())

    def draw_settings(self, parent_frame):
        if (self.opt_frame == None):
            self.opt_frame = tk.Frame(parent_frame, width=self.frame_width)

            speedLabel = tk.Label(self.opt_frame, text="Speed:")
            self.speedEntry = tk.Scale(self.opt_frame, orient=tk.HORIZONTAL,
                                       from_=1, to=self.maxSpeed, width=20)
            self.speedEntry.set(self.speed)
            speedLabel.grid(row=1,column=0)
            self.speedEntry.grid(row=1,column=1)
        return self.opt_frame

class ServoSettings(CommandSettings):

    # repeats are the number of times the command is exectued.
    # for example, the command is always something like "Move one posistion to the right"
    def __init__(self, function_to_call, repeats, img, maxRepeats=4):
        CommandSettings.__init__(self,img)
        self.function_to_call = function_to_call
        self.repeats = repeats
        self.maxRepeats = maxRepeats
        self.opt_frame = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "(Function: {}, Repeats: {})".format(self.function_to_call, self.repeats)

    def gen_command(self):
        repeat_num = self.repeatEntry.get()
        print("Command: ", self.function_to_call, "Repeats: ", self.repeatEntry.get())
        def do_stuff():
            self.function_to_call()
            for i in range(repeat_num):
                self.function_to_call()
        return do_stuff


    def draw_settings(self, parent_frame):
        if (self.opt_frame == None):
            self.opt_frame = tk.Frame(parent_frame,width=self.frame_width)

            repeatLabel = tk.Label(self.opt_frame, text="Repeats:")
            self.repeatEntry = tk.Scale(self.opt_frame, orient=tk.HORIZONTAL, from_=0, to=self.maxRepeats, width=20)
            self.repeatEntry.set(self.repeats)
            repeatLabel.grid(row=1,column=0)
            self.repeatEntry.grid(row=1,column=1)
        return self.opt_frame
