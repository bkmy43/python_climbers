# int[][] maze = new int[width][height]; // The maze
# boolean[][] wasHere = new boolean[width][height];
# boolean[][] correctPath = new boolean[width][height]; // The solution to the maze
# int startX, startY; // Starting X and Y values of maze
# int endX, endY;     // Ending X and Y values of maze
#
# public void solveMaze() {
#     maze = generateMaze(); // Create Maze (1 = path, 2 = wall)
#     for (int row = 0; row < maze.length; row++)
#         // Sets boolean Arrays to default values
#         for (int col = 0; col < maze[row].length; col++){
#             wasHere[row][col] = false;
#             correctPath[row][col] = false;
#         }
#     boolean b = recursiveSolve(startX, startY);
#     // Will leave you with a boolean array (correctPath)
#     // with the path indicated by true values.
#     // If b is false, there is no solution to the maze
# }
# public boolean recursiveSolve(int x, int y) {
#     if (x == endX && y == endY) return true; // If you reached the end
#     if (maze[x][y] == 2 || wasHere[x][y]) return false;
#     // If you are on a wall or already were here
#     wasHere[x][y] = true;
#     if (x != 0) // Checks if not on left edge
#         if (recursiveSolve(x-1, y)) { // Recalls method one to the left
#             correctPath[x][y] = true; // Sets that path value to true;
#             return true;
#         }
#     if (x != width - 1) // Checks if not on right edge
#         if (recursiveSolve(x+1, y)) { // Recalls method one to the right
#             correctPath[x][y] = true;
#             return true;
#         }
#     if (y != 0)  // Checks if not on top edge
#         if (recursiveSolve(x, y-1)) { // Recalls method one up
#             correctPath[x][y] = true;
#             return true;
#         }
#     if (y != height- 1) // Checks if not on bottom edge
#         if (recursiveSolve(x, y+1)) { // Recalls method one down
#             correctPath[x][y] = true;
#             return true;
#         }
#     return false;
# }
import random

class Maze:
    walls = [[False]]

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.entrance = (0,0)
        self.exit = (height, width)
        self.walls = [[False for i in range(width)] for j in range(height)]

    def display(self):
        symbols = {"CUR_POSITION": u'\u2591\u2591', "EMPTY_CELL":'  ', "WALL": u'\u2588\u2588',
                   "H_BOUND": u'\u2501\u2501', "V_BOUND": u'\u2503',
                   "UP_LEFT": u'\u250F', "UP_RIGHT": u'\u2513', "BOTTOM_LEFT": u'\u2517', "BOTTOM_RIGHT": u'\u251B'}

        print("Maze size: {}*{}\nEntrance: {}, Exit: {}".format(self.height, self.width, self.entrance, self.exit))

        str = symbols.get("UP_LEFT")
        for j in range(self.width):
            if (0, j) != self.entrance and (0, j) != self.exit:
                str = str + symbols.get("H_BOUND")
            else:
                str = str + '  '
        print(str + symbols.get("UP_RIGHT"))

        for i in range(self.height):
            if (i,0) != self.entrance and (i,0) != self.exit:
                str = symbols.get("V_BOUND")
            else:
                str = ' '

            for j in range(self.width):
                if (i,j) == self.entrance:
                    str = str + symbols.get("CUR_POSITION")
                else:
                    if self.walls[i][j]:
                        str = str + symbols.get("WALL")
                    else:
                        str = str + symbols.get("EMPTY_CELL")

            if (i,j) != self.entrance and (i,j) != self.exit:
                str = str + symbols.get("V_BOUND")

            print(str)

        str = symbols.get("BOTTOM_LEFT")
        for j in range(self.width):
            if (self.height-1, j) != self.entrance and (self.height-1, j) != self.exit:
                str = str + symbols.get("H_BOUND")
            else:
                str = str + '  '
        print(str + symbols.get("BOTTOM_RIGHT"))

    def randomize(self, walls_density=0.2):
        self.entrance = self.get_random_position_on_maze_boundary()
        self.exit = self.get_random_position_on_maze_boundary()

        for i in range(self.height):
            for j in range(self.width):
                if random.random() < walls_density and (i,j)!=self.entrance and (i,j) !=self.exit:
                    self.walls[i][j] = True


    def get_random_position_on_maze_boundary(self):
        boundaries = ['UP', 'LEFT', 'BOTTOM', 'RIGHT']

        wall = random.choice(boundaries)

        if wall == 'UP':
            return (0, random.choice(range(self.width)))

        if wall == 'BOTTOM':
            return (self.height-1, random.choice(range(self.width)))

        if wall == 'LEFT':
            return (random.choice(range(self.height)), 0)

        if wall == 'RIGHT':
            return (random.choice(range(self.height)), self.width-1)


m1 = Maze(10,10)
m1.randomize(0.2)
m1.display()


m1 = Maze(15,15)
m1.randomize(0.3)
m1.display()


m1 = Maze(20,20)
m1.randomize(0.4)
m1.display()
