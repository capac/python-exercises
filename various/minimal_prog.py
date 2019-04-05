# import the pygame module, so you can use it
import pygame

# define a main function


def main():

    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("images/icon_python.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 800 x 600
    screen_width = 800
    screen_height = 600
    red, green, blue = 204, 187, 255
    screen = pygame.display.set_mode((screen_width, screen_height))
    image = pygame.image.load("images/happy.png")

    # define the position of the smiley
    xpos = 50
    ypos = 50
    # how many pixels we move our smiley each frame
    step_x = 10
    step_y = 10

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
            # check if the smiley is still on screen, if not change direction
        if xpos > screen_width - 128 or xpos < 0:
            step_x = -step_x
        if ypos > screen_height - 128 or ypos < 0:
            step_y = -step_y
        # update the position of the smiley
        xpos += step_x  # move it to the right
        ypos += step_y  # move it down

        # erase the screen
        screen.fill((red, green, blue))
        # now blit the smiley on screen
        screen.blit(image, (xpos, ypos))
        # and update the screen (don't forget that!)
        pygame.display.flip()

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
