import tank_wars_iit.examples as examples
import tank_wars_iit.scenario as scenario
from tank_wars_iit import Controller, ControllerAction, ControllerState
import tank_wars_iit.util as util
import pygame
from random import random

#import random

class HoomanController(Controller):
    name = "HoomanTank"
    body_color = "#DDDDDD"
    head_color = "#AAAAAA"
    def __init__(self):
    	self.prevPosition = [0,0]
    def act(self, state: ControllerState) -> ControllerAction:
        action = ControllerAction()
        action.move_toward = state.coin_position
        action.move_power = 1
        #action.move_toward = None
        print(state.position)
        print(self.prevPosition)
        distance = util.distance(self.prevPosition[0], self.prevPosition[1], state.position[0], state.position[1])
        if int(distance) == 0:
            print("Hil Nahi Raha hu maii........")
            action.move_power = -1.0
            action.turn_power = 0.5
            action.turn_toward = state.coin_position
            action.move_toward = (self.prevPosition[0] * 0.5, self.prevPosition[1] * 0.5)
            action.turret_turn_power = 1

        self.prevPosition =  state.position

        state.shot_cooldown = 0
        #print(state.enemy_position[0])

        # Shoot
        #distance = util.distance(state)
        if state.can_see_enemy:
            action.aim_toward = state.enemy_position
            action.shoot = True

        return action

scenario.one_vs_one(HoomanController, examples.AggressiveController)