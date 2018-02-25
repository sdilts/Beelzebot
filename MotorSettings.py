class CommandSettings:
    def __init__(self, img):
        self.img = img

    def get_customizations():
        return {key:value for key, value in A.__dict__.items() if not key.startswith('__') and not callable(key)}



class MotorSettings(CommandSettings):

    def __init__(self,function_to_call,speed, wait, img, maxSpeed=3):
        CommandSettings.__init__(self,img)
        self.function_to_call = function_to_call
        self.wait = wait
        self.speed_or_position = speed_or_position

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "(Function: {}, Wait: {}, speed_or_position: {})".format(self.function_to_call, self.wait, self.speed_or_position)

    def verify_new_settings(new_settings):
        pass

class ServoSettings(CommandSettings):

    def __init__(self, function_to_call, repeats, img, maxRepeats=1):
        CommandSettings.__init__(self,img)
        self.function_to_call = function_to_call
        self.repeats = repeats

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "(Function: {}, Repeats: {})".format(self.function_to_call, self.repeats)

    def verify_new_settings(new_settings):
        return True
