import pygame
pygame.init()
window = pygame.display.set_mode((1200,400))
track = pygame.image.load('track6.png')
car = pygame.image.load('tesla.png')

#resize the car to the size of the road
car = pygame.transform.scale(car,(30, 60)) # number is dimension
# postion of the car in the whole image
car_x = 155
car_Y = 300
focal_dis = 25 # camera focal distance
cam_x_offset = 0
cam_y_offset = 0
direction = 'up'
drive = True
clock = pygame.time.Clock()
while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    clock.tick(60)
    cam_x = car_x + cam_x_offset + 15# camera go 15 pixel inside the car
    cam_y = car_Y + cam_y_offset + 15

    # to get the pixel of the road to detect the road
    up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
    right_px = window.get_at((cam_x + focal_dis, cam_y))[0]
    print(up_px, right_px, down_px)
    #change of the direction (take turn)
    if direction == 'up' and up_px != 255 and right_px == 255:
        direction = 'right'
        #rotate camera
        cam_x_offset = 30
        #to rotate our car
        car =  pygame.transform.rotate(car, -90)
    # change direction to down
    elif direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        car_x = car_x + 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'down' and down_px != 255 and right_px == 255:
        direction = 'right'
        car_Y = car_Y + 30
        cam_x_offset = 30
        cam_y_offset = 0
        car = pygame.transform.rotate(car, 90)
    elif direction == 'right' and right_px != 255 and up_px == 255:
        direction = 'up'
        car_x = car_x + 30
        cam_x_offset = 0
        car = pygame.transform.rotate(car, 90)

    #DRIVE
    #Condition if only the white(255)  car should run
    if direction == 'up' and up_px == 255:
        car_Y = car_Y - 2 # this is used to run the car
    #move car to x axis
    elif direction == 'right' and right_px == 255:
        car_x = car_x + 2
    #move car in y axis toward down direction
    elif direction == 'down' and down_px == 255:
        car_Y = car_Y + 2

    # move car toward downside
    window.blit(track, (0,0)) # (0,0 ) is the position of the image
    window.blit(car,(car_x, car_Y))  #this is used to move the car
    pygame.draw.circle(window,(0, 255, 0), (cam_x, cam_y), 5, 5)  # 5,5 is the radix and width of the circle
    pygame.display.update()



