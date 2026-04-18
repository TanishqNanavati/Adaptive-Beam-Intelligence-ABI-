# Models the LEO satellite position and movement

import numpy as np
from config import SAT_X, SAT_Y, SAT_HEIGHT, SAT_SPEED, SAT_STEPS, GRID_SIZE

def create_satellite():
    """
    Initialize satellite at its starting position.

    Returns:
        dict: Satellite state with position and height
    """
    satellite = {
        "x": SAT_X,
        "y": SAT_Y,
        "height": SAT_HEIGHT
    }
    print(f"[✓] Satellite initialized at ({satellite['x']}, {satellite['y']}) km, altitude {satellite['height']} km")
    return satellite

def move_satellite(satellite,steps=SAT_STEPS,speed=SAT_SPEED):
    """
    Simulate satellite movement across the grid.

    Args:
        satellite (dict): Current satellite state
        step (int): Number of movement steps to simulate
        speed (float): Movement speed in km per step

    Returns:
        list: List of satellite positions at each step (path)
    """
    
    path = []
    x,y = satellite['x'],satellite['y']
    
    for _ in range(steps):
        path.append((x,y))
        x += speed
        y += speed*0.4  # Simulate a diagonal movement with some variation
        
        x = x%GRID_SIZE
        y = y%GRID_SIZE
        
    print(f"[✓] Satellite path simulated over {steps} steps")
    return path

def get_position(satellite):
    """
    Return current (x, y, height) of satellite.

    Args:
        satellite (dict): Satellite state

    Returns:
        tuple: (x, y, height)
    """
    return satellite["x"], satellite["y"], satellite["height"]
        
        
    