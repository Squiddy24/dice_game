from random import randint
from enemy_stats import enemy_stats
class GCM():
    #runs when the gcm is created
    def spawn_enemy(self):
        self.enemy_select = randint(1,2) 
        if self.enemy_select  == 1:
            self.enemy_health = enemy_stats["enemy_1"]["health"]
        elif self.enemy_select == 2:
            self.enemy_health = enemy_stats["enemy_2"]["health"]

    #runs every frame
    def damage(self,final_damage):
        self.enemy_health -= final_damage 
        print(f"you dealt {final_damage} damage. The enemy has {self.enemy_health} remaning")
        if self.enemy_health <= 0:
            print("yo that dudes dead")
        elif 
