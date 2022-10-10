"""

margin = alien_width 
space taken by one alien = 2 * width of an alien


availabe space in a row = width of window - margin on both side.
availabe space in a row = settings.screen.width - (2*alien_width)


number of alien in a row = available space in a row / space taken by one alien                
settings.screen.width - (2*alien.width) // (2*alien_width)

#-----------------------------------------------------------------------------------------------------

available_space_y = settings.screen.height - (3 * alien.rect.height) - ship.rect.height

number of rows = available_space_y // 2 * alien.rect.height

#-----------------------------------------------------------------------------------------------------

# 1
    def _reboot_game(self):
        ""Game starts over after a space ship is destroyed.""
        # get rid of any remaining alien or bullet 
        self.aliens.empty()
        self.bullets.empty()

        # create new fleet
        self._create_fleet()
        self.ship.center_ship()

        # pause
        sleep(0.5)

# 2

    def _restart_game(self):
        ""Game will stop because all 3 ships destroyed and ask to restart.""
        # get rid of any remaining alien or bullet 
        self.aliens.empty()
        self.bullets.empty()

        # create new fleet
        self._create_fleet()
        self.ship.center_ship()

        # pause
        sleep(0.5)

        # ship_left will be restored to 3
        self.settings.ship_limit = 3

# 3
            #################
    def _game_over(self):
        if self.settings.ship_limit == 0:
            sys.exit()
        else:
            pass














"""


# self.x = x coordinate
# self.rect.x = x coordinate of rectangle




# Using break in for loop.
'''
listt = [1,2,3,4,5,6,7,8]
for i in listt:
    if i % 2 == 0:
        print('even',i)
        break
'''
# added by myself

# method: game_over
# method: reboot_game
# used method:  sys.exit() game will exit when ship left == 0



dict = {'fname':['sunyog','lodhi','suyog','lodhi']}

for key in dict.values():
    print(key) 