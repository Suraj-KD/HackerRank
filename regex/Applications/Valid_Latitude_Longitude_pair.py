'''
Task:
Given a line of text which possibly contains the latitude and longitude of a point, can you use regular expressions to identify the latitude and longitude referred to (if any)?

Input Format :
The first line contains an integer N, which is the number of tests to follow.
This is followed by N lines of text. Each line contains a pair of co-ordinates which possibly indicate the latitude and longitude of a place.

Constraints :
1 <= N <= 100
The latitude and longitude, if present will always appear in the form of (X, Y) where X and Y are decimal numbers.
For a valid (latitude, longitude) pair:
-90<=X<=+90 and -180<=Y<=180.
They will not contain any symbols for degrees or radians or N/S/E/W. There may or may not be a +/- sign preceding X or Y.
There will be a space between Y and the comma before it.
There will be no space between X and the preceding left-bracket, or between Y and the following right-bracket.
There will be no unnecessary zeros (0) before X or Y.

Output Format :
"Valid" where X and Y are the latitude and longitude which you found to be a valid (latitude,longitude) pair.
If the given pair of numbers are not a valid (latitude,longitude) pair, output "Invalid".

Sample Input : 
2
(75, 180)
(90., 180.)

Sample Output :
Valid
Invalid
'''
import re, sys
Regex_pattern = r'\(([+-]?(\d|[1-9]\d)(\.[0-9]+)?), ([+-]?(\d|[1-9]\d|[1-9]\d\d)(\.?[0-9]+)?)\)'
for line in sys.stdin.readlines()[1:]:
    match = re.search(Regex_pattern, line)
    try:
        latitude = float(match.group(1))
        longitude = float(match.group(4))
        valid = True
        if not ((-90 <= latitude) and (latitude <= 90)):
            valid = False
        if not ((-180 <= longitude) and (longitude <= 180)):
            valid = False
    except (ValueError, AttributeError):
        valid = False
    if valid:
        print("Valid")
    else:
        print("Invalid")
