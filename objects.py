import time
import random

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)

class Cell():
    def __init__(self, _x1, _x2, _y1, _y2, _win = None, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2
        self._win = _win 
        self.visited = False
        self.mid = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)

    def draw(self):
        if self._win is None:
            return
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bot_left = Point(self._x1, self._y2)
        bot_right = Point(self._x2, self._y2)
        
        if self.has_top_wall:
            top_line = Line(top_left, top_right)
            top_line.draw(self._win.canvas, "black")
        else:
            top_line = Line(top_left, top_right)
            top_line.draw(self._win.canvas, "white")
        
        if self.has_right_wall:
            right_line = Line(top_right, bot_right)
            right_line.draw(self._win.canvas, "black")
        else:
            right_line = Line(top_right, bot_right)
            right_line.draw(self._win.canvas, "white")

        if self.has_bottom_wall:
            bot_line = Line(bot_left, bot_right)
            bot_line.draw(self._win.canvas, "black")
        else:
            bot_line = Line(bot_left, bot_right)
            bot_line.draw(self._win.canvas, "white")
        
        if self.has_left_wall:
            left_line = Line(top_left, bot_left)
            left_line.draw(self._win.canvas, "black")
        else:
            left_line = Line(top_left, bot_left)
            left_line.draw(self._win.canvas, "white")

    def draw_move(self, to_cell, undo=False):
        if undo is False:
            color = "red"
        else:
            color = "grey"
        #x_mid =  self._x1 + (self._x2-self._x1) / 2
        #y_mid = self._y1 + (self._y2-self._y1)/2
        
        path = Line(self.mid, to_cell.mid)
        path.draw(self._win.canvas, fill_color=color)

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed != None:
            random.seed(seed)
        self._create_cells()

    
    def _create_cells(self):
        self._cells = []
        # Create columns of cells
        #for j in range(self.num_cols):
        #    column = []
        #    for i in range(self.num_rows):
        for i in range(self.num_rows):
            rows = []
            for j in range(self.num_cols): 
         
                # Calculate cell coordinates
                x1 = self.x1 + j * self.cell_size_x
                y1 = self.y1 + i * self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y
                
                cell = Cell(_x1=x1, _x2=x2, _y1=y1, _y2=y2, _win=self.win)
                
                rows.append(cell)
            self._cells.append(rows)

   
        self.__break_walls_r(i, j)
        self._break_entrance_and_exit() 
        self.__reset_cells_visited()    
        for j in range(self.num_cols):
            for i in range(self.num_rows):
                self._draw_cell(i, j)  

        

    def _draw_cell(self, i, j):
        
        cell = self._cells[i][j]
        cell.draw()
        self._animate()

    def _animate(self):
        if self.win is not None:
            self.win.redraw()
        time.sleep(0.1)
            

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        


    def __break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            
            adjacent = []
            if 0 <= i-1 <= self.num_rows-1 and self._cells[i-1][j].visited is False:
                top_cell = self._cells[i-1][j]
                adjacent.append((top_cell, "top"))
            if 0 <= j+1 <= self.num_cols-1 and self._cells[i][j+1].visited is False:
                right_cell = self._cells[i][j+1]
                adjacent.append((right_cell, "right"))
            if 0 <= i+1 <= self.num_rows-1 and self._cells[i+1][j].visited is False:
                bot_cell = self._cells[i+1][j]
                adjacent.append((bot_cell, "bot"))
            if 0 <= j-1 <= self.num_cols-1 and self._cells[i][j-1].visited is False:
                left_cell = self._cells[i][j-1]
                adjacent.append((left_cell, "left"))
            if adjacent == []:
                return
            else:
                index= random.randrange(0, len(adjacent))
                next_item = adjacent[index]
                next_cell = next_item[0]
                direction = next_item[1]
                
                if direction == "top":
                    current_cell.has_top_wall = False
                    next_cell.has_bottom_wall = False
                    self.__break_walls_r(i-1, j)

                if direction == "right":
                    current_cell.has_right_wall = False
                    next_cell.has_left_wall = False
                    self.__break_walls_r(i, j+1)

                if direction == "bot":
                    current_cell.has_bottom_wall = False
                    next_cell.has_top_wall = False
                    self.__break_walls_r(i+1, j)

                if direction == "left":
                    current_cell.has_left_wall = False
                    next_cell.has_right_wall = False
                    self.__break_walls_r(i, j-1)

  
    def __reset_cells_visited(self):
        for j in range(self.num_cols):
            for i in range(self.num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        current = self._cells[i][j]
        current.visited = True
    
        if current == self._cells[-1][-1]:
            return True
        
        paths = []
        # Boundary checks added here:
        if i > 0 and current.has_top_wall == False and self._cells[i-1][j].visited is False:
            paths.append((-1, 0))
        if j < self.num_cols - 1 and current.has_right_wall == False and self._cells[i][j+1].visited is False:
            paths.append((0, +1))
        if i < self.num_rows - 1 and current.has_bottom_wall == False and self._cells[i+1][j].visited is False:
            paths.append((+1, 0))
        if j > 0 and current.has_left_wall == False and self._cells[i][j-1].visited is False:
            paths.append((0, -1))
        
        if paths == []:
            return False
        else:
            for di, dj in paths:
                ni = i + di
                nj = j + dj
                next_cell = self._cells[ni][nj]
                # Draw your move, recurse, handle undo if needed
                current.draw_move(next_cell)
                
                result = self._solve_r(ni, nj)
                if result:
                    return True
                current.draw_move(next_cell, undo=True)
        return False
    
    '''
    def _solve_r(self, i, j):
        print(f"Solving cell ({i}, {j})")
        self._animate()
        current = self._cells[i][j]
        current.visited = True
        
        if current == self._cells[-1][-1]:
            return True
        
            
        paths = []
        if current.has_top_wall == False and self._cells[i-1][j].visited is False:
            paths.append((-1, 0))
            

        if current.has_right_wall == False and self._cells[i][j+1].visited is False:
            paths.append((0, +1))


        if current.has_bottom_wall == False and self._cells[i+1][j].visited is False:
            paths.append((+1, 0))


        if current.has_left_wall == False and self._cells[i][j-1].visited is False:
            paths.append((0, -1))


        if paths == []:
            return False
        else:
            for di, dj in paths:
                ni = i + di
                nj = j + dj
                next_cell = self._cells[ni][nj]
                current.draw_move(next_cell)
                

                result = self._solve_r(ni, nj)
                if result:
                    return True
                current.draw_move(next_cell, undo=True)
        return False

'''