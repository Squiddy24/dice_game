from random import randint

class Damage_calculator():
    #runs when the damage calculator is created
    def __init__(self):
        pass

    #this is where damage is calculated (fun!)
    def calculate_damage(self, dice, weapon, *relic):
        final_damage = 0
        base_damage = 0

        face_1 = randint(0,5) #its 0-5 because lists are dumb and start at 0
        face_2 = randint(0,5)

        #checks for imbues
        if len(dice[0][face_1]) > 1:
            print("face 1 has an imbue")

        if len(dice[1][face_2]) > 1:
            print("face 2 has an imbue")
            

        base_damage = dice[0][face_1][0] + dice[1][face_2][0]

        print(f"face 1 = {face_1 + 1}, face 2 = {face_2 + 1}, total is = {base_damage}")

        pass