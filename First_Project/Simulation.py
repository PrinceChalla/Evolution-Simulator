import random
import time

import pygame
pygame.init()

saturation_point = 6
Redemption_Probability = 0.0005
genome = []
serialno = 1
serialno_2 = 1


light_purple = (120,0,120)
yellow = (225,225,0)
red = (225,0,0)
green = (0,225,0)
blue = (0,0,225)


file_name = "Report.txt"
file_name2 = "Genome_History.txt"


# will be in the format dna = [class,colour,speed,no of offspring,size]
#dna = [1,1,1,2,1,30]


time_elased_since_init = time.time() 
timer_setter = time.time()

screen = pygame.display.set_mode((1000,1000),pygame.RESIZABLE)

class herbivore(pygame.sprite.Sprite):
    def __init__(self,colour,speed,no_of_offspring,size,lifespan,dna,*groups):
        super().__init__(*groups)
        self.image = pygame.Surface((30*size,30*size))
        self.image.fill(light_purple)
        pygame.draw.circle(self.image,(colour),(15*size,15*size),15*size)
        self.rect = self.image.get_rect()
        self.rect.center = ((screen.get_width()/2),(screen.get_height()/2))
        #self.numbers = [-6,-3,3,6]
        self.numbers = [-6*speed,6*speed]
        self.time_created = time.time()
        self.lifespan = lifespan
        self.dna = dna
        self.stamina = 0
    def update(self):
       
        self.rect.x += random.choice(self.numbers) * dt
        self.rect.y += random.choice(self.numbers) * dt
        if (screen.get_width() < self.rect.x) or (self.rect.x < 0)  :
             self.rect.x = ((screen.get_width()/2))
        if(screen.get_height() < self.rect.y) or (self.rect.y < 0) :
            self.rect.y = ((screen.get_height()/2))

        
        self.check_collisions_with_trees()
        self.reproduce(time.time())

    def reproduce(self,time_now):
        if time_now - self.time_created > self.lifespan :
            if self.stamina < 2 :
                self.kill()
                
            else :
                replicate(self.dna)
                self.time_created = time_now
                self.stamina = 0

    def check_collisions_with_trees(self) :
        if pygame.sprite.spritecollide(self,tree_group,True):
            self.stamina +=1



class tree (pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        position_x = random.randrange(0,screen.get_width())
        position_y = random.randrange(0,screen.get_height())
        self.image = pygame.Surface((2,2))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.center = (position_x,position_y)
        


class carnivore(pygame.sprite.Sprite):
    def __init__(self,colour,speed,no_of_offspring,size,lifespan,dna,*groups):
        super().__init__(*groups)
        self.image = pygame.Surface((20*size,20*size))
        self.colour = colour
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.center = ((screen.get_width()/2),(screen.get_height()/2))
        #self.numbers = ([-10*speed,-6*speed,6*speed,10*speed])
        self.numbers = ([-6*speed,6*speed])
        self.time_created = time.time()
        self.lifespan = lifespan
        self.dna = dna
        self.stamina = 0
    def update(self):
        
        self.rect.x += random.choice(self.numbers) * dt
        self.rect.y += random.choice(self.numbers)*  dt
        if (screen.get_width() < self.rect.x) or (self.rect.x < 0)  :
             self.rect.x = ((screen.get_width()/2))
        if(screen.get_height() < self.rect.y) or (self.rect.y < 0) :
            self.rect.y = ((screen.get_height()/2))

        self.check_collisions_with_herbivores()
        self.reproduce(time.time())
    def reproduce(self,time_now):
        if time_now - self.time_created > self.lifespan :
            if self.stamina < 5 :
                self.kill()
                
            else :
                replicate(self.dna)
                self.time_created = time_now
                self.stamina = 0

    def check_collisions_with_herbivores(self):
        if self.stamina < saturation_point :
            if self.colour == red:
                if pygame.sprite.spritecollide(self,red_herbivore_group,True):
                    self.stamina += 1
                    


            elif self.colour == blue:
                if pygame.sprite.spritecollide(self,blue_herbivore_group,True):
                    self.stamina += 1
                    

            elif self.colour == yellow:
                if pygame.sprite.spritecollide(self,yellow_herbivore_group,True):
                    self.stamina += 1
                

    


no_of_added_trees = 0
tree_group = pygame.sprite.Group()


Herbivore = herbivore(red,2,2,1,5,[1,1,2,2,1,5])

herbivore_group = pygame.sprite.Group()
herbivore_group.add(Herbivore)

# run this code to start the world with a carnivore ( Not Stable )

# Defining general carnivore group

carnivore_group = pygame.sprite.Group()
#Carnivore = carnivore(blue,2,2,1,5,[2,3,2,2,1,5])
#carnivore_group.add(Carnivore)


# creating the groups for herbivores
red_herbivore_group = pygame.sprite.Group()
blue_herbivore_group = pygame.sprite.Group()
yellow_herbivore_group = pygame.sprite.Group()

# Creating the group for carnivores
red_carnivore_group = pygame.sprite.Group()
blue_carnivore_group = pygame.sprite.Group()
yellow_carnivore_group = pygame.sprite.Group()




clock = pygame.time.Clock()
running = True
dt = 0

def replicate(dna):
    print(dna)
    save2()
    global genome
    genome = dna
    if random.random() < 0.01 :
        dna[0]= random.choice([1,2])

    if random.random() < 0.05 :
        dna[1] = random.randrange(1,4)

    if random.random() < 0.01 :
        dna[2] = (random.uniform(0.7,1.3))*dna[2]
        #dna[2] = random.choice(((dna[2])*1.3),((dna[2])*0.7))

    if random.random() < 0.01 :
        dna[3] = (random.randrange(-1,2)) + dna[3]
        #dna[3] = random.choice(((dna[3])+1),((dna[3])-1))

    if random.random() < 0.01 :
        dna[4] = (random.uniform(0.7,1.3))*dna[4]

    if random.random()< 0.01 :
        dna[5] = (random.randrange(-10,11)) + dna[5]
       # dna[5] = random.choice(((dna[5])-10),((dna[5])+10))

    category = dna[0]

    if dna[1] == 1 :
        organism_colour = red
    elif dna[1] ==2 :
        organism_colour = yellow
    else :
        organism_colour = blue

    speed = dna[2]
    fertility = dna[3]
    size = dna[4]
    organism_lifespan = dna[5]
    organism_dna = [dna[0],dna[1],dna[2],dna[3],dna[4],dna[5]]
    if category == 1 :
        organism = herbivore(organism_colour,speed,fertility,size,organism_lifespan,organism_dna)
        herbivore_group.add(organism)
        if organism_colour == red :
            red_herbivore_group.add(organism)
        elif organism_colour == blue :
            blue_herbivore_group.add(organism)
        elif organism_colour == yellow :
            yellow_herbivore_group.add(organism)    
    elif category == 2 :
        organism = carnivore(organism_colour,speed,fertility,size,organism_lifespan,organism_dna) 
        carnivore_group.add(organism)
        if organism_colour == red :
            red_carnivore_group.add(organism)
        elif organism_colour == blue :
            blue_carnivore_group.add(organism)
        elif organism_colour == yellow :
            yellow_carnivore_group.add(organism)    

    
def save():
    global serialno
    file = open(file_name,"a")
    
    Combined_herbivore_dna_list = []
    Combined_carnivore_dna_list = []

    for i in herbivore_group :
        Combined_herbivore_dna_list.append(i.dna)


    for i in carnivore_group :
        Combined_carnivore_dna_list.append(i.dna)


    len_Combined_herbivore_dna_list = len(Combined_herbivore_dna_list)
    len_Combined_carnivore_dna_list = len(Combined_carnivore_dna_list)
    
    combined_list_for_herbivores = [
    sum(values) / len_Combined_herbivore_dna_list  # Compute the mean for each position
    for values in zip(*Combined_herbivore_dna_list)  # Zip to combine corresponding elements
]


    combined_list_for_carnivores = [
    sum(values) / len_Combined_carnivore_dna_list  # Compute the mean for each position
    for values in zip(*Combined_carnivore_dna_list)  # Zip to combine corresponding elements
]

    save_dictionary = {"Serial No": serialno,
    "Time elapsed since run":time_elapsed_since_run,
    "No of Red Herbivores":len(red_herbivore_group),
    "No of Blue Herbivores":len(blue_herbivore_group),
    "No of Yellow Herbivores":len(yellow_herbivore_group),
    "Total No of Herbivores":len(herbivore_group),
    "Average Herbivore DNA":combined_list_for_herbivores,
    "No of Red Carnivores":len(red_carnivore_group),
    "No of Blue Carnivores":len(blue_carnivore_group),
    "No of Yellow Carnivores":len(yellow_carnivore_group),
    "Total No of Carnivores":len(carnivore_group),
    "Average Carnivore DNA":combined_list_for_carnivores,
    "Total No of Organisms":len(herbivore_group)+len(carnivore_group)}


    file.write((str(save_dictionary))+"\n")
    file.close()

    serialno += 1

    
def save2():
    global serialno_2
    file_2 = open(file_name2,"a")
    file_2.write((str({"Serial No":serialno_2,"Time elapsed since run":time_elapsed_since_run,"Genome":genome})) + "\n")
    file_2.close()
    serialno_2 += 1



file = open(file_name,"a")
file.write(str(time.ctime())+"\n"+"\n")
file.close()
file_2 = open(file_name2,"a")
file_2.write(str(time.ctime())+"\n"+"\n")
file_2.close()




while running:

    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(light_purple)



    time_now = time.time()


    time_elapsed_since_run = time_now - time_elased_since_init


        
    if len(tree_group) < 10000 :
        Tree = tree()
        tree_group.add(Tree)



    if random.random() < Redemption_Probability :
        Messiah = herbivore(random.choice([red,blue,yellow]),2,2,1,5,[1,random.choice([1,2,3]),2,2,1,5])
        herbivore_group.add(Messiah)


# updating sprites and drawing them
    tree_group.draw(screen)
    herbivore_group.update()
    herbivore_group.draw(screen)

    carnivore_group.update()
    carnivore_group.draw(screen)

#Collision detection and kill


    # flip() the display to put your work on screen
    pygame.display.flip()


    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 20
    timer = time_now - timer_setter
    if timer >= 1 :
        save()
        timer_setter = time_now

pygame.quit()
