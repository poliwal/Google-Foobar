"""
	Level 2 :- Dont Get Voluteered
	As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. It's not easy building a doomsday device and capturing bunnies at the same time, after all! In order to make sure that everyone working for her is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

	To help yourself get to and from your bunk every day, write a function called answer(src, dest) which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle. The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape). Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

	-	0	1	2	3	4	5	6	7
	0	0	1	2	3	4	5	6	7
	1	8	9	10	11	12	13	14	15
	2	16	17	18	19	20	21	22	23
	3	24	25	26	27	28	29	30	31
	4	32	33	34	35	36	37	38	39
	5	40	41	42	43	44	45	46	47
	6	48	49	50	51	52	53	54	55
	7	56	57	58	59	60	61	62	63

	Test cases
	Inputs:
	(int) src = 19
	(int) dest = 36

	Output:
	(int) 1

	Inputs:
	(int) src = 0
	(int) dest = 1

	Output:
	(int) 3
"""

class Chess:
	def __init__(self,x,y,distance):
		self.x = x
		self.y = y
		self.distance = distance
	
def solution(src, dest):
	pos = {}
	c = 0
	x,y = 1,0
	for i in range(64):
		y+=1
		if c == 8:
			x+=1
			y=1
			c=0
		pos[i] = (x,y)
		c+=1
	src = pos[src]
	dest = pos[dest]
	xShift = [2,2,-2,-2,1,1,-1,-1]
	yShift = [1,-1,1,-1,2,-2,2,-2]
	visited = [[False for _ in range(9)]for _ in range(9)]
	visited[src[0]][src[1]] = True
	q = []
	q.append(Chess(src[0],src[1],0))
	
	while len(q)>0:
		s = q[0]
		q.pop(0)
		
		if s.x == dest[0] and s.y == dest[1]:
			return s.distance
		
		for shift in range(8):
			x = s.x + xShift[shift]
			y = s.y + yShift[shift]
			
			if (x>=1 and x<=8 and y>=1 and y<=8) and not visited[x][y]:
				visited[x][y] = True
				q.append(Chess(x,y,s.distance+1))

print(solution(19,36))   