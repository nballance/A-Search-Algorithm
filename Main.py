from Map import *


def main():
    make_grid()
    #passed
    
    #print_grid()
    #passed

    # make_hard()
    # #passed

     
    # make_highway()
    # #passed

    # make_blocked()

    # #read_grid_file("example_grid.txt")
    # print_grid()

    make_start()
    make_goal()
    make_hard()
    
    print(write_grid_file())
    print("hello world!")

if __name__ == "__main__":
    main()
