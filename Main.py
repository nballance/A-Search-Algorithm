from Map import *
from Draw_Grid import *
# from A_Star_Test import *
# from Heuristic_Search import *
from Heuristic_Search2 import *
import sys

def main():
    print("Would you like to read in a file? ('1' for yes and '2' for no)")
    response_str = input()
    try:
        response_int = int(response_str)
        
        if(response_int == 1):
            
            #open_file()
            print("Enter the name of the file.")
            file_name = input()

            make_grid()

            read_grid_file(file_name)

            draw_grid(False)

        elif(response_int == 2):
            make_grid()
    
            make_hard()

            design_all_highways()
            
            make_blocked()


            # print_grid()

            make_start()
            make_goal()

            
            # a_search_standard()

            draw_grid(False)

            print("Enter the algorithm you would like to test: ", "'1' for standard a_search_algorithm"," or ", "'2' for a_search_algorithm with weight")
            algo_int = -1
            algo_str = input()
            try:
                algo_int = int(algo_str)
                if(algo_int == 1):
                    print("standard a_search_algorithm called.")
                    a_search_standard()
                    draw_grid(True)
                    #Call draw function here
                elif(algo_int == 2):
                    print("Enter the weight for the a_search_algorithm: ")
                    weight_str = input()
                    try:
                        weight = int(weight_str)
                        print("a_search_algorithm with weight of ", weight, " called.")
                        a_search(weight)
                        draw_grid(True)
                        #Call draw function here
                    except ValueError:
                        print("That's not an integer weight!")
                else:
                    print("Enter an integer as 1 or 2!")
                
            except ValueError:
                print("That's not an int!")
        else:
            print("Enter an integer as 1 or 2!")
    except ValueError:
        print("Enter an integer as 1 or 2!")



    

    

    # print(write_grid_file())
    # read_grid_file()
if __name__ == "__main__":
    main()
