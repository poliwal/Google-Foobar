""" 
    Level-2 :- Bunny Prisoner Locating

    Keeping track of Commander Lambda's many bunny prisoners is starting to get tricky. You've been tasked with writing a program to match bunny prisoner IDs to cell locations.

    The LAMBCHOP doomsday device takes up much of the interior of Commander Lambda's space station, and as a result the prison blocks have an unusual layout. They are stacked in a triangular shape, and the bunny prisoners are given numerical IDs starting from the corner, as follows:

    | 7 | 4 8 | 2 5 9 | 1 3 6 10

    Each cell can be represented as points (x, y), with x being the distance from the vertical wall, and y being the height from the ground.

    For example, the bunny prisoner at (1, 1) has ID 1, the bunny prisoner at (3, 2) has ID 9, and the bunny prisoner at (2,3) has ID 8. This pattern of numbering continues indefinitely (Commander Lambda has been taking a LOT of prisoners).

    Write a function answer(x, y) which returns the prisoner ID of the bunny at location (x, y). Each value of x and y will be at least 1 and no greater than 100,000. Since the prisoner ID can be very large, return your answer as a string representation of the number.

    Test cases
    Inputs: (int) x = 3 (int) y = 2 Output: (string) "9"

    Inputs: (int) x = 5 (int) y = 10 Output: (string) "96"
"""

def solution(x,y):
  l = [1]
  row = (x-1)+y
  for i in range(y-1):
      l.append(l[i]+(i+1))
  res = []
  column = row
  Elem = l[-1]
  i = 0
  ind = (y-1)+2
  res.append(Elem)
  for i in range(x-1):
      Elem = Elem+ind
      ind += 1

  return str(Elem)


print(solution(3,2))