class MotorSettings:


    def __init__(self,function_to_call,speed_or_position, wait, img):
        # self.motor_channel
        # self.speed_dir
        self.function_to_call = function_to_call
        self.wait = wait
        self.speed_or_position = speed_or_position
        self.img = img

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "(Function: {}, Wait: {}, speed_or_position: {})".format(self.function_to_call, self.wait, self.speed_or_position)
