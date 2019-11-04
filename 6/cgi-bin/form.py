import cgi
import math

form = cgi.FieldStorage()
firstSide = form.getfirst("first", 0)
secondSide = form.getfirst("second", 0)
thirdSide = form.getfirst("third", 0)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Square triangle</title>
        </head>
        <body>""")

intFirst = 0
intSecond = 0
intThird = 0
showResult = False

try:
    intFirst = int(firstSide)
    intSecond = int(secondSide)
    intThird = int(thirdSide)
    showResult = True
except Exception:
    print("<p>Not valid value</p>")

p = (intFirst + intSecond+ intThird)/2
triangleSquare = math.sqrt(p * (p - intFirst) * (p - intSecond) * (p - intThird))
if showResult:
    print("<h1>Result computing:</h1>")
    print("<p>First side triangle: {}</p>".format(firstSide))
    print("<p>Second side triangle: {}</p>".format(secondSide))
    print("<p>Third side triangle: {}</p>".format(thirdSide))
    print("<p>Result: {}</p>".format(triangleSquare))
print("""</body>
        </html>""")
