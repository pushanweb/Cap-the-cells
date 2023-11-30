from Play import *


def main():
    while True:
                
        size_x = int(input("\nEnter the size of the square board from 2 to 6: \n")) * 2 + 1

        size_y = size_x

        depth = int(input("\nChoose Difficulty level from 2 to 4: \n"))

        Match = Play(size_y, size_x, depth)
        Match.start()
            
if __name__ == "__main__":
    main()
