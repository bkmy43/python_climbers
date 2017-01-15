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
import os
import time

class Maze:
    cur_x = 0
    cur_y = 0
    entrance = (0, 0)
    max_steps = 50000
    pause_between_steps = 0.05

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.exit = (height, width)
        self.walls = [[False for i in range(width)] for j in range(height)]
        self.visited = [[False for i in range(width)] for j in range(height)]

    def cur_position(self):
        return (self.cur_y, self.cur_x)

    def display(self):
        symbols = {"CUR_POSITION": u'ME', "VISITED": u'\u2591\u2591', "NOT_VISITED":'  ', "WALL": u'\u2588\u2588',
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
                if (i,j) == self.cur_position():
                    str = str + symbols.get("CUR_POSITION")
                else:
                    if self.walls[i][j]:
                        str = str + symbols.get("WALL")
                    elif self.visited[i][j]:
                        str = str + symbols.get("VISITED")
                    else:
                        str = str + symbols.get("NOT_VISITED")

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

    def randomize(self, walls_density=0.25):
        self.entrance = self.get_random_position_on_maze_boundary()
        self.exit = self.get_random_position_on_maze_boundary()
        self.cur_y = self.entrance[0]
        self.cur_x = self.entrance[1]

        for i in range(self.height):
            for j in range(self.width):
                if random.random() < walls_density and (i,j)!=self.entrance and (i,j) !=self.exit:
                    self.walls[i][j] = True


    def get_random_position_on_maze_boundary(self):
        boundaries = ['UP', 'LEFT', 'BOTTOM', 'RIGHT']

        wall = random.choice(boundaries)

        if wall == 'UP':
            return (0, random.choice(range(self.width)))
        elif wall == 'BOTTOM':
            return (self.height-1, random.choice(range(self.width)))
        elif wall == 'LEFT':
            return (random.choice(range(self.height)), 0)
        elif wall == 'RIGHT':
            return (random.choice(range(self.height)), self.width-1)

    def move(self, direction):
        if direction == 'UP':
            if self.cur_y > 0 and not self.walls[self.cur_y-1][self.cur_x]:
                self.cur_y = self.cur_y-1
            else:
                return False
        elif direction == 'DOWN':
            if self.cur_y < self.height - 1 and not self.walls[self.cur_y + 1][self.cur_x]:
                self.cur_y = self.cur_y + 1
            else:
                return False
        elif direction == 'LEFT':
            if self.cur_x > 0 and not self.walls[self.cur_y][self.cur_x - 1]:
                self.cur_x = self.cur_x - 1
            else:
                return False
        elif direction == 'RIGHT':
            if self.cur_x < self.width - 1 and not self.walls[self.cur_y][self.cur_x + 1]:
                self.cur_x = self.cur_x + 1
            else:
                return False

        self.visited[self.cur_y][self.cur_x] = True
        return True

    def chaotic_run(self):
        for i in range(self.max_steps):
            time.sleep(self.pause_between_steps)
            os.system('clear')
            m1.move(random.choice(('UP', 'DOWN', 'LEFT', 'RIGHT')))
            m1.display()
            if self.cur_position() == self.exit:
                print("Sucessfully reached exit. {} steps were needed".format(i + 1))
                return True
            print("This is CHAOTIC RUN\nTrying to get out of this maze... {} steps done".format(i+1))
            print(self.get_best_move())

        print("Maximum of {} steps reached, exit not found...".format(i+1))
        return False


    def smart_run(self):
        for i in range(self.max_steps):
            time.sleep(self.pause_between_steps)
            os.system('clear')
            m1.move(self.get_best_move())
            m1.display()
            if self.cur_position() == self.exit:
                print("Sucessfully reached exit. {} steps were needed".format(i + 1))
                return True
            print("This is SMART RUN\nTrying to get out of this maze... {} steps done".format(i + 1))

        print("Maximum of {} steps reached, exit not found...".format(i + 1))
        return False

    def get_best_move(self):
        options = {'UP':0, 'DOWN':0, 'LEFT':0, 'RIGHT':0}

        for option in options.keys():
            if option == 'UP':
                if self.cur_y > 0 and not self.walls[self.cur_y - 1][self.cur_x]:
                    options[option] = self.get_distance(self.exit, (self.cur_y-1, self.cur_x))
                else:
                    options[option] = self.width + self.height
            elif option == 'DOWN':
                if self.cur_y < self.height - 1 and not self.walls[self.cur_y + 1][self.cur_x] and not self.visited[self.cur_y + 1][self.cur_x]:
                    options[option] = self.get_distance(self.exit, (self.cur_y + 1, self.cur_x))
                else:
                    options[option] = self.width + self.height
            elif option == 'LEFT':
                if self.cur_x > 0 and not self.walls[self.cur_y][self.cur_x - 1]  and not self.visited[self.cur_y][self.cur_x - 1]:
                    options[option] = self.get_distance(self.exit, (self.cur_y, self.cur_x-1))
                else:
                    options[option] = self.width + self.height
            elif option == 'RIGHT':
                if self.cur_x < self.width - 1 and not self.walls[self.cur_y][self.cur_x + 1] and not self.visited[self.cur_y][self.cur_x + 1]:
                    options[option] = self.get_distance(self.exit, (self.cur_y, self.cur_x - 1))
                else:
                    options[option] = self.width + self.height

        return min(options, key=options.get)

    def get_distance(self,point1, point2):
        return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])

os.environ['TERM']='xterm'

m1 = Maze(40,40)
m1.randomize(0.25)
m1.display()

m1.smart_run()





