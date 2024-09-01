from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
# レイヤーの色設定

# Blender
LAYER_1_COLOR_ORANGE = (255, 128, 0)
LAYER_1_COLOR_BLUE = (0, 109, 143)

LAYER_1 = {
    'name': 'LAYER_1',
    'color_map': {
        1: LAYER_1_COLOR_ORANGE, 3: LAYER_1_COLOR_ORANGE, 4: LAYER_1_COLOR_ORANGE,
        5: LAYER_1_COLOR_ORANGE, 6: LAYER_1_COLOR_ORANGE, 8: LAYER_1_COLOR_ORANGE,
        10: LAYER_1_COLOR_ORANGE, 11: LAYER_1_COLOR_ORANGE, 12: LAYER_1_COLOR_ORANGE,
        13: LAYER_1_COLOR_ORANGE, 14: LAYER_1_COLOR_ORANGE, 9: LAYER_1_COLOR_BLUE
    },
    'keycodes': [
        None, Keycode.B, (Keycode.CONTROL, Keycode.C), (Keycode.CONTROL, Keycode.V),
        (Keycode.CONTROL, Keycode.KEYPAD_THREE), Keycode.F, Keycode.G, Keycode.H,
        Keycode.KEYPAD_ONE, Keycode.KEYPAD_SEVEN, Keycode.K, Keycode.L,
        Keycode.KEYPAD_THREE, Keycode.KEYPAD_PERIOD, Keycode.O, Keycode.P
    ]
}

#MagicaVoxel
LAYER_2_COLOR_PURPLE = (53, 2, 87)
LAYER_2_COLOR_PURPLE2 = (255, 157, 0)
LAYER_2_COLOR_PURPLE3 = (255, 198, 194)

LAYER_2 = {
    'name': 'LAYER_2',
    'color_map': {
        0: LAYER_2_COLOR_PURPLE, 1: LAYER_2_COLOR_PURPLE, 2: LAYER_2_COLOR_PURPLE,
        3: LAYER_2_COLOR_PURPLE, 6: LAYER_2_COLOR_PURPLE, 10: LAYER_2_COLOR_PURPLE,
        12: LAYER_2_COLOR_PURPLE, 13: LAYER_2_COLOR_PURPLE, 14: LAYER_2_COLOR_PURPLE,
        15: LAYER_2_COLOR_PURPLE, 4: LAYER_2_COLOR_PURPLE2, 8: LAYER_2_COLOR_PURPLE2,
        5: LAYER_2_COLOR_PURPLE3, 9: LAYER_2_COLOR_PURPLE3
    },
    'keycodes': [
        None, Keycode.TWO, Keycode.THREE, Keycode.FOUR,
        Keycode.LEFT_ARROW, Keycode.PAGE_DOWN, Keycode.THREE, Keycode.MINUS,
        Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.F2, Keycode.F2,
        Keycode.RIGHT_ARROW, Keycode.PAGE_UP, Keycode.EIGHT, Keycode.EQUALS
    ]
}

# None
LAYER_3_COLOR_1 = (120, 155, 0)
LAYER_3_COLOR_2 = (5, 255, 220)

LAYER_3 = {
    'name': 'LAYER_3',
    'color_map': {
        0: LAYER_3_COLOR_1, 1: LAYER_3_COLOR_1, 2: LAYER_3_COLOR_1, 3: LAYER_3_COLOR_1,
        4: LAYER_3_COLOR_2, 5: LAYER_3_COLOR_2, 6: LAYER_3_COLOR_2, 7: LAYER_3_COLOR_2,
        8: LAYER_3_COLOR_1, 9: LAYER_3_COLOR_1, 10: LAYER_3_COLOR_1, 11: LAYER_3_COLOR_1,
        12: LAYER_3_COLOR_2, 13: LAYER_3_COLOR_2, 14: LAYER_3_COLOR_2, 15: LAYER_3_COLOR_2
    },
    'keycodes': [
        None, Keycode.A, Keycode.Q, Keycode.B,
        Keycode.W, Keycode.C, Keycode.E, Keycode.D,
        Keycode.R, Keycode.E, Keycode.T, Keycode.F,
        Keycode.Y, Keycode.G, Keycode.U, Keycode.H
    ]
}

# None
LAYER_4_COLOR_1 = (60, 55, 110)
LAYER_4_COLOR_2 = (155, 70, 20)

LAYER_4 = {
    'name': 'LAYER_4',
    'color_map': {
        0: LAYER_4_COLOR_1, 1: LAYER_4_COLOR_2, 2: LAYER_4_COLOR_1, 3: LAYER_4_COLOR_2,
        4: LAYER_4_COLOR_2, 5: LAYER_4_COLOR_1, 6: LAYER_4_COLOR_2, 7: LAYER_4_COLOR_1,
        8: LAYER_4_COLOR_1, 9: LAYER_4_COLOR_2, 10: LAYER_4_COLOR_1, 11: LAYER_4_COLOR_2,
        12: LAYER_4_COLOR_2, 13: LAYER_4_COLOR_1, 14: LAYER_4_COLOR_2, 15: LAYER_4_COLOR_1
    },
    'keycodes': [
        None, Keycode.E, ConsumerControlCode.VOLUME_INCREMENT, ConsumerControlCode.STOP,
        Keycode.E, Keycode.F, Keycode.G, ConsumerControlCode.MUTE,
        Keycode.I, Keycode.J, Keycode.K, (Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.C), # open chrome
        Keycode.M, Keycode.N, Keycode.O, (Keycode.WINDOWS, Keycode.E) # open explorer
    ]
}

# None
LAYER_5_COLOR_1 = (120, 155, 0)
LAYER_5_COLOR_2 = (5, 255, 220)

LAYER_5 = {
    'name': 'LAYER_5',
    'color_map': {
        0: LAYER_5_COLOR_1, 1: LAYER_5_COLOR_1, 2: LAYER_5_COLOR_1, 3: LAYER_5_COLOR_1,
        4: LAYER_5_COLOR_2, 5: LAYER_5_COLOR_2, 6: LAYER_5_COLOR_2, 7: LAYER_5_COLOR_2,
        8: LAYER_5_COLOR_1, 9: LAYER_5_COLOR_1, 10: LAYER_5_COLOR_1, 11: LAYER_5_COLOR_1,
        12: LAYER_5_COLOR_2, 13: LAYER_5_COLOR_2, 14: LAYER_5_COLOR_2, 15: LAYER_5_COLOR_2
    },
    'keycodes': [
        None, Keycode.A, Keycode.Q, Keycode.B,
        Keycode.W, Keycode.C, Keycode.E, Keycode.D,
        Keycode.R, Keycode.E, Keycode.T, Keycode.F,
        Keycode.Y, Keycode.G, Keycode.U, Keycode.H
    ]
}

# None
LAYER_6_COLOR_1 = (120, 155, 0)
LAYER_6_COLOR_2 = (5, 255, 220)

LAYER_6 = {
    'name': 'LAYER_6',
    'color_map': {
        0: LAYER_6_COLOR_1, 1: LAYER_6_COLOR_1, 2: LAYER_6_COLOR_1, 3: LAYER_6_COLOR_1,
        4: LAYER_6_COLOR_2, 5: LAYER_6_COLOR_2, 6: LAYER_6_COLOR_2, 7: LAYER_6_COLOR_2,
        8: LAYER_6_COLOR_1, 9: LAYER_6_COLOR_1, 10: LAYER_6_COLOR_1, 11: LAYER_6_COLOR_1,
        12: LAYER_6_COLOR_2, 13: LAYER_6_COLOR_2, 14: LAYER_6_COLOR_2, 15: LAYER_6_COLOR_2
    },
    'keycodes': [
        None, Keycode.A, Keycode.Q, Keycode.B,
        Keycode.W, Keycode.C, Keycode.E, Keycode.D,
        Keycode.R, Keycode.E, Keycode.T, Keycode.F,
        Keycode.Y, Keycode.G, Keycode.U, Keycode.H
    ]
}

# None
LAYER_7_COLOR_1 = (120, 155, 0)
LAYER_7_COLOR_2 = (5, 255, 220)

LAYER_7 = {
    'name': 'LAYER_7',
    'color_map': {
        0: LAYER_7_COLOR_1, 1: LAYER_7_COLOR_1, 2: LAYER_7_COLOR_1, 3: LAYER_7_COLOR_1,
        4: LAYER_7_COLOR_2, 5: LAYER_7_COLOR_2, 6: LAYER_7_COLOR_2, 7: LAYER_7_COLOR_2,
        8: LAYER_7_COLOR_1, 9: LAYER_7_COLOR_1, 10: LAYER_7_COLOR_1, 11: LAYER_7_COLOR_1,
        12: LAYER_7_COLOR_2, 13: LAYER_7_COLOR_2, 14: LAYER_7_COLOR_2, 15: LAYER_7_COLOR_2
    },
    'keycodes': [
        None, Keycode.A, Keycode.Q, Keycode.B,
        Keycode.W, Keycode.C, Keycode.E, Keycode.D,
        Keycode.R, Keycode.E, Keycode.T, Keycode.F,
        Keycode.Y, Keycode.G, Keycode.U, Keycode.H
    ]
}

# None
LAYER_8_COLOR_1 = (120, 155, 0)
LAYER_8_COLOR_2 = (5, 255, 220)

LAYER_8 = {
    'name': 'LAYER_8',
    'color_map': {
        0: LAYER_8_COLOR_1, 1: LAYER_8_COLOR_1, 2: LAYER_8_COLOR_1, 3: LAYER_8_COLOR_1,
        4: LAYER_8_COLOR_2, 5: LAYER_8_COLOR_2, 6: LAYER_8_COLOR_2, 7: LAYER_8_COLOR_2,
        8: LAYER_8_COLOR_1, 9: LAYER_8_COLOR_1, 10: LAYER_8_COLOR_1, 11: LAYER_8_COLOR_1,
        12: LAYER_8_COLOR_2, 13: LAYER_8_COLOR_2, 14: LAYER_8_COLOR_2, 15: LAYER_8_COLOR_2
    },
    'keycodes': [
        None, Keycode.A, Keycode.Q, Keycode.B,
        Keycode.W, Keycode.C, Keycode.E, Keycode.D,
        Keycode.R, Keycode.E, Keycode.T, Keycode.F,
        Keycode.Y, Keycode.G, Keycode.U, Keycode.H
    ]
}

LAYER_100 = {
    'name': 'LAYER_100',
    'color_map': {
        3: LAYER_1_COLOR_ORANGE,
        7: LAYER_2_COLOR_PURPLE,
        11: LAYER_3_COLOR_2,
        15: LAYER_4_COLOR_2,
        2: LAYER_5_COLOR_2,
        6: LAYER_6_COLOR_2,
        10: LAYER_7_COLOR_2,
        14: LAYER_8_COLOR_2
    },
    'keycodes': None
}
