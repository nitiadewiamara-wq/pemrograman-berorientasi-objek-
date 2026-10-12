class Hero:
    # Class variable
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # Instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1

    # Method tanpa parameter tambahan
    def siapa(self):
        return f"{self.name} memiliki power {self.power}"

    # Method dengan parameter tanpa return eksplisit
    def healthUp(self, up):
        self.health += up

    # Method dengan return
    def gethealth(self):
        return self.health

    # Method dengan parameter dan return
    def serang(self, lawan):
        damage = self.power - lawan.armor

        if damage < 0:
            damage = 0

        lawan.health -= damage

        return f"{self.name} menyerang {lawan.name} dengan damage {damage}"


# Membuat objek hero
hero1 = Hero("Sniper", 100, 10, 5)
hero2 = Hero("Axe", 200, 15, 0)

# Menampilkan informasi hero
print(hero1.siapa())

# Mengubah armor hero
hero1.armor = 10
print(f"Armor {hero1.name} = {hero1.armor}")

# Menampilkan jumlah hero
print(f"Jumlah hero = {Hero.jumlah}")

# Menambah health hero
hero1.healthUp(20)
print(f"Health {hero1.name} = {hero1.gethealth()}")
print(f"Health {hero2.name} = {hero2.gethealth()}")

# Menyerang lawan
print(hero1.serang(hero2))
print(f"Health {hero2.name} setelah diserang = {hero2.gethealth()}")

