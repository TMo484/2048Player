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
import win32api, win32con
import pandas as pd
from random import *
from selenium import webdriver

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
tile_size = 150

game_coordinates = (np.array(game_array) * tile_size) + edge_buffer

board_coordinates = (648,242,1252,850)
new_game_coordinates = (1150, 150)

shell = win32com.client.Dispatch("WScript.Shell")

#open the webbrowser to play
browser = webdriver.Chrome()
url = "https://gabrielecirulli.github.io/2048/"
browser.get(url)
#read the HTML inside
innerHTML = browser.execute_script("return document.body.innerHTML")


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

def is_game_over(img):
    if img.load()[5,5] == (223,212,202):
        return True
    else:
        return False
    
def start_new_game(new_game_coordinates):
    x = new_game_coordinates[0]
    y = new_game_coordinates[1]
    win32api.SetCursorPos(new_game_coordinates)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

training_data = pd.read_csv('C:\\Users\\Tom Mori\\Documents\\2048_ML\\rfc_training_data.csv')
training_data.columns = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

#for i in range(5):
#    print("Current Generation: " + str(i))
#    #set up the model
#    training_data = training_data[training_data[17]==1]
#    X = training_data.drop([16,17], axis=1)
#    y = training_data[16]
#    clf = RandomForestClassifier()
#    clf.fit(X, y)
#    #start a new game
#    start_new_game(new_game_coordinates)
#    # initialize the variables
#    img = grab_img(board_coordinates)
#    board_vals = get_board_value(img)
#    score = np.array(board_vals).sum()
#    # set up some counters
#    same_move_count = 0
#    error_count = 0
#    # Start Playing!
#    while not is_game_over(img):
#        img = grab_img(board_coordinates)
#        if error_count >= 10:
#            print("I've had a few errors...")
#            break
#        else:
#            try:    
#            # pull the new board data
#                board_vals = get_board_value(img)
#            # make a prediction, and press the key
#            # first check to see if we've been making the same move
#                if same_move_count >= 2:
#                    prediction = randint(0,3)
#                    print("random move")
#                else:
#                    prediction = clf.predict(np.array(board_vals).reshape(1, -1))[0]
#                press_keys(prediction)
#            # wait for board to move
#                sleep(0.15)
#            # check to see if the score increased
#                score_inc = np.array(get_board_value(grab_img(board_coordinates))).sum() > score
#                if score_inc:
#                    same_move_count = 0
#                else:
#                    same_move_count += 1
#            # set the score to the new board_value
#                score = np.array(board_vals).sum()
#            # create a DataFrame for this move
#                this_move_data = pd.DataFrame(np.append(board_vals, [prediction, int(score_inc)])).transpose()
#            # add the new move to the training data
#                training_data = training_data.append(this_move_data)
#            # if I can't read the board, throw an error
#            except:
#                error_count += 1
#                print("Whoops. Trying again...")
#    # if we have hit the game over endpoint:
#    print("Game Over!")
#    # save this gernerations data
#    training_data.to_csv('rfc_training_data.csv', index=False)
#    training_data.to_csv('rfc_training_data_' + strftime('%Y_%m_%d_%H_%M') + '.csv', index=False)