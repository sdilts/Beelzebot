from tkinter import *
from tkinter import font
from bodyControl import *
from PIL import ImageTk
from MotorSettings import *

def foo():
    print( "I'm a dummy function!")

class RoboWindow(Frame):

    command_list = []
    cur_selected_indx = 0

    def __init__(self, master=None):
        Frame.__init__(self, master, width=500)
        self.master = master
        self.controller = RobotController()
        self.load_images()
        self.init_gui()

    def load_images(self):
        self.waist_img_left = ImageTk.PhotoImage(file="./robot images/waist_left.png")
        self.waist_img_right =ImageTk.PhotoImage(file="./robot images/waist_right.png")

        self.img_waist_left_small  = ImageTk.PhotoImage(file="./robot images/waist_left_small.png")
        self.img_waist_right_small = ImageTk.PhotoImage(file="./robot images/waist_right_small.png")

        self.img_look_up = ImageTk.PhotoImage(file="./robot images/look_up.png")
        self.img_look_down = ImageTk.PhotoImage(file="./robot images/look_down.png")
        self.img_look_left = ImageTk.PhotoImage(file="./robot images/look_left.png")
        self.img_look_right = ImageTk.PhotoImage(file="./robot images/look_right.png")
        self.img_move_forward = ImageTk.PhotoImage(file="./robot images/up.png")
        self.img_move_backward = ImageTk.PhotoImage(file="./robot images/down.png")
        self.img_turn_right = ImageTk.PhotoImage(file="./robot images/right.png")
        self.img_turn_left = ImageTk.PhotoImage(file="./robot images/left.png")
        self.img_wait = ImageTk.PhotoImage(file="./robot images/wait_large.png")

        self.img_trash = ImageTk.PhotoImage(file="./robot images/trash.png")
        self.img_play  = ImageTk.PhotoImage(file="./robot images/play.png")

        self.img_command = ImageTk.PhotoImage(file="./robot images/demonic_deeds.png")

    def init_gui(self):
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(size=24)
        self.master.option_add('*Font', default_font)
        self.master.title("Robot!")
        self.pack(fill=BOTH, expand=1)

        self.control_frame = Frame(self)

        # stuff for the entry_frame:
        self.waist_frame = Frame(self.control_frame)
        self.waist_left =  Button(self.waist_frame, text="waist left", image=self.waist_img_left,
                                  command = lambda: self.command_btn_pressed(ServoSettings(self.controller.move_waist_left, 1, self.img_waist_left_small, 3)))
        self.waist_right = Button(self.waist_frame, text="waist right", image=self.waist_img_right,
                                  command = lambda: self.command_btn_pressed(ServoSettings(self.controller.move_waist_right, 1, self.img_waist_right_small, 3)))

        self.waist_left.grid(row=0, column=0)
        self.waist_right.grid(row=0, column=1)



        self.look_frame = Frame(self.control_frame)
        self.look_up =    Button(self.look_frame, text="look up",
                                 image=self.img_look_up,
                                 command = lambda: self.command_btn_pressed(ServoSettings(self.controller.move_head_up, 1, self.img_look_up )))
        self.look_down =  Button(self.look_frame, text="look down",
                                 image=self.img_look_down,
                                 command = lambda: self.command_btn_pressed(ServoSettings(self.controller.move_head_down, 1, self.img_look_down )))
        self.look_left =  Button(self.look_frame, text="look left",
                                 image=self.img_look_left,
                                 command = lambda: self.command_btn_pressed(ServoSettings(self.controller.move_head_left, 1, self.img_look_left)))
        self.look_right = Button(self.look_frame, text="look right",
                                 image=self.img_look_right,
                                 command = lambda: self.command_btn_pressed(ServoSettings(self.controller.move_head_right, 1, self.img_look_right)))


        self.look_up.grid(row=0, column=1)
        self.look_down.grid(row=2, column=1)
        self.look_left.grid(row=1, column=0)
        self.look_right.grid(row=1, column=3)


        self.move_frame = Frame(self.control_frame)
        self.move_forward  = Button(self.move_frame, text="forward",
                                    image=self.img_move_forward,
                                    command = lambda: self.command_btn_pressed(MotorSettings(self.controller.setSpeed, 1, self.img_move_forward )))
        self.move_backward = Button(self.move_frame, text="backward",
                                    image=self.img_move_backward,
                                    command = lambda: self.command_btn_pressed(MotorSettings(self.controller.setSpeed, 1, self.img_move_backward )))
        self.turn_left     = Button(self.move_frame, text="turn left",
                                    image=self.img_turn_left,
                                    command = lambda: self.command_btn_pressed(MotorSettings(self.controller.setSpeed, 1, self.img_turn_left, maxSpeed=1)))
        self.turn_right    = Button(self.move_frame, text="turn right",
                                    image=self.img_turn_right,
                                    command = lambda: self.command_btn_pressed(MotorSettings(self.controller.setSpeed, 1, self.img_turn_right, maxSpeed=1 )))


        self.move_forward.grid(row=0, column=1)
        self.move_backward.grid(row=2, column=1)
        self.turn_left.grid(row=1, column=0)
        self.turn_right.grid(row=1, column=3)


        self.waist_frame.grid(row=0, column=0)
        self.look_frame.grid(row=0, column=1)
        self.move_frame.grid(row=0, column=2)

        self.wait_button = Button(self.control_frame, text="Wait!",
                                  image=self.img_wait,
                                  command = lambda: self.command_btn_pressed(WaitSettings(foo, 1, self.img_wait)))
        self.wait_button.grid(row=0, column=3)

        self.control_frame.pack()

        # stuff for the programming frame:
        self.programming_frame = Frame(self,height=200)
        self.programming_label = Label(self.programming_frame, text="Commands:", image=self.img_command)
        self.programming_label.grid(row=0)
        self.command_q_frame = Frame(self.programming_frame, height=75,width=600,  bg="white")
        self.command_q_frame.grid(row=1)

        self.programming_frame.pack()


        self.settings_frame = Frame(self)

        self.trash_button = Button(self.settings_frame, text="Trash", image=self.img_trash)
        self.trash_button.grid(row=1, column=0, padx=50)

        self.entry_label = Label(self.settings_frame, text="Command Options")
        self.entry_label.grid(row=0, column=1)

        self.entry_frame = Frame(self.settings_frame, width=500, height=100)
        self.entry_frame.grid(row=1, column=1)

        self.go_button = Button(self.settings_frame, text="Play!", image=self.img_play)
        self.go_button.grid(row=1, column=2)

        self.settings_frame.pack()



    def command_btn_pressed(self,newCommand):
        if len(self.command_list) == 0:
            self.command_list.insert(self.cur_selected_indx, newCommand)
            self.selectButton(self.cur_selected_indx)
        else:
            self.command_list.insert(self.cur_selected_indx+1, newCommand)
            self.selectButton(self.cur_selected_indx+1)


    def selectButton(self, index):
        if index != self.cur_selected_indx or len(self.command_list) == 1:
            self.cur_selected_indx = index;
            self.draw_command_q(self.cur_selected_indx)
            self.draw_entry_window(self.command_list[self.cur_selected_indx])

    def draw_entry_window(self,motor_command):
        # figure out what we need to draw based off what is in the object:
        window = self.entry_frame
        old_frames = window.winfo_children()
        for old in old_frames:
            old.pack_forget()
        inner = motor_command.draw_settings(window)
        window.width = 400
        inner.pack()
        pass

    def draw_command_q(self, toHighlight):
        old_buttons = self.command_q_frame.winfo_children()
        for btn in old_buttons:
            btn.destroy()
        for (indx, cmd) in enumerate(self.command_list):
            if indx == toHighlight:
                newBtn = Button(self.command_q_frame, text=str(indx),
                                bd=4, relief=SUNKEN, image=cmd.img,
                                command= lambda i=indx: self.selectButton(i))
            else:
                newBtn = Button(self.command_q_frame, text=str(indx),
                                image=cmd.img,
                                command= lambda i=indx: self.selectButton(i))
            newBtn.grid(row=0, column=indx)
        self.command_q_frame.grid(row=1)

def main():
    root = Tk()
    f = RoboWindow(root)
    root.mainloop()


main()
