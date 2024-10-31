from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class LoggerMixin:
    def log_info(self, message):
        print(f"INFO: {message}")

class Square(Shape, LoggerMixin):
    def __init__(self, side_length):
        self.side_length = side_length

    
    def calculate_area(self):
        area = self.side_length ** 2
        self.log_info(f"Square area calculated: {area}")
        return area


square_instance = Square(side_length=4)

square_area = square_instance.calculate_area()