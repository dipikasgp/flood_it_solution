import copy
import random

import numpy as np


class FloodFill:

    @classmethod
    def flood_fill(cls, image, chosen_color):
        prev_color = image[0][0]
        cls.fill(image, 0, 0, chosen_color, prev_color)
        return image

    @classmethod
    def fill(cls, image, row, col, chosen_color, prev_color):
        '''
        :param image: tile to check
        :param row: current row
        :param col: current column
        :param chosen_color: chosen color with which the tile needs to be filled
        :param prev_color: previous color of the origin
        :return: returns the image itself
        '''
        # check if current cell is out of bounds or connected to the origin
        if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != prev_color:
            return

        image[row][col] = chosen_color
        cls.fill(image, row + 1, col, chosen_color, prev_color)
        cls.fill(image, row, col + 1, chosen_color, prev_color)
        cls.fill(image, row - 1, col, chosen_color, prev_color)
        cls.fill(image, row, col - 1, chosen_color, prev_color)

    @classmethod
    def find_filled_cells(cls, image, row, col, color, visited):
        '''
        :param image: tile to check
        :param row: current row to visit
        :param col: current colum to visit
        :param color: check the cells which has color
        :param visited: matrix to flag visited cells
        :return: number of filled cells with color
        '''
        # check if current cell is out of bounds or not of the target color or already visited
        if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != color or visited[row][
            col]:
            return 0

        visited[row][col] = True
        filled_cells = 1

        filled_cells += cls.find_filled_cells(image, row + 1, col, color, visited)
        filled_cells += cls.find_filled_cells(image, row - 1, col, color, visited)
        filled_cells += cls.find_filled_cells(image, row, col + 1, color, visited)
        filled_cells += cls.find_filled_cells(image, row, col - 1, color, visited)

        return filled_cells

    @staticmethod
    def print_tiles(image):
        '''
        prints the image
        '''
        for row in image:
            for element in row:
                print(element, end=' ')
            print()

    @classmethod
    def find_best_move(cls, image):
        '''
        This function checks the best move for the tile so that
        the number of tiles covered is maximized
        :param image: tile to check
        :return: returns the best choice of color
        '''
        np_image = np.array(image)
        unique_colors = list(np.unique(np_image))
        best_choice = {item: 0 for item in unique_colors}
        for color in unique_colors:
            if color == image[0][0]:
                continue
            matrix = copy.deepcopy(image)
            matrix = cls.flood_fill(matrix, chosen_color=color)
            visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
            filled_cells = cls.find_filled_cells(matrix, 0, 0, color, visited)
            best_choice[color] = filled_cells
        return max(best_choice, key=best_choice.get)

    @staticmethod
    def create_tiles(n, m):
        """
        :type n: integer
        :type m: integer
        """
        tiles = [[random.randint(0, m - 1) for _ in range(n)] for _ in range(n)]
        FloodFill.print_tiles(tiles)
        return tiles

    @classmethod
    def play(cls, tiles, automated_player=True):
        """
        :type tiles: list[list]
        :type automated_player: boolean
        """
        moves = 0
        while True:
            best_choice = cls.find_best_move(tiles)
            if automated_player:
                tiles = cls.flood_fill(tiles, chosen_color=best_choice)
                moves += 1
                print()
                cls.print_tiles(tiles)
            else:
                user_input = input(f'Next best move - {best_choice}. Choose it? Enter Y for yes, N for No')
                choice = str(user_input).lower()
                if choice == 'y':
                    tiles = cls.flood_fill(tiles, chosen_color=best_choice)
                    moves += 1
                    print()
                    cls.print_tiles(tiles)
                else:
                    num = input("Enter the number:")
                    num = int(num)
                    if choice == -1:
                        break
                    tiles = cls.flood_fill(tiles, chosen_color=num)
                    moves += 1
                    print()
                    cls.print_tiles(tiles)
            np_tiles = np.array(tiles)
            uniques = list(np.unique(np_tiles))
            if len(uniques) == 1:
                break
        return moves


if __name__ == '__main__':
    while True:
        # while True:
        #     n = input('Enter the size of the tiles: ')
        #     if int(n) <= 0:
        #         print("That's not a valid input. Please try again ")
        #     else:
        #         break
        # while True:
        #     m = input('Enter the number of colors: ')
        #     if int(m) <= 0:
        #          print("That's not a valid input please try again ")
        #     elif int(m) > int(n) * int(n):
        #         print("Number of colors cannot be greater than the size of the tiles. Please try again")
        #     else:
        #         break
        # image = FloodFill.create_tiles(int(n), int(m))
        automated_player = input('Do you want an automated player? Enter 1 for Yes, 0 for No: ')
        image = [[1, 0, 1, 1, 1, 1],
                 [1, 0, 1, 1, 1, 1],
                 [1, 0, 1, 1, 1, 1],
                 [1, 0, 1, 1, 1, 1],
                 [1, 0, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1]]
        # img = FloodFill.flood_fill(image, 2)
        FloodFill.print_tiles(image)
        automated_player = False
        total_moves = FloodFill.play(image, automated_player)
        print('Total moves taken: ', total_moves)
        user_input = input("Do you want to play again? Enter Y for Yes, N for No: ")
        if user_input.lower() != 'y':
            break
