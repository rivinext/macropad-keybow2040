from adafruit_hid.keycode import Keycode

# レイヤーの色設定
LAYER_1_COLOR_ORANGE = (255, 128, 0)  # オレンジ色
LAYER_1_COLOR_BLUE = (0, 109, 143)  # 青色

LAYER_2_COLOR_PURPLE = (53, 2, 87)  # 紫色
LAYER_2_COLOR_PURPLE2 = (255, 233, 196)  # 薄紫色
LAYER_2_COLOR_PURPLE3 = (255, 119, 0)  # 濃紫色

# レイヤーの設定
LAYER_1 = {
    'name': 'LAYER_1',
    'color_map': {
        1: LAYER_1_COLOR_ORANGE, 3: LAYER_1_COLOR_ORANGE, 4: LAYER_1_COLOR_ORANGE,
        5: LAYER_1_COLOR_ORANGE, 6: LAYER_1_COLOR_ORANGE, 8: LAYER_1_COLOR_ORANGE,
        10: LAYER_1_COLOR_ORANGE, 11: LAYER_1_COLOR_ORANGE, 12: LAYER_1_COLOR_ORANGE,
        13: LAYER_1_COLOR_ORANGE, 14: LAYER_1_COLOR_ORANGE, 9: LAYER_1_COLOR_BLUE
    },
    'keycodes': [
        Keycode.A, Keycode.B, Keycode.C, Keycode.D,
        Keycode.E, Keycode.F, Keycode.G, Keycode.H,
        Keycode.I, Keycode.J, Keycode.K, Keycode.L,
        Keycode.M, Keycode.N, Keycode.O, Keycode.P
    ]
}

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
        Keycode.ONE, Keycode.TWO, Keycode.THREE, Keycode.FOUR,
        Keycode.FIVE, Keycode.SIX, Keycode.SEVEN, Keycode.EIGHT,
        Keycode.NINE, Keycode.ZERO, Keycode.MINUS, Keycode.EQUALS,
        Keycode.BACKSPACE, Keycode.TAB, Keycode.ENTER, Keycode.ESCAPE
    ]
}

LAYER_3 = {
    'name': 'LAYER_3',
    'color': (255, 0, 255),  # ピンク色
    'keycodes': [
        Keycode.SHIFT, Keycode.A, Keycode.SHIFT, Keycode.B,
        Keycode.SHIFT, Keycode.C, Keycode.SHIFT, Keycode.D,
        Keycode.SHIFT, Keycode.E, Keycode.SHIFT, Keycode.F,
        Keycode.SHIFT, Keycode.G, Keycode.SHIFT, Keycode.H
    ]
}

LAYER_100 = {
    'name': 'LAYER_100',
    'color': (0, 0, 255),  # 青色
    'keycodes': None,  # キーコードなし
    'active_indexes': [3, 7, 11]  # 移動可能なレイヤーキーのみ光らせる
}
