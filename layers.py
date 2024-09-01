from adafruit_hid.keycode import Keycode
# レイヤーの色設定

# Blender
LAYER_1_COLOR_ORANGE = (255, 128, 0)  # オレンジ色
LAYER_1_COLOR_BLUE = (0, 109, 143)  # 青色

LAYER_1 = {
    'name': 'LAYER_1',
    'color_map': {
        1: LAYER_1_COLOR_ORANGE, 3: LAYER_1_COLOR_ORANGE, 4: LAYER_1_COLOR_ORANGE,
        5: LAYER_1_COLOR_ORANGE, 6: LAYER_1_COLOR_ORANGE, 8: LAYER_1_COLOR_ORANGE,
        10: LAYER_1_COLOR_ORANGE, 11: LAYER_1_COLOR_ORANGE, 12: LAYER_1_COLOR_ORANGE,
        13: LAYER_1_COLOR_ORANGE, 14: LAYER_1_COLOR_ORANGE, 9: LAYER_1_COLOR_BLUE
    },
    'keycodes': [
        Keycode.ALT, Keycode.B, (Keycode.CONTROL, Keycode.C), (Keycode.CONTROL, Keycode.V),
        Keycode.E, Keycode.F, Keycode.G, Keycode.H,
        Keycode.I, Keycode.J, Keycode.K, Keycode.L,
        Keycode.M, Keycode.N, Keycode.O, Keycode.P
    ]
}

#MagicaVoxel
LAYER_2_COLOR_PURPLE = (53, 2, 87)  # 紫色
LAYER_2_COLOR_PURPLE2 = (255, 157, 0)  # 薄紫色
LAYER_2_COLOR_PURPLE3 = (255, 198, 194)  # 濃紫色

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
        Keycode.ALT, Keycode.TWO, Keycode.THREE, Keycode.FOUR,
        Keycode.FIVE, Keycode.SIX, Keycode.SEVEN, Keycode.EIGHT,
        Keycode.NINE, Keycode.ZERO, Keycode.MINUS, Keycode.EQUALS,
        Keycode.BACKSPACE, Keycode.TAB, Keycode.ENTER, Keycode.ESCAPE
    ]
}

# None
LAYER_3_COLOR_GREEN = (120, 155, 0)
LAYER_3_COLOR_YELLOW = (5, 255, 220)

LAYER_3 = {
    'name': 'LAYER_3',
    'color_map': {
        0: LAYER_3_COLOR_GREEN, 1: LAYER_3_COLOR_GREEN, 2: LAYER_3_COLOR_GREEN, 3: LAYER_3_COLOR_GREEN,
        4: LAYER_3_COLOR_YELLOW, 5: LAYER_3_COLOR_YELLOW, 6: LAYER_3_COLOR_YELLOW, 7: LAYER_3_COLOR_YELLOW,
        8: LAYER_3_COLOR_GREEN, 9: LAYER_3_COLOR_GREEN, 10: LAYER_3_COLOR_GREEN, 11: LAYER_3_COLOR_GREEN,
        12: LAYER_3_COLOR_YELLOW, 13: LAYER_3_COLOR_YELLOW, 14: LAYER_3_COLOR_YELLOW, 15: LAYER_3_COLOR_YELLOW
    },
    'keycodes': [
        Keycode.ALT, Keycode.A, Keycode.SHIFT, Keycode.B,
        Keycode.SHIFT, Keycode.C, Keycode.SHIFT, Keycode.D,
        Keycode.SHIFT, Keycode.E, Keycode.SHIFT, Keycode.F,
        Keycode.SHIFT, Keycode.G, Keycode.SHIFT, Keycode.H
    ]
}

# None
LAYER_4_COLOR_GREEN = (0, 255, 0)  # 緑色
LAYER_4_COLOR_YELLOW = (255, 255, 0)  # 黄色

LAYER_4 = {
    'name': 'LAYER_4',
    'color_map': {
        0: LAYER_4_COLOR_GREEN, 1: LAYER_4_COLOR_GREEN, 2: LAYER_4_COLOR_GREEN, 3: LAYER_4_COLOR_GREEN,
        4: LAYER_4_COLOR_YELLOW, 5: LAYER_4_COLOR_YELLOW, 6: LAYER_4_COLOR_YELLOW, 7: LAYER_4_COLOR_YELLOW,
        8: LAYER_4_COLOR_GREEN, 9: LAYER_4_COLOR_GREEN, 10: LAYER_4_COLOR_GREEN, 11: LAYER_4_COLOR_GREEN,
        12: LAYER_4_COLOR_YELLOW, 13: LAYER_4_COLOR_YELLOW, 14: LAYER_4_COLOR_YELLOW, 15: LAYER_4_COLOR_YELLOW
    },
    'keycodes': [
        Keycode.I, Keycode.J, Keycode.K, Keycode.L,
        Keycode.E, Keycode.F, Keycode.G, Keycode.H,
        Keycode.I, Keycode.J, Keycode.K, Keycode.L,
        Keycode.M, Keycode.N, Keycode.O, Keycode.P
    ]
}

LAYER_100 = {
    'name': 'LAYER_100',
    'color_map': {
        3: (0, 0, 255),  # 青色
        7: (0, 0, 255),  # 青色
        11: (0, 0, 255),  # 青色
        15: (0, 0, 255)  # 青色
    },
    'keycodes': None  # キーコードなし
}
