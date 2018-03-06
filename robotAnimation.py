import tkinter as tk
import _thread
import time

class DrawingStuff(tk.Frame):
    def __init__(self, r, c=None):
        tk.Frame.__init__(self,r)
        self.screen_width = 640
        self.screen_height = 480

        self.head_x = 100
        self.head_y = 50
        self.head_width = 440
        self.head_height = 180

        self.mouth_width = 75
        self.mouth_x = self.head_x+(self.head_width/2) - (self.mouth_width/2)
        self.mouth_y = self.head_y+ (self.head_height *1.5)


        self.eye_r = 100
        self.eye_x = self.head_x + self.eye_r+10
        self.eye_y = self.head_y + self.eye_r+10
        self.pupil_r = 20

        self.distance = (self.eye_r*2)+(self.head_width -(self.eye_r*4)-20)

        self.step_x = 1
        self.step_y = 1


        self.client = c
        self.root = r
        self.flag = False
        self.speed = .001
        #self.canvasW = 800
        #self.canvasH = 410
        self.canvas = tk.Canvas(self, width =self.screen_width, height=self.screen_height)
        self.canvas.pack()

    def eye(self, x, y, r, tag_name, color):
        # form a bounding square using center (x,y) and radius r
        # upper left corner (ulc) and lower right corner (lrc) coordinates of square
        ulc = x-r, y-r
        lrc = x+r, y+r
        # give the circle a tag name for reference
        self.canvas.create_oval(ulc, lrc, tag=tag_name,width = 0, fill=color)

    def make_face(self):
        #root = tk.Tk()
        #canvas = tk.Canvas(root, self.width = self.screen_width, self.height = self.screen_height)
        #canvas.grid(row = 0, column = 0)
        i = 0
        j = 0

        aflag = False
        bflag = False
        #head
        self.canvas.create_rectangle(self.head_x, self.head_y, self.head_x+self.head_width, self.head_y+self.head_height,width = 0, fill = 'red')
        self.canvas.create_rectangle(self.head_x-60, self.head_y+50, self.head_x, self.head_y+20,width = 0, fill = 'orange')
        self.canvas.create_rectangle(self.head_x+self.head_width, self.head_y+50, self.head_x+self.head_width+60, self.head_y+20,width = 0, fill = 'orange')
        self.canvas.create_rectangle(self.head_x-60, self.head_y+50, self.head_x-30, self.head_y-10,width = 0, fill = 'orange')
        self.canvas.create_rectangle(self.head_x+self.head_width+30, self.head_y+50, self.head_x+self.head_width+60, self.head_y-10,width = 0, fill = 'orange')

        self.canvas.create_polygon(self.head_x-60, self.head_y-10, self.head_x-30, self.head_y-40,
                                  self.head_x-30, self.head_y-10,fill = 'orange')

        self.canvas.create_polygon(self.head_x+self.head_width+30,self.head_y-10, self.head_x+self.head_width+30, self.head_y-40,
                                  self.head_x+self.head_width+60,self.head_y-10,fill = 'orange')

        self.canvas.create_polygon(self.head_x, self.head_y+self.head_height, self.head_x+self.head_width, self.head_y+self.head_height,
                                  self.head_x + (self.head_width/2), self.head_y+(self.head_height*2),fill = 'red')

        while(self.flag):

            self.canvas.create_polygon(((2*self.head_x)+(self.head_width/2)/2, ((self.head_y*2)+(3*self.head_height))/2, ((2*self.head_x)+self.head_width*(3/2))/2,
                                  ((self.head_y*2)+(3*self.head_height))/2
                                  self.head_x + (self.head_width/2), self.head_y+(self.head_height*2),fill = 'red')

            #eyes
            self.eye(self.eye_x, self.eye_y, self.eye_r, "eye", "white")
            self.eye(self.eye_x+self.distance, self.eye_y, self.eye_r, "eye", "white")

            self.eye(self.eye_x+i, self.eye_y+j, self.pupil_r, "pupil", "black")
            self.eye(self.eye_x+self.distance+i, self.eye_y+j, self.pupil_r, "pupil", "black")

            #mouth
            self.canvas.create_polygon(self.mouth_x, self.mouth_y, self.mouth_x+self.mouth_width, self.mouth_y,
                                  self.mouth_x+(self.mouth_width/2)-(i/2), self.mouth_y+(self.mouth_width/4)-(i/4), fill = 'black')
            self.root.update()
            time.sleep(self.speed)

##            self.eye(self.eye_x, self.eye_y, self.pupil_r, "pupil", "black")
##            self.eye(self.eye_x+self.distance, self.eye_y, self.pupil_r, "pupil", "black")
##            self.root.update()
##            time.sleep(self.speed)
            if i == 70:
                aflag = True
            elif i == -70:
                aflag = False
            if aflag:
                i -=10
            else:
                i +=10






    def changeFlag(self):

        if self.flag == True:
            self.flag = False
        else:
            self.flag = True

    def show(self):
        self.canvas.grid()
        print("Showing!")

    def hide(self):
        self.canvas.grid_forget()
        print("Hiding...")

    def drawEyes(self):
        midRow = int(self.canvasH/2)
        midCol = int(self.canvasW/2)
        while(True):
            self.c.create_oval(5, 5, midCol-5, self.canvasH-40, fill="#000000")
            self.c.create_oval(midCol+5, 5, self.canvasW, self.canvasH-40, fill="#000000")
            leftRow = int(midRow/2)+100
            leftCol = int(midCol/2)
            #start pupils
            self.c.create_oval(leftRow, leftCol, leftRow+100, leftCol+100, fill="#ffffff")
            self.c.create_oval(700, 220, 600, 320, fill="#ffffff")
            self.root.update()
            time.sleep(self.speed)

            self.c.create_oval(5, 5, midCol-5, self.canvasH-40, fill="#000000")
            self.c.create_oval(midCol+5, 5, self.canvasW, self.canvasH-40, fill="#000000")
            self.c.create_oval(leftRow, leftCol, leftRow-100, leftCol+100, fill="#ffffff")
            self.c.create_oval(500, 220, 600, 320, fill="#ffffff")
            self.root.update()

