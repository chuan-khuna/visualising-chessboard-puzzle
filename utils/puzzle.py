import numpy as np


def generate_board(n=6):
    # generate a chess board size 2 ** n
    # and the position of the key

    num_row = n // 2
    num_col = n - num_row
    row = 2**num_row
    col = 2**num_col

    board = np.random.randint(2, size=2**n)
    key_position = np.random.randint(2**n)
    key = np.zeros_like(board)
    key[key_position] = 1

    board = board.reshape(row, col)
    key = key.reshape(row, col)

    return board, key, key_position


def to_binary_string(length, number):
    return f"{number:0{length}b}"


def generate_binary_position_array(n):
    position = np.arange(2**n)
    bin_position = []
    for pos in position:
        bin_position.append(to_binary_string(n, pos))
    return bin_position

def generate_pairity_masking(n):
    binary_pos_arr = generate_binary_position_array(n)
    masking_dict = {}
    for i in range(n):
        # mask if position the bit at i = 1
        mask_i = []
        for pos in binary_pos_arr:
            if pos[i] == '1':
                mask_i.append(1)
            else: 
                mask_i.append(np.nan)
        masking_dict[n-i-1] = np.array(mask_i)
    return masking_dict