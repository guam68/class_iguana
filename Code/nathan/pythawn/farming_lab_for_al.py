class Farmer:
    def __init__(self, energy, filth, day_light, milk, milk_val, eggs, eggs_val, bacon, bacon_val, money, wallet, cow_price, cow_count, pig_price, pig_count, coop_price, coop_count):
        self.energy = energy
        self.filth = filth
        self.day_light = day_light
        self.milk = milk
        self.milk_val = milk_val
        self.eggs = eggs
        self.eggs_val = eggs_val
        self.bacon = bacon
        self.bacon_val = bacon_val
        self.money = money
        self.wallet = wallet
        self.cow_price = cow_price
        self.cow_count = cow_count
        self.pig_price = pig_price
        self.pig_count = pig_count
        self.coop_price = coop_price
        self.coop_count = coop_count

    def farm(self):
        self.day_light = self.day_light - 2
        self.filth = self.filth + 1
        self.energy = self.energy - 1
        if self.energy <= 0 or self.day_light <= 0:
            print('You ran out of energy and died')
            exit()
        if self.filth > 5:
            print('You got so stinky all the animals left you')
            exit()
        else:
            return f'energy: {self.energy}, filth: {self.filth}, day light: {self.day_light}'

    def bathe(self):
        self.day_light = self.day_light - 1
        self.filth = 0
        if self.energy <= 0 or self.day_light <= 0:
            print('You ran out of energy and died')
            exit()
        else:
            return f'energy: {self.energy}, filth: {self.filth}, day light: {self.day_light}'

    def sleep(self):
        self.day_light = 10
        self.energy = 5
        return f'energy: {self.energy}, filth: {self.filth}, day light: {self.day_light}'

    def milk_cow(self):
        self.milk += self.milk_val
        return f'You have {self.milk} gallon of milk'

    def farm_chicken(self):
        self.eggs += self.eggs_val
        return f'You have {self.eggs} eggs'

    def make_bacon(self):
        self.bacon += self.bacon_val
        return f'You have {self.bacon} pounds of bacon'

    def make_money(self):
        if self.money == 0:
            self.milk *= 3
            self.bacon *= 4
            self.money += self.milk + self.eggs + self.bacon
            self.wallet += self.money
            return f'you made {self.money} dollars'
        if self.money != 0:
            self.money = 0
            self.milk = 0
            self.bacon = 0
            self.eggs = 0
            return self.money, self.milk, self.bacon, self.eggs

    def check_wallet(self):
        return f'{self.wallet} dollars'

    def new_cow(self):
        if self.wallet < self.cow_price:
            print(f'you do not have enough money, you need ${self.cow_price}. keep on farming')
        elif self.wallet >= self.cow_price:
            self.milk_val += 5
            self.cow_count += 1
            self.wallet -= self.cow_price
            self.cow_price *= 2
            return f' you now have {self.cow_count} cow(s), and make {self.milk_val} gallons of milk per farming. ${self.wallet} left'

    def new_pig(self):
        if self.wallet < self.pig_price:
            print(f'you do not have enough money, you need ${self.pig_price}. keep on farming')
        elif self.wallet >= self.pig_price:
            self.bacon_val += 24
            self.pig_count += 1
            self.wallet -= self.pig_price
            self.pig_price *= 2
            return f' you now have {self.pig_count} pig(s), and make {self.bacon_val} pounds of bacon per farming. ${self.wallet} left'

    def upgrade_chicken_coop(self):
        if self.wallet < self.coop_price:
            print(f'you do not have enough money, you need ${self.coop_price}. keep on farming')
        elif self.wallet >= self.coop_price:
            self.eggs_val += 120
            self.coop_count += 1
            self.wallet -= self.coop_price
            self.coop_price *= 2
            return f' you now gain {self.eggs_val} eggs per farming. ${self.wallet} left'


print('you are just a simple farmer and you heart is on the farm')
print('you can take a farmer from the farm but you can never take a farm from the farmer\n...')
farmer = Farmer(5, 0, 10, 0, 5, 0, 12, 0, 24, 0, 0, 500, 1, 750, 1, 1000, 0)
while True:
    task = input('\nHowdy, what would you like to do?\n(farm)\n(bathe)\n(sleep)\n(sell)\n(store)\n(check wallet)\n**type \'city boy\' to leave the farm**\n>')
    if task == 'farm':
        print(farmer.farm())
        animal = input('which animal are you looking to farm?\n(cow)\n(chicken)\n(pig)\n>')
        if animal == 'cow':
            print(farmer.milk_cow())
        elif animal == 'chicken':
            print(farmer.farm_chicken())
        elif animal == 'pig':
            print(farmer.make_bacon())
    elif task == 'bathe':
        print(farmer.bathe())
    elif task == 'sleep':
        print(farmer.sleep())
    elif task == 'sell':
        print(farmer.make_money())
        farmer.make_money()
    elif task == 'store':
        purchases = input(f'What would you like to buy:\n${farmer.cow_price}(new cow)\n${farmer.pig_price}(new pig)\n${farmer.coop_price}(chicken coop upgrade)\n>')
        if purchases == 'new cow':
            print(farmer.new_cow())
        elif purchases == 'new pig':
            print(farmer.new_pig())
        elif purchases == 'chicken coop upgrade':
            print(farmer.upgrade_chicken_coop())
    elif task == 'check wallet':
        print(farmer.check_wallet())
    elif task == 'city boy':
        print('Thank you, come again')
        break



