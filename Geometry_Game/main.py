class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, lower_left, upper_right):
        if lower_left[0] < self.x < upper_right[0] \
                and lower_left[1] < self.y < upper_right[1]:
            return True
        else:
            return False
