from gui import Window
from objects import Point, Line, Cell, Maze

def main():
    win = Window(800, 600)
    num_cols = 12
    num_rows = 10
    m1 = Maze(15, 15, num_rows, num_cols, 10, 10, win)

    m1.solve()

    win.wait_for_close()



if __name__ == "__main__":
    main()

    


        #p1 = Point(100, 100)
    #p2 = Point(200, 200)
    #my_line = Line(p1, p2)
    #my_cell1 = Cell(50,100,200,100,win, False, False, True, True)
    #my_cell2 = Cell(10,30,50,10,win, True, True, True, True)    
    #my_cell1.draw()
    #my_cell2.draw()
    #my_cell1.draw_move(my_cell2)
    #win.draw_line(my_line, "black")