import json
import pygame


def color_map_f():


    # Load color map from JSON file
    with open('./colors_map.json', 'r') as file:
        json_color_map = json.load(file)

    color_map_f = {
        pygame.K_F1: tuple(json_color_map["F1"]),
        pygame.K_F2: tuple(json_color_map["F2"]),
        pygame.K_F3: tuple(json_color_map["F3"]),
        pygame.K_F4: tuple(json_color_map["F4"]),
        pygame.K_F5: tuple(json_color_map["F5"]),
        pygame.K_F6: tuple(json_color_map["F6"]),
        pygame.K_F7: tuple(json_color_map["F7"]),
        pygame.K_F8: tuple(json_color_map["F8"]),
        pygame.K_F9: tuple(json_color_map["F9"]),
        pygame.K_F10: tuple(json_color_map["F10"]),
        pygame.K_F11: tuple(json_color_map["F11"]),
        pygame.K_1: tuple(json_color_map["1"]),
        pygame.K_2: tuple(json_color_map["2"]),
        pygame.K_3: tuple(json_color_map["3"]),
        pygame.K_4: tuple(json_color_map["4"]),
        pygame.K_5: tuple(json_color_map["5"]),
        pygame.K_6: tuple(json_color_map["6"]),
        pygame.K_7: tuple(json_color_map["7"]),
        pygame.K_8: tuple(json_color_map["8"]),
        pygame.K_9: tuple(json_color_map["9"]),
        pygame.K_0: tuple(json_color_map["0"])
    }

    return color_map_f


