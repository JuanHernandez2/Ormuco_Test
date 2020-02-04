import sys

class Line:
    """ Representation of a 1D delimited line"""

    def __init__(self, start, end):
        self.start = min(start, end)
        self.end = max(start, end)
    

    def __str__(self):
        return "Line: (" + str(self.start) + ", " + str(self.end) + ")"

def overlap(line1: Line, line2: Line):

    if line1.start >= line2.start and line1.start < line2.end:
        return True
    elif line1.end > line2.start and line1.end <= line2.end:
        return True
    elif line1.end >= line2.end and line1.start <= line2.start:
        return True
    else:
        return False

if __name__ == "__main__":
    line1 = Line(1, 5)
    line2 = Line(6,8)
    if overlap(line1, line2):
        print(f"{str(line1)} and {str(line2)} overlaps")
    else:
        print(f"{str(line1)} and {str(line2)} don´t overlap")

    
    line1 = Line(1, 13)
    line2 = Line(6,8)
    if overlap(line1, line2):
        print(f"{str(line1)} and {str(line2)} overlaps")
    else:
        print(f"{str(line1)} and {str(line2)} don´t overlap")
    

    line1 = Line(1, 13)
    line2 = Line(500,1000)
    if overlap(line1, line2):
        print(f"{str(line1)} and {str(line2)} overlaps")
    else:
        print(f"{str(line1)} and {str(line2)} don´t overlap")

    