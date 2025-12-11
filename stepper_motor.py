from machine import Pin
import time

pins=[
    [1,0,0,0]
    [1,1,0,0]
    [0,1,0,0]
    [0,1,1,0]
    [0,0,1,0]
    [0,0,1,1]
    [0,0,0,1]
    [1,0,0,1]
      ]

delay = 2
steps_per_rev = 4096

def step(direction=1): # direction = 1 -> forward, -1 -> backwards
    for pin in pins:
        