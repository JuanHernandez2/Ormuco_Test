# Overlaping script

What I did is that I created a Line class that will represent a line on the x-axis, after that I do 3 comparaisons:

1. If the start of the first line is major or equal to the start of the second line and the start of the first line is minor to the end of the second line then it overlaps
2. If the end of the first line is major to the start of the second line and the end of the first line is minor or equal to the end of the second line then it overlaps
3. If the end of the first line is major or equal to the end of the second line and the start of the first line is minor or equal to the start of the second line then it overlaps

If none of the above conditions are True then the two line doesn´t overlap. 
 
