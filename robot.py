class Robot:
    def __init__(self, name, src, dst):
        self.name = name
        self.src = src
        self.dst = dst
        self.path = [src, ]
print("Robot file loaded from:", __file__)
