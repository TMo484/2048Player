# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 20:16:38 2017

@author: Tom Mori
"""

from PIL import Image
import pyscreenshot as ImageGrab
import numpy as np
from time import sleep
import win32com.client
import pandas as pd

import tensorflow as tf
from sklearn.ensemble import RandomForestClassifier

tile_dict = {(205, 193, 180): 0,
             (205, 193, 179): 0,
             (238, 228, 218): 2,
             (237, 224, 200): 4,
             (242, 177, 121): 8,
             (245, 149, 99): 16,
             (246, 124, 95): 32,
             (246, 94, 59): 64,
             (237, 207, 114): 128,
             (237, 204, 97): 256,
             (237, 200, 80): 512}

game_array = [(0,0), (1,0), (2,0), (3,0),
             (0,1), (1,1), (2,1), (3,1),
             (0,2), (1,2), (2,2), (3,2),
             (0,3), (1,3), (2,3), (3,3)]

edge_buffer = 40
tile_size = 335

game_coordinates = (np.array(game_array) * tile_size) + edge_buffer

board_coordinates = (172, 457, 1347, 1670)

shell = win32com.client.Dispatch("WScript.Shell")

def grab_img(coordinates):
    im = ImageGrab.grab(bbox=coordinates)
    return im

def get_board_value(img):
    pix = img.load()
    board_vals = []
    try:
        board_vals = [tile_dict[pix[int(x[0]), int(x[1])]] for x in game_coordinates]
        return board_vals
    except KeyError:
        print("Failed to find key")
        return board_vals

def read_clf_output(output):
    return None

def press_keys(direction):
    if direction == 0:
        print('Up')
        shell.SendKeys("{Up}")
    elif direction == 1:
        print('Down')
        shell.SendKeys("{Down}")
    elif direction == 2:
        print('Left')
        shell.SendKeys("{Left}")
    elif direction == 3:
        print('Right')
        shell.SendKeys("{Right}")    
    else:
        raise TypeError

X = training_data.drop([16,17], axis=1)
y = training_data(training_data[16])
clf.fit(X, y)
clf.predict(X[0])

#for i in range(3):
#    print(3-i)
#    sleep(1)
#board_vals = get_board_value(grab_img(board_coordinates))
#post_move_score = np.array(board_vals).sum()
#for i in range(25):
#    sleep(1)
#    pre_move_score = post_move_score
#    board_vals = get_board_value(grab_img(board_coordinates))
#    pred_df = pd.DataFrame(board_vals).transpose()
#    
#    predicted_move = clf.predict(pred_df)[0]
#    press_keys(predicted_move)
#    post_move_score = np.array(board_vals).sum()
#    
#    if post_move_score > pre_move_score:
#        score_inc = 1
#    else:
#        score_inc = 0
#    print(score_inc)