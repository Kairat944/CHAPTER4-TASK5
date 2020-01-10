# Soldier Ryan has an AK47
# Soldiers can fire ("tigi-tigitishh").
# Guns can fire bullets.
# Guns can fill bullets - increase the number of bullets(reloads)

# Create class Act_of_Shooting, which will inheritates from class Soldier, class Guns.
# Where soldier will fire from a gun and reload, and fire one more time.






class Soldier():
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def fire(self):
        print('Tigi - tish')

class Guns():
    def __init__(self):
        Soldier.__init__(self)
         
    def fire_bullets(self):
        print(f'{self.name} is shooting from {self.gun}')
        self.bullets = 5
        while self.bullets >= 0:
            self.fire()
            self.bullets -= 1
            
            if self.bullets == 0:
                self.reload()

    def reload(self):
        self.choice = input('Bullets are finished, please reload your gun! if you want to fire type y!!')
        if self.choice == 'y':
            self.fire_bullets()
        else:
            pass

class Act_of_Shooting(Soldier, Guns):
    def __init__(self, name, gun):
        Soldier.__init__(self, name, gun)


Ryan = Act_of_Shooting('Rayan', 'AK47')
Ryan.fire_bullets()
