import time
import threading
import _thread
import robotAnimation as ra
from tkinter import *
from tkinter import font
from bodyControl import *
from PIL import ImageTk
from MotorSettings import *

def wait(sleep_time):
    time.sleep(sleep_time)

class RoboWindow(Frame):

    command_list = []
    cur_selected_indx = 0

    def __init__(self, master=None):
        Frame.__init__(self, master, width=500)
        self.master = master
        self.controller = RobotController()
        self.load_images()
        self.init_gui()
        self.face_frame = ra.DrawingStuff(self)
        pad = 3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)

    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

    def start_face(self):
        self.face_frame.pack()
        self.face_frame.changeFlag()
        thread = threading.Thread(target=self.face_frame.make_face)
        thread.start()
        return thread



    def load_images(self):
        self.waist_img_left = ImageTk.PhotoImage(file="./robot images/waist_right.png")
        self.waist_img_right =ImageTk.PhotoImage(file="./robot images/waist_left.png")

        self.img_waist_left_small  = ImageTk.PhotoImage(file="./robot images/waist_right_small.png")
        self.img_waist_right_small = ImageTk.PhotoImage(file="./robot images/waist_left_small.png")

        self.img_look_up = ImageTk.PhotoImage(file="./robot images/look_up.png")
        self.img_look_down = ImageTk.PhotoImage(file="./robot images/look_down.png")
        self.img_look_left = ImageTk.PhotoImage(file="./robot images/look_right.png")
        self.img_look_right = ImageTk.PhotoImage(file="./robot images/look_left.png")
        self.img_move_backward = ImageTk.PhotoImage(file="./robot images/up.png")
        self.img_move_forward = ImageTk.PhotoImage(file="./robot images/down.png")
        self.img_turn_left = ImageTk.PhotoImage(file="./robot images/right.png")
        self.img_turn_right = ImageTk.PhotoImage(file="./robot images/left.png")
        self.img_wait = ImageTk.PhotoImage(file="./robot images/wait_large.png")
        self.img_stop = ImageTk.PhotoImage(file = "./robot images/stop.png")	

        self.img_trash = ImageTk.PhotoImage(file="./robot images/trash.png")
        self.img_play  = ImageTk.PhotoImage(file="./robot images/play.png")

        self.img_command = ImageTk.PhotoImage(file="./robot images/demonic_deeds.png")

    def init_gui(self):
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(size=12)
        self.master.option_add('*Font', default_font)
        self.master.title("Robot!")
        self.pack(fill=BOTH, expand=1)
        self.input_frame = Frame(self)
        self.input_frame.pack()

        self.control_frame = Frame(self.input_frame)

        # stuff for the entry_frame:
        self.waist_frame = Frame(self.control_frame)
        self.waist_left =  Button(self.waist_frame, text="waist left", image=self.waist_img_left,
                                  command = lambda: self.command_btn_pressed(ServoSettings(self.controller.move_waist_left, 0, self.img_waist_left_small, 3)))
        self.waist_right = Button(self.waist_frame, text="waist right", image=self.waist_img_right,
                                  command = lambda: self.command_btn_pressed(ServoSettings(self.controller.move_waist_right, 0, self.img_waist_right_small, 3)))

        self.waist_right.grid(row=0, column=0)
        self.waist_left.grid(row=0, column=1)



        self.look_frame = Frame(self.control_frame)
        self.look_up =    Button(self.look_frame, text="look up",
                                 image=self.img_look_up,
                                 command = lambda: self.command_btn_pressed(ServoSettings(self.controller.move_head_up, 0, self.img_look_up )))
        self.look_down =  Button(self.look_frame, text="look down",
                                 image=self.img_look_down,
                                 command = lambda: self.command_btn_pressed(ServoSettings(self.controller.move_head_down, 0, self.img_look_down )))
        self.look_left =  Button(self.look_frame, text="look left",
                                 image=self.img_look_left,
                                 command = lambda: self.command_btn_pressed(ServoSettings(self.controller.move_head_left, 0, self.img_look_left)))
        self.look_right = Button(self.look_frame, text="look right",
                                 image=self.img_look_right,
                                 command = lambda: self.command_btn_pressed(ServoSettings(self.controller.move_head_right, 0, self.img_look_right)))


        self.look_up.grid(row=0, column=1)
        self.look_down.grid(row=1, column=1)
        self.look_right.grid(row=1, column=0)
        self.look_left.grid(row=1, column=3)
        #self.look_frame.pack(padx=10)

        self.move_frame = Frame(self.control_frame)
        self.move_forward  = Button(self.move_frame, text="forward",
                                    image=self.img_move_forward,
                                    command = lambda: self.command_btn_pressed(MotorSettings(self.controller.setSpeed, 1, self.img_move_forward )))
        self.move_backward = Button(self.move_frame, text="backward",
                                    image=self.img_move_backward,
                                    command = lambda: self.command_btn_pressed(MotorSettings(self.controller.move_backwards, 1, self.img_move_backward )))
        self.turn_left     = Button(self.move_frame, text="turn left",
                                    image=self.img_turn_left,
                                    command = lambda: self.command_btn_pressed(StopSettings(self.controller.turn_clockwise, 1, self.img_turn_left)))
        self.turn_right    = Button(self.move_frame, text="turn right",
                                    image=self.img_turn_right,
                                    command = lambda: self.command_btn_pressed(StopSettings(self.controller.turn_counterClockWise, 1, self.img_turn_right)))


        self.move_backward.grid(row=0, column=1)
        self.move_forward.grid(row=1, column=1)
        self.turn_right.grid(row=1, column=0)
        self.turn_left.grid(row=1, column=3)


        self.waist_frame.grid(row=0, column=0)
        self.look_frame.grid(row=0, column=1)
        self.move_frame.grid(row=0, column=2)

        self.wait_button = Button(self.control_frame, text="Wait!",
                                  image=self.img_wait,
                                  command = lambda: self.command_btn_pressed(WaitSettings(wait, 1, self.img_wait)))
        self.wait_button.grid(row=0, column=3)
        self.stop_button = Button(self.control_frame, text = "Stop!", image=self.img_stop, command = lambda:self.command_btn_pressed(StopSettings(self.controller.stop_moving, 1, self.img_stop)))
        #self.wait_button.pack(padx = 10)
        self.stop_button.grid(row = 1, column = 3)
        self.control_frame.pack(pady=5)

        # stuff for the programming frame:
        self.programming_frame = Frame(self.input_frame,height=200)
        self.programming_label = Label(self.programming_frame, text="Commands:", image=self.img_command)
        self.programming_label.grid(row=0)
        self.command_q_frame = Frame(self.programming_frame, height=75,width=400)
        self.command_q_frame.grid(row=1)

        self.programming_frame.pack(pady=5)


        self.settings_frame = Frame(self.input_frame)

        self.trash_button = Button(self.settings_frame, text="Trash", image=self.img_trash, command=self.trashButton)
        self.trash_button.grid(row=1, column=0, padx=50)

        self.entry_label = Label(self.settings_frame, text="Command Options")
        self.entry_label.grid(row=0, column=1)

        self.entry_frame = Frame(self.settings_frame, width=400, height=100)
        self.entry_frame.pack_propagate(False)
        self.entry_frame.grid(row=1, column=1)

        self.go_button = Button(self.settings_frame, text="Play!", image=self.img_play, command=self.play)
        self.go_button.grid(row=1, column=2)

        self.settings_frame.pack(pady=5)


    def play(self):
        commands = self.command_seq_gen()

        def run_commands(callback_func):
            print("\n\nCommands:")
            self.controller.reset_pos()
            for cmd in commands:
                print("Running: ", cmd)
                cmd()
            self.controller.stop_moving()
            callback_func()

        def restore_config(thread):
            self.face_frame.pack_forget()
            self.face_frame.changeFlag()
            thread.join()
            self.input_frame.pack()

        self.input_frame.pack_forget()
        thread = self.start_face()
        _thread.start_new_thread(run_commands,tuple([lambda: restore_config(thread)]))

        print("Thread: ", thread)

    def command_seq_gen(self):
        command_seq = []
        for cmd in self.command_list:
            command_seq.append(cmd.gen_command())
        return command_seq

    def command_btn_pressed(self,newCommand):
        if len(self.command_list) == 0:
            self.command_list.insert(self.cur_selected_indx, newCommand)
            self.selectButton(self.cur_selected_indx)
        else:
            self.command_list.insert(self.cur_selected_indx+1, newCommand)
            self.selectButton(self.cur_selected_indx+1)

    def selectButton(self, index, force=False):
        if index != self.cur_selected_indx or len(self.command_list) == 1 or force:
            if index < len(self.command_list):
                self.cur_selected_indx = index;
                self.draw_entry_window(self.command_list[index])
            else:
                window = self.entry_frame
                old_frames = window.winfo_children()
                for old in old_frames:
                    old.pack_forget()
            self.draw_command_q(index)

    def trashButton(self):
        if len(self.command_list) > 0:
            del self.command_list[self.cur_selected_indx]
            if self.cur_selected_indx > 0:
                self.selectButton(self.cur_selected_indx-1)
            else:
                self.selectButton(0, force=True)

    def draw_entry_window(self,motor_command):
        # figure out what we need to draw based off what is in the object:
        window = self.entry_frame
        old_frames = window.winfo_children()
        for old in old_frames:
            old.pack_forget()
        inner = motor_command.draw_settings(window)
        window.width = 400
        inner.pack()

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

def showAndTellAdventures(paint):
    for i in range(150):
        print("**" + i)
    paint.hide()
    time.sleep(2)
    paint.show()
    time.sleep(2)
    paint.hide()

def main():
    root = Tk()
    f = RoboWindow(root)
    root.mainloop()


main()
