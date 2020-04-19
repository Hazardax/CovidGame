from Window import Window
from Button import Button
from Text import Text
from Data import main_lib, episode_position
import pygame


text = Text(300, 200, 30)
window = Window(930, 700, "Game")


def print_text(data, text):
    text.set_text(data)
    text.print(window)


def update_buttons(buttons_list):
    for i in range(len(buttons_list)):
        if buttons_list[i].is_pressed():
            buttons_list[i].set_color((255, 0, 0, 100))
            return i
        else:
            buttons_list[i].set_color((255, 255, 255, 100))
        buttons_list[i].draw(window)


def create_check_buttons(data):
    x = 20
    y = 500
    count = 0
    main_count = 0
    buttons_list = []

    while main_count < len(data):
        if count == 2:
            count = 0
            x = 20
            y += 100
        count += 1
        main_count += 1

        x *= count * 3.55

        buttons_list.append(Button(x, y, 360, 70))

    return update_buttons(buttons_list)


def episode_func(episode_code, text):
    global episode_position
    work_data = main_lib[episode_code]
    print_text(work_data[0], text)  # print text on game window, return None
    if work_data[1]:
        num_answer = create_check_buttons(work_data[1])  # create buttons and text on them
        if num_answer is None:
            return True
    else:
        return False
    episode_position = work_data[2][num_answer]
    return True


clock = pygame.time.Clock()
run = True
while run:
    clock.tick(128)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    window.fill_window()
    window.draw_surface(0, 0)

    episode_func(episode_position, text)

    window.update()

pygame.quit()
