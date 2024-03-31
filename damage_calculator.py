from random import randint
import imbue_manager

class Damage_calculator():
    #runs when the damage calculator is created
    def __init__(self):
        pass

    #this is where damage is calculated (fun!)
    def calculate_damage(self, dice, weapon, relic):
        base_damage = 0
        final_damage = 0
        imbue_damage_face_1 = 0
        imbue_damage_face_2 = 0
        face_1 = randint(0,5) #its 0-5 because lists are dumb and start at 0
        face_2 = randint(0,5)

        #checks for imbues
        if len(dice[0][face_1]) > 1:
            imbue_damage_face_1 = imbue_manager.calculate_imbue_damage(dice[0][face_1][1])

        if len(dice[1][face_2]) > 1:
            imbue_damage_face_2 = imbue_manager.calculate_imbue_damage(dice[1][face_2][1])

        base_damage = dice[0][face_1][0] + dice[1][face_2][0]
        final_damage = base_damage + imbue_damage_face_1 + imbue_damage_face_2

        print(f"you have an inbue that does {imbue_damage_face_1} damage")
        print(f"you have an inbue that does {imbue_damage_face_2} damage")
        print(f"face 1 = {face_1 + 1}, face 2 = {face_2 + 1}, total is = {final_damage}")

        return final_damage