from collections import deque
from random import randint, choice
def time_str(value:int|float) -> str:
    '''Returns string of time'''
    hours, minutes= divmod(value, 60)
    if hours < 12:
        meridiem = ' AM'
    elif hours > 23:
        hours %= 12
        meridiem = ' AM'
    else:
        hours %= 12
        meridiem = ' PM'
    return f"{int(hours)}:{minutes if minutes >= 10 else f'0{minutes}'}" + meridiem

class FSM:
    '''Finite-state machine'''
    def __init__(self, start) -> None:
        self.events = deque([start])

    def add_event(self, e:object):
        '''Add event to the events'''
        self.events.appendleft(e)

    def pop(self):
        '''Deletes last element and returns function'''
        return self.events.pop()()

    @property
    def peek(self):
        '''Smth like peek'''
        return self.events[-1]

    def __str__(self) -> str:
        return f'Queue={self.events}'

    def __repr__(self) -> str:
        return f'{self.events}'

class Student:
    '''Me'''
    time = 0
    def __init__(self) -> None:
        self.day = FSM(self.sleep)
        self.health = 100
        self.hunger = 0
        self.energy = 0
        self.weather = None
        self.state = self.day.peek
        self.home = False

    def my_day(self):
        '''My day'''
        while self.day.events:
            self.day.pop()

    def play(self):
        '''Play games'''
        print(f'\nTime: {time_str(self.time)}, \
Hunger: {self.hunger}, Energy: {self.energy}')
        print('Hmm... what should i play...')
        game = choice(['Brawl Stars', 'Clash Royale', 'Valheim', 'Sea of Thieves'])
        print(f'{game} les gooo!')
        match game:
            case 'Brawl Stars':
                self.hunger += 15
                self.energy -= 5
                self.time += 40
            case 'Brawl Stars':
                self.hunger += 20
                self.energy -= 10
                self.time += 20
            case 'Valheim':
                self.hunger += 30
                self.energy -= 30
                self.time += 90
            case 'Sea of Thieves':
                self.hunger += 50
                self.energy -= 50
                self.time += 180
        self.state = self.study
        self.day.add_event(self.state)

    def shower(self):
        '''Taking shower'''
        print(f'\nTime: {time_str(self.time)}, \
Hunger: {self.hunger}, Energy: {self.energy}')
        print(choice(['Time to take a shower!', "Ughh... i'm stinky, i need a wash"]))
        print('... '.join(['washing']*3))
        self.energy += 10
        self.hunger += 5
        self.time += 30
        self.state = self.at_home
        self.day.add_event(self.state)

    def at_home(self):
        '''Time at home'''
        print(f'\nTime: {time_str(self.time)}, \
Hunger: {self.hunger}, Energy: {self.energy}')
        if self.home is False:
            print("Finally I'm at home")
            self.home = True
        else:
            print('I gotta do something')
        if self.time >= 1320:
            print('\nahhhh-hhaaaaaa')
            print('I think i gotta go for a sleep\n')
            self.state = self.sleep
            self.day.add_event(self.state)
        elif self.energy < 60 < self.hunger:
            self.state = self.eat
            self.day.add_event(self.state)
        else:
            random = randint(1,8)
            if random == 3:
                print('I have some free time')
                self.time += 90
                self.hunger += 25
                self.energy += 15
                self.day.add_event(self.state)
            elif random == 5:
                self.state = self.shower
                self.day.add_event(self.state)
            else:
                self.state = self.study
                self.day.add_event(self.study)

    def ice_cream(self):
        '''Walk with ice cream'''
        print(f'\nTime: {time_str(self.time)}, \
Hunger: {self.hunger}, Energy: {self.energy}')
        print('Nice weather and no ice cream?')
        print('No way bro...')
        self.time += 20
        self.energy -= randint(4, 8)
        self.hunger -= 5
        self.state = self.at_home
        self.day.add_event(self.state)

    def walk_with_ps(self):
        '''Walk in park with pan Stepan'''
        print(f'\nTime: {time_str(self.time)}, \
Hunger: {self.hunger}, Energy: {self.energy}')
        print('What a good day to walk with pan Stepan')
        self.energy += 5
        self.hunger += 20
        self.time += 30
        self.state = self.at_home
        self.day.add_event(self.state)

    def walk_in_park(self):
        '''Walk in park with friends'''
        print(f'\nTime: {time_str(self.time)}, \
Hunger: {self.hunger}, Energy: {self.energy}')
        print('Another day, another walk with besties')
        self.energy += 5
        self.hunger += 20
        self.time += 60
        if randint(1,4) == 4 and self.weather == 'warm':
            self.state = self.ice_cream
            self.day.add_event(self.state)
        else:
            self.state = self.at_home
            self.day.add_event(self.state)

    def study(self):
        '''Study state'''
        print(f'\nTime: {time_str(self.time)}, \
Hunger: {self.hunger}, Energy: {self.energy}')
        print(choice(['Time to study!', 'Study again...', 'STUDYYYY!!!!']))
        self.hunger += randint(10, 15)
        self.energy -= randint(25,35)
        self.time += 80
        if self.time in range(780, 860):
            random = randint(1,5)
            if random == 2 and self.weather in ['warm', 'overcast']:
                self.state = self.walk_with_ps
                self.day.add_event(self.state)
            elif random == 4 and self.weather in ['warm', 'overcast']:
                self.state = self.walk_in_park
                self.day.add_event(self.state)
            else:
                print(choice(['Time to go home!', "I'm too sleepy, i'm going home", \
                    'Hmm... I wonder if the bus is close']))
                self.state = self.at_home
                self.day.add_event(self.at_home)

        elif self.energy < 30 or 80 < self.hunger:
            self.state = self.eat
            self.day.add_event(self.state)

        elif self.time > 900:
            if randint(1,3) == 2:
                print("Nah, I don't wanna study, games les go")
                self.state = self.play
                self.day.add_event(self.state)
            else:
                self.day.add_event(self.study)
        else:
            self.day.add_event(self.study)

    def eat(self):
        '''Eat state'''
        print(f'\nTime: {time_str(self.time)}, \
Hunger: {self.hunger}, Energy: {self.energy}')
        print('Hmm... what i gonna eat?')
        eat = []
        if self.time <= 480:
            eat.append('coffee')
            if self.hunger >= 55:
                eat.append('scrambled eggs and salad')
                self.energy += randint(6, 8)
                self.time += 25
                self.hunger -= randint(10, 15)
            else:
                eat.append('cookies')
                self.energy += randint(3, 7)
                self.hunger -= randint(3, 7)
                self.time += 15
            self.time += 60
        else:
            if self.time >= 750:
                if randint(1,2) == 1:
                    print("I'm not too hungry")
                    eat.append('tea')
                    eat.append('cookies')
                    self.hunger -= randint(4, 8)
                    self.energy += randint(8, 12)
                    self.time += 30
                else:
                    print('Refreshment time!!!')
                    eat.append(choice(['mashed potato', 'rice', 'pasta']))
                    eat.append(choice(['cutlets', 'meatballs']))
                    self.energy += randint(12, 16)
                    self.hunger -= randint(15, 20)
                    self.time += 60
            else:
                if randint(1,2) == 1:
                    print("Let's go to trapezna")
                    eat.append(choice(['rice', 'pasta', 'buckwheat', 'mashed potatoes']))
                    eat.append(choice(['chicken breast', 'pork kebab', 'pork chop']))
                    self.energy += randint(12, 16)
                    self.hunger -= randint(15, 20)
                    self.time += 50
                else:
                    print("Cafeteria time!")
                    eat.append(choice(['latte', 'cappuccino', 'cream coffee']))
                    if randint(1,5) == 3:
                        eat.append(choice(['spartak', 'muffin', 'macaroons']))
                        self.energy += 15
                        self.hunger -= randint(8, 12)
                    self.energy += 10
                    self.hunger -= randint(2, 4)
                    self.time += 30
        if self.hunger < 0:
            self.hunger = 0
        elif self.hunger > 100:
            self.hunger = 100
        if self.energy < 0:
            self.energy = 0
        elif self.energy > 100:
            self.energy = 100
        if self.energy < 40 or self.hunger > 70:
            self.day.add_event(self.eat)
        else:
            print(f'Food: {", ".join(eat)}')
            if self.time >= 760:
                self.state = self.at_home
                self.day.add_event(self.state)
            else:
                self.state = self.study
                self.day.add_event(self.state)

    def get_dressed(self):
        '''Getting dressed'''
        print(f'\nTime: {time_str(self.time)}, \
Hunger: {self.hunger}, Energy: {self.energy}')
        self.weather = choice(['warm', 'rainy', 'overcast'])
        match self.weather:
            case 'warm':
                outfit_theme = 'white'
            case 'rainy':
                outfit_theme = 'black'
            case 'overcast':
                outfit_theme = choice(['black', 'white_cold'])

        match outfit_theme:
            case 'black':
                print("Outfit: jacket, black-colored T-shirt, sport pants, sneakers")
            case 'white':
                print("Outfit: shirt, shorts, white sneakers")
            case 'white_cold':
                print("Outfit: blazer, shirt, shorts, white sneakers")

        self.time += 10
        self.energy -= 5
        self.hunger += randint(4, 8)
        self.state = self.eat
        self.day.add_event(self.state)

    def washing(self):
        '''Washing'''
        print("I'm washing my face and brush my teeth...")
        if randint(1,4) == 2:
            print("I'm shaving...")
            self.time += 5
        self.energy += 5
        self.time += 5
        self.hunger += randint(4, 8)
        self.state = self.get_dressed
        self.day.add_event(self.state)

    def dream(self):
        '''Dream'''
        random = randint(1,10)
        if random == 1:
            print("I fall asleep planning my next day's labor\n\
and in my dreams I complete it,\n\
hewing wood, foraging for food and hunting after swift deer.\n\
I return home exhausted but happy, only to awaken and find the day is still ahead of I... ")
        elif random == 2:
            print("I dream of a mighty bear,\n\
sleeping deep below the earth in the winter of the world.\n\
It turns in its sleep, folds upon folds of flesh and fur. It has no head, no limbs.\n\
A vast mass of bear flesh, mercifully quiet. ")
        elif random == 3:
            print("I dream I am walking in a snowy wood \n\
when I come upon a naked child,\n\
sitting against a tree with his eyes closed but his chest moving to breathe.\n\
As I kneel beside him, I know he has been sleeping here for many centuries,\n\
waiting for I. When I touch his shoulder, we both awaken. ")
        elif random == 4:
            print("I dream I am hunting with my companions,\n\
running high over green hills and down through mist-haunted valleys.\n\
Ahead of I, my prey stumbles and I leap forward, sinking my teeth into warm flesh.\n\
When I wake, the taste of metal lingers in my mouth. ")
        elif random == 5:
            print("Sleep is a river and dreams are live fish.\n\
I wake in the morning with my net empty. ")
        elif random == 6:
            print("I sleep in fits and fretful dreams, \n\
the weight of the nightmare heavy on my chest. \n\
When morning comes, I greet it with relief.")
        elif random == 7:
            print("I dream of a bright hall filled with \n\
gracious warriors and fair maidens.\n\
The air hums with song, the boards groan under the weight of steaming dishes,\n\
the mead flows like water. I awake slowly with the laughter still ringing in my ears… ")
        elif random == 8:
            print("I fall into the deep well of sleep \n\
and dream only of darkness.")
        elif random == 9:
            print("I lie on the battlefield, \n\
dreaming eyes turned upward to a sky veiled by smoke. \n\
The calls of my warriors grow fainter and my eyes close for a second time.\n\
Great talons slide beneath I and I feel myself rising, \n\
lifted from my body like a babe from its crib… ")
        elif random == 10:
            print("On a boat carved from dark wood, \n\
beneath ragged sails, I lie with my arms folded across my chest.\n\
Blurred faces, like thumbprints on the darkness, croon familiar songs\n\
as they push I out to float on a sea as black and flat as glass. ")
        print()

    def sleep(self):
        '''sleep state'''
        if self.time == 420:
            print(f'Time: {time_str(self.time)}, \
Hunger: {self.hunger}, Energy: {self.energy}')
            self.state = self.washing
            self.day.add_event(self.state)
        else:
            print(f'Time: {time_str(self.time)}, \
Hunger: {self.hunger}, Energy: {self.energy}')
            print('ZZZzzzz.....\n')
            self.hunger += randint(4, 8)
            self.energy += 10
            if self.time >= 1320:
                print('Best end of the best day')
            else:
                if randint(1,6) == 4:
                    print('I have a dream\n')
                    self.state = self.dream
                    self.day.add_event(self.state)
                self.day.add_event(self.sleep)
                self.time += 60

if __name__ == '__main__':
    me = Student()
    me.my_day()
