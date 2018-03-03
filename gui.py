import bodyControl as rc
import tkinter as tkinter

tk = tkinter.Tk()

has_prev_key_release = None

'''
When holding a key down, multiple key press and key release events are fired in
succession. Debouncing is implemented in order to squash these repeated events
and know when the "real" KeyRelease and KeyPress events happen.
'''

def on_key_release(event):
    global has_prev_key_release
    has_prev_key_release = None

def on_key_press(event):
    pass

def on_key_release_repeat(event, function):
    global has_prev_key_release
    has_prev_key_release = tk.after_idle(on_key_release, event)
    function()
    # print("on_key_release_repeat", repr(event.char))

def on_key_press_repeat(event):
    global has_prev_key_release
    if has_prev_key_release:
        tk.after_cancel(has_prev_key_release)
        has_prev_key_release = None
    else:
        on_key_press(event)

# frame = tkinter.Frame(tk, width=100, height=100)
# frame.bind("<KeyRelease-a>", lambda x: on_key_release_repeat(x, robot.move_head_right))
# frame.bind("<KeyPress-a>", on_key_press_repeat)

# frame.bind("<KeyPress-d>", lambda x: on_key_release_repeat(x, robot.move_head_left))
# frame.bind("<KeyPress-d>", on_key_press_repeat)

# frame.bind("<KeyRelease-s>", lambda x: on_key_release_repeat(x, robot.move_head_down))
# frame.bind("<KeyPress-s>", on_key_press_repeat)

# frame.bind("<KeyRelease-w>", lambda x: on_key_release_repeat(x, robot.move_head_up))
# frame.bind("<KeyPress-w>", on_key_press_repeat)

robot = rc.RobotController()

def foo():
    print("Stuff")


frame = tkinter.Frame(tk, width=100, height=100)
frame.bind("<KeyRelease-a>", lambda x: on_key_release_repeat(x, robot.move_head_left))
frame.bind("<KeyPress-a>", on_key_press_repeat)

frame.bind("<KeyRelease-d>", lambda x: on_key_release_repeat(x, robot.move_head_right))
frame.bind("<KeyPress-d>", on_key_press_repeat)

frame.bind("<KeyRelease-s>", lambda x: on_key_release_repeat(x, robot.move_head_down))
frame.bind("<KeyPress-s>", on_key_press_repeat)

frame.bind("<KeyRelease-w>", lambda x: on_key_release_repeat(x, robot.move_head_up))
frame.bind("<KeyPress-w>", on_key_press_repeat)

frame.bind("<KeyRelease-q>", lambda x: on_key_release_repeat(x, robot.move_waist_left))
frame.bind("<KeyPress-q>", on_key_press_repeat)

frame.bind("<KeyRelease-e>", lambda x: on_key_release_repeat(x, robot.move_waist_right))
frame.bind("<KeyPress-e>", on_key_press_repeat)

frame.bind("<KeyRelease-i>", lambda x: on_key_release_repeat(x, robot.ramp_forward))
frame.bind("<KeyPress-i>", on_key_press_repeat)

frame.bind("<KeyRelease-k>", lambda x: on_key_release_repeat(x, robot.ramp_backward))
frame.bind("<KeyPress-k>", on_key_press_repeat)

frame.bind("<KeyRelease-l>", lambda x: on_key_release_repeat(x, robot.turn_coutnerClockWise))
frame.bind("<KeyPress-l>", on_key_press_repeat)

frame.bind("<KeyRelease-j>", lambda x: on_key_release_repeat(x, robot.turn_clockwise))
frame.bind("<KeyPress-j>", on_key_press_repeat)

frame.bind("<KeyRelease-space>", lambda x: on_key_release_repeat(x, robot.stop_moving))
frame.bind("<KeyPress-space>", on_key_press_repeat)

frame.pack()
frame.focus_set()

tk.mainloop()
