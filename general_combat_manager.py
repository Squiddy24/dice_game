from random import randint
from enemy_stats import enemy_stats

class GCM():
    #runs when the gcm is created
    def spawn_enemy(self):
        self.enemy_select = randint(1,2) 
        if self.enemy_select  == 1:
            self.enemy_health = enemy_stats["enemy_1"]["health"]
            self.enemy_die = enemy_stats["enemy_1"]["damage"]
            self.ememy_modifier = enemy_stats["enemy_1"]["modifer"]

        elif self.enemy_select == 2:
            self.enemy_health = enemy_stats["enemy_2"]["health"]
            self.enemy_die = enemy_stats["enemy_2"]["damage"]
            self.ememy_modifier = enemy_stats["enemy_2"]["modifer"]


    #runs every frame
    def damage(self,final_damage, player):
        self.enemy_health -= final_damage 
        print(f"you dealt {final_damage} damage. The enemy has {self.enemy_health} remaning")
        if self.enemy_health <= 0:
            print("yo that dudes dead")
        else: 
            enemy_damage = self.enemy_die[randint(0,5)]
            player.health -= enemy_damage + self.ememy_modifier
            print(f"you took {enemy_damage + self.ememy_modifier} damage, you have {player.health} health left")
            
            
