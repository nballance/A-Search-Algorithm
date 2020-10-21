from Map import *
from draw_grid import *

def main():
    make_grid()
    
    make_hard()

    design_all_highways()
    
    make_blocked()
    
    # print_grid()
    make_start()
    print("start x: ", start[0], " start y: ", start[1])
    make_goal()

    print("goal x: ", goal[0], " goal y: ", goal[1])

    draw_grid(False)

    # print(write_grid_file())
    # read_grid_file()
if __name__ == "__main__":
    main()
