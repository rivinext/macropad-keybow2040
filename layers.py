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
LAYER_2_COLOR_PURPLE2 = (235, 120, 40)
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
        None, Keycode.N, Keycode.N, Keycode.N,
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
LAYER_5_COLOR_1 = (240,230,140)
LAYER_5_COLOR_2 = (138,43,226)

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
LAYER_6_COLOR_1 = (120, 215, 10)
LAYER_6_COLOR_2 = (115, 65, 40)

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
LAYER_7_COLOR_1 = (60, 155, 90)
LAYER_7_COLOR_2 = (225, 55, 20)

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
LAYER_8_COLOR_1 = (20, 155, 110)
LAYER_8_COLOR_2 = (25, 55, 20)

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

# None
LAYER_9_COLOR_1 = (255,99,71)
LAYER_9_COLOR_2 = (30,144,255)

LAYER_9 = {
    'name': 'LAYER_9',
    'color_map': {
        0: LAYER_9_COLOR_1, 1: LAYER_9_COLOR_1, 2: LAYER_9_COLOR_1, 3: LAYER_9_COLOR_1,
        4: LAYER_9_COLOR_2, 5: LAYER_9_COLOR_2, 6: LAYER_9_COLOR_2, 7: LAYER_9_COLOR_2,
        8: LAYER_9_COLOR_1, 9: LAYER_9_COLOR_1, 10: LAYER_9_COLOR_1, 11: LAYER_9_COLOR_1,
        12: LAYER_9_COLOR_2, 13: LAYER_9_COLOR_2, 14: LAYER_9_COLOR_2, 15: LAYER_9_COLOR_2
    },
    'keycodes': [
        None, Keycode.A, Keycode.Q, Keycode.B,
        Keycode.W, Keycode.C, Keycode.E, Keycode.D,
        Keycode.R, Keycode.E, Keycode.T, Keycode.F,
        Keycode.Y, Keycode.G, Keycode.U, Keycode.H
    ]
}

# None
LAYER_10_COLOR_1 = (218,112,214)
LAYER_10_COLOR_2 = (50,205,50)

LAYER_10 = {
    'name': 'LAYER_10',
    'color_map': {
        0: LAYER_10_COLOR_1, 1: LAYER_10_COLOR_1, 2: LAYER_10_COLOR_1, 3: LAYER_10_COLOR_1,
        4: LAYER_10_COLOR_2, 5: LAYER_10_COLOR_2, 6: LAYER_10_COLOR_2, 7: LAYER_10_COLOR_2,
        8: LAYER_10_COLOR_1, 9: LAYER_10_COLOR_1, 10: LAYER_10_COLOR_1, 11: LAYER_10_COLOR_1,
        12: LAYER_10_COLOR_2, 13: LAYER_10_COLOR_2, 14: LAYER_10_COLOR_2, 15: LAYER_10_COLOR_2
    },
    'keycodes': [
        None, Keycode.A, Keycode.Q, Keycode.B,
        Keycode.W, Keycode.C, Keycode.E, Keycode.D,
        Keycode.R, Keycode.E, Keycode.T, Keycode.F,
        Keycode.Y, Keycode.G, Keycode.U, Keycode.H
    ]
}

# None
LAYER_11_COLOR_1 = (255,105,180)
LAYER_11_COLOR_2 = (75,0,130)

LAYER_11 = {
    'name': 'LAYER_11',
    'color_map': {
        0: LAYER_11_COLOR_1, 1: LAYER_11_COLOR_1, 2: LAYER_11_COLOR_1, 3: LAYER_11_COLOR_1,
        4: LAYER_11_COLOR_2, 5: LAYER_11_COLOR_2, 6: LAYER_11_COLOR_2, 7: LAYER_11_COLOR_2,
        8: LAYER_11_COLOR_1, 9: LAYER_11_COLOR_1, 10: LAYER_11_COLOR_1, 11: LAYER_11_COLOR_1,
        12: LAYER_11_COLOR_2, 13: LAYER_11_COLOR_2, 14: LAYER_11_COLOR_2, 15: LAYER_11_COLOR_2
    },
    'keycodes': [
        None, Keycode.A, Keycode.Q, Keycode.B,
        Keycode.W, Keycode.C, Keycode.E, Keycode.D,
        Keycode.R, Keycode.E, Keycode.T, Keycode.F,
        Keycode.Y, Keycode.G, Keycode.U, Keycode.H
    ]
}

# None
LAYER_12_COLOR_1 = (120, 55, 225)
LAYER_12_COLOR_2 = (45, 125, 40)

LAYER_12 = {
    'name': 'LAYER_12',
    'color_map': {
        0: LAYER_12_COLOR_1, 1: LAYER_12_COLOR_1, 2: LAYER_12_COLOR_1, 3: LAYER_12_COLOR_1,
        4: LAYER_12_COLOR_2, 5: LAYER_12_COLOR_2, 6: LAYER_12_COLOR_2, 7: LAYER_12_COLOR_2,
        8: LAYER_12_COLOR_1, 9: LAYER_12_COLOR_1, 10: LAYER_12_COLOR_1, 11: LAYER_12_COLOR_1,
        12: LAYER_12_COLOR_2, 13: LAYER_12_COLOR_2, 14: LAYER_12_COLOR_2, 15: LAYER_12_COLOR_2
    },
    'keycodes': [
        None, Keycode.A, Keycode.Q, Keycode.B,
        Keycode.W, Keycode.C, Keycode.E, Keycode.D,
        Keycode.R, Keycode.E, Keycode.T, Keycode.F,
        Keycode.Y, Keycode.G, Keycode.U, Keycode.H
    ]
}

# None
LAYER_13_COLOR_1 = (70,130,180)
LAYER_13_COLOR_2 = (255,228,225)

LAYER_13 = {
    'name': 'LAYER_13',
    'color_map': {
        0: LAYER_13_COLOR_1, 1: LAYER_13_COLOR_1, 2: LAYER_13_COLOR_1, 3: LAYER_13_COLOR_1,
        4: LAYER_13_COLOR_2, 5: LAYER_13_COLOR_2, 6: LAYER_13_COLOR_2, 7: LAYER_13_COLOR_2,
        8: LAYER_13_COLOR_1, 9: LAYER_13_COLOR_1, 10: LAYER_13_COLOR_1, 11: LAYER_13_COLOR_1,
        12: LAYER_13_COLOR_2, 13: LAYER_13_COLOR_2, 14: LAYER_13_COLOR_2, 15: LAYER_13_COLOR_2
    },
    'keycodes': [
        None, Keycode.A, Keycode.Q, Keycode.B,
        Keycode.W, Keycode.C, Keycode.E, Keycode.D,
        Keycode.R, Keycode.E, Keycode.T, Keycode.F,
        Keycode.Y, Keycode.G, Keycode.U, Keycode.H
    ]
}

# None
LAYER_14_COLOR_1 = (0,0,0) #(20, 225, 170)
LAYER_14_COLOR_2 = (0,0,0) #(225, 145, 0)

LAYER_14 = {
    'name': 'LAYER_14',
    'color_map': {
        0: LAYER_14_COLOR_1, 1: LAYER_14_COLOR_1, 2: LAYER_14_COLOR_1, 3: LAYER_14_COLOR_1,
        4: LAYER_14_COLOR_2, 5: LAYER_14_COLOR_2, 6: LAYER_14_COLOR_2, 7: LAYER_14_COLOR_2,
        8: LAYER_14_COLOR_1, 9: LAYER_14_COLOR_1, 10: LAYER_14_COLOR_1, 11: LAYER_14_COLOR_1,
        12: LAYER_14_COLOR_2, 13: LAYER_14_COLOR_2, 14: LAYER_14_COLOR_2, 15: LAYER_14_COLOR_2
    },
    'keycodes': [
        None, Keycode.A, Keycode.Q, Keycode.B,
        Keycode.W, Keycode.C, Keycode.E, Keycode.D,
        Keycode.R, Keycode.E, Keycode.T, Keycode.F,
        Keycode.Y, Keycode.G, Keycode.U, Keycode.H
    ]
}

# None
LAYER_15_COLOR_1 = (0,0,0) #(186,85,211)
LAYER_15_COLOR_2 = (0,0,0) #(0,255,127)
LAYER_15_COLOR_3 = (0,255,127) #(0,255,127)

LAYER_15 = {
    'name': 'LAYER_15',
    'color_map': {
        0: LAYER_15_COLOR_1, 1: LAYER_15_COLOR_1, 2: LAYER_15_COLOR_3, 3: LAYER_15_COLOR_3,
        4: LAYER_15_COLOR_2, 5: LAYER_15_COLOR_2, 6: LAYER_15_COLOR_2, 7: LAYER_15_COLOR_3,
        8: LAYER_15_COLOR_1, 9: LAYER_15_COLOR_1, 10: LAYER_15_COLOR_1, 11: LAYER_15_COLOR_1,
        12: LAYER_15_COLOR_3, 13: LAYER_15_COLOR_2, 14: LAYER_15_COLOR_2, 15: LAYER_15_COLOR_2
    },
    'keycodes': [
        None, None, "HELLO", "RIVI",
        None, None, None, "CUSTOM1",
        None, None, None, None,
        (Keycode.WINDOWS, Keycode.E), None, None, None
    ]
}

LAYER_100 = {
    'name': 'LAYER_100',
    'color_map': {
        3: LAYER_1_COLOR_ORANGE, 7: LAYER_2_COLOR_PURPLE, 11: LAYER_3_COLOR_2, 15: LAYER_4_COLOR_2,
        2: LAYER_5_COLOR_2, 6: LAYER_6_COLOR_2, 10: LAYER_7_COLOR_2, 14: LAYER_8_COLOR_2,
        1: LAYER_9_COLOR_1, 5: LAYER_10_COLOR_1, 9: LAYER_11_COLOR_1, 13: LAYER_12_COLOR_1,
        0: (0,0,0), 4: LAYER_13_COLOR_1, 8: LAYER_14_COLOR_1, 12: LAYER_15_COLOR_3
    },
    'keycodes': None
}
