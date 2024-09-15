from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode

# レイヤーの色設定
L00C1 = (0, 0, 0) #LAYER_0_COLOR_1

# Blender
L01C1 = (255, 128, 0)
L01C2 = (0, 109, 143)

LAYER_1 = {
    'name': 'LAYER_1',
    'color_map': {
        3: L01C1, 7: L00C1, 11: L01C1, 15: L00C1,
        2: L00C1, 6: L01C1, 10: L01C1, 14: L01C1,
        1: L01C1, 5: L01C1, 9: L01C2, 13: L01C1,
        0: L00C1, 4: L01C1, 8: L01C1, 12: L01C1
    },
    'keycodes': {
        3: (Keycode.CONTROL, Keycode.V), 7: Keycode.H, 11: Keycode.L, 15: Keycode.P,
        2: (Keycode.CONTROL, Keycode.C), 6: Keycode.G, 10: Keycode.K, 14: Keycode.O,
        1: Keycode.B, 5: Keycode.F, 9: Keycode.KEYPAD_SEVEN, 13: Keycode.KEYPAD_PERIOD,
        0: None, 4: (Keycode.CONTROL, Keycode.KEYPAD_THREE), 8: Keycode.KEYPAD_ONE, 12: Keycode.KEYPAD_THREE
    }
}

# MagicaVoxel
L02C1 = (53, 2, 87)
L02C2 = (235, 120, 40)
L02C3 = (255, 198, 194)

LAYER_2 = {
    'name': 'LAYER_2',
    'color_map': {
        3: L02C1, 7: L02C1, 11: L02C1, 15: L02C1,
        2: L02C1, 6: L02C1, 10: L02C1, 14: L02C1,
        1: L02C1, 5: L02C3, 9: L02C3, 13: L02C1,
        0: L02C1, 4: L02C2, 8: L02C2, 12: L02C1
    },
    'keycodes': {
        0: None,
        1: Keycode.N,
        2: Keycode.N,
        3: Keycode.N,
        4: Keycode.LEFT_ARROW,
        5: Keycode.PAGE_DOWN,
        6: Keycode.THREE,
        7: Keycode.MINUS,
        8: Keycode.DOWN_ARROW,
        9: Keycode.UP_ARROW,
        10: Keycode.F2,
        11: Keycode.F2,
        12: Keycode.RIGHT_ARROW,
        13: Keycode.PAGE_UP,
        14: Keycode.EIGHT,
        15: Keycode.EQUALS
    }
}

# LAYER_3
L03C1 = (120, 155, 0)
L03C2 = (5, 255, 220)

LAYER_3 = {
    'name': 'LAYER_3',
    'color_map': {
        3: L03C1, 7: L03C2, 11: L03C1, 15: L03C2,
        2: L03C1, 6: L03C2, 10: L03C1, 14: L03C2,
        1: L03C1, 5: L03C2, 9: L03C1, 13: L03C2,
        0: L03C1, 4: L03C2, 8: L03C1, 12: L03C2
    },
    'keycodes': {
        3: Keycode.B, 7: Keycode.D, 11: Keycode.F, 15: Keycode.H,
        2: Keycode.Q, 6: Keycode.E, 10: Keycode.T, 14: Keycode.U,
        1: Keycode.A, 5: Keycode.C, 9: Keycode.E, 13: Keycode.G,
        0: None, 4: Keycode.W, 8: Keycode.R, 12: Keycode.Y
    }
}

# LAYER_4
L04C1 = (60, 55, 110)
L04C2 = (155, 70, 20)

LAYER_4 = {
    'name': 'LAYER_4',
    'color_map': {
        3: L04C2, 7: L04C1, 11: L04C2, 15: L04C1,
        2: L04C1, 6: L04C2, 10: L04C1, 14: L04C2,
        1: L04C2, 5: L04C1, 9: L04C2, 13: L04C1,
        0: L04C1, 4: L04C2, 8: L04C1, 12: L04C2
    },
    'keycodes': {
        3: ConsumerControlCode.STOP, 7: ConsumerControlCode.MUTE, 11: (Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.C), 15: (Keycode.WINDOWS, Keycode.E),
        2: ConsumerControlCode.VOLUME_INCREMENT, 6: Keycode.G, 10: Keycode.K, 14: Keycode.O,
        1: Keycode.E, 5: Keycode.F, 9: Keycode.J, 13: Keycode.N,
        0: None, 4: Keycode.E, 8: Keycode.I, 12: Keycode.M
    }
}

# LAYER_5
L05C1 = (240, 230, 120)
L05C2 = (138, 13, 226)

LAYER_5 = {
    'name': 'LAYER_5',
    'color_map': {
        3: L05C1, 7: L05C2, 11: L05C1, 15: L05C2,
        2: L05C2, 6: L05C1, 10: L05C2, 14: L05C1,
        1: L05C1, 5: L05C2, 9: L05C1, 13: L05C2,
        0: L05C2, 4: L05C1, 8: L05C2, 12: L05C1
    },
    'keycodes': {
        3: Keycode.B, 7: Keycode.D, 11: Keycode.F, 15: Keycode.H,
        2: Keycode.Q, 6: Keycode.E, 10: Keycode.T, 14: Keycode.U,
        1: Keycode.A, 5: Keycode.C, 9: Keycode.E, 13: Keycode.G,
        0: None, 4: Keycode.W, 8: Keycode.R, 12: Keycode.Y
    }
}

# LAYER_6
L06C1 = (120, 215, 10)
L06C2 = (115, 65, 40)

LAYER_6 = {
    'name': 'LAYER_6',
    'color_map': {
        3: L06C1, 7: L06C2, 11: L06C1, 15: L06C2,
        2: L06C1, 6: L06C2, 10: L06C1, 14: L06C2,
        1: L06C1, 5: L06C2, 9: L06C1, 13: L06C2,
        0: L06C1, 4: L06C2, 8: L06C1, 12: L06C2
    },
    'keycodes': {
        3: Keycode.B, 7: Keycode.D, 11: Keycode.F, 15: Keycode.H,
        2: Keycode.Q, 6: Keycode.E, 10: Keycode.T, 14: Keycode.U,
        1: Keycode.A, 5: Keycode.C, 9: Keycode.E, 13: Keycode.G,
        0: None, 4: Keycode.W, 8: Keycode.R, 12: Keycode.Y
    }
}

# LAYER_7
L07C1 = (60, 155, 90)
L07C2 = (225, 55, 20)

LAYER_7 = {
    'name': 'LAYER_7',
    'color_map': {
        3: L07C1, 7: L07C2, 11: L07C1, 15: L07C2,
        2: L07C2, 6: L07C1, 10: L07C2, 14: L07C1,
        1: L07C1, 5: L07C2, 9: L07C1, 13: L07C2,
        0: L07C2, 4: L07C1, 8: L07C2, 12: L07C1
    },
    'keycodes': {
        3: Keycode.B, 7: Keycode.D, 11: Keycode.F, 15: Keycode.H,
        2: Keycode.Q, 6: Keycode.E, 10: Keycode.T, 14: Keycode.U,
        1: Keycode.A, 5: Keycode.C, 9: Keycode.E, 13: Keycode.G,
        0: None, 4: Keycode.W, 8: Keycode.R, 12: Keycode.Y
    }
}

# LAYER_8
L08C1 = (20, 155, 110)
L08C2 = (25, 55, 20)

LAYER_8 = {
    'name': 'LAYER_8',
    'color_map': {
        3: L08C1, 7: L08C2, 11: L08C1, 15: L08C2,
        2: L08C1, 6: L08C2, 10: L08C1, 14: L08C2,
        1: L08C1, 5: L08C2, 9: L08C1, 13: L08C2,
        0: L08C1, 4: L08C2, 8: L08C1, 12: L08C2
    },
    'keycodes': {
        3: Keycode.B, 7: Keycode.D, 11: Keycode.F, 15: Keycode.H,
        2: Keycode.Q, 6: Keycode.E, 10: Keycode.T, 14: Keycode.U,
        1: Keycode.A, 5: Keycode.C, 9: Keycode.E, 13: Keycode.G,
        0: None, 4: Keycode.W, 8: Keycode.R, 12: Keycode.Y
    }
}

# LAYER_9
L09C1 = (255, 99, 71)
L09C2 = (30, 144, 255)

LAYER_9 = {
    'name': 'LAYER_9',
    'color_map': {
        3: L09C1, 7: L09C2, 11: L09C1, 15: L09C2,
        2: L09C1, 6: L09C2, 10: L09C1, 14: L09C2,
        1: L09C1, 5: L09C2, 9: L09C1, 13: L09C2,
        0: L09C1, 4: L09C2, 8: L09C1, 12: L09C2
    },
    'keycodes': {
        3: Keycode.B, 7: Keycode.D, 11: Keycode.F, 15: Keycode.H,
        2: Keycode.Q, 6: Keycode.E, 10: Keycode.T, 14: Keycode.U,
        1: Keycode.A, 5: Keycode.C, 9: Keycode.E, 13: Keycode.G,
        0: None, 4: Keycode.W, 8: Keycode.R, 12: Keycode.Y
    }
}

# LAYER_10
L10C1 = (218, 112, 214)
L10C2 = (50, 205, 50)

LAYER_10 = {
    'name': 'LAYER_10',
    'color_map': {
        3: L10C1, 7: L10C2, 11: L10C1, 15: L10C2,
        2: L10C2, 6: L10C1, 10: L10C2, 14: L10C1,
        1: L10C1, 5: L10C2, 9: L10C1, 13: L10C2,
        0: L10C2, 4: L10C1, 8: L10C2, 12: L10C1
    },
    'keycodes': {
        3: Keycode.B, 7: Keycode.D, 11: Keycode.F, 15: Keycode.H,
        2: Keycode.Q, 6: Keycode.E, 10: Keycode.T, 14: Keycode.U,
        1: Keycode.A, 5: Keycode.C, 9: Keycode.E, 13: Keycode.G,
        0: None, 4: Keycode.W, 8: Keycode.R, 12: Keycode.Y
    }
}

# LAYER_11
L11C1 = (155, 105, 180)
L11C2 = (15, 110, 130)

LAYER_11 = {
    'name': 'LAYER_11',
    'color_map': {
        3: L11C2, 7: L11C1, 11: L11C2, 15: L11C1,
        2: L11C2, 6: L11C1, 10: L11C2, 14: L11C1,
        1: L11C1, 5: L11C2, 9: L11C1, 13: L11C2,
        0: L11C1, 4: L11C2, 8: L11C1, 12: L11C2
    },
    'keycodes': {
        3: Keycode.B, 7: Keycode.D, 11: Keycode.F, 15: Keycode.H,
        2: Keycode.Q, 6: Keycode.E, 10: Keycode.T, 14: Keycode.U,
        1: Keycode.A, 5: Keycode.C, 9: Keycode.E, 13: Keycode.G,
        0: None, 4: Keycode.W, 8: Keycode.R, 12: Keycode.Y
    }
}

# LAYER_12
L12C1 = (120, 55, 225)
L12C2 = (45, 125, 40)

LAYER_12 = {
    'name': 'LAYER_12',
    'color_map': {
        3: L12C1, 7: L12C2, 11: L12C2, 15: L12C1,
        2: L12C2, 6: L12C1, 10: L12C1, 14: L12C2,
        1: L12C2, 5: L12C1, 9: L12C1, 13: L12C2,
        0: L12C1, 4: L12C2, 8: L12C2, 12: L12C1
    },
    'keycodes': {
        3: Keycode.B, 7: Keycode.D, 11: Keycode.F, 15: Keycode.H,
        2: Keycode.Q, 6: Keycode.E, 10: Keycode.T, 14: Keycode.U,
        1: Keycode.A, 5: Keycode.C, 9: Keycode.E, 13: Keycode.G,
        0: None, 4: Keycode.W, 8: Keycode.R, 12: Keycode.Y
    }
}

# LAYER_13
L13C1 = (70, 130, 180)
L13C2 = (255, 228, 225)

LAYER_13 = {
    'name': 'LAYER_13',
    'color_map': {
        3: L13C2, 7: L13C1, 11: L13C2, 15: L13C1,
        2: L13C2, 6: L13C1, 10: L13C2, 14: L13C1,
        1: L13C1, 5: L13C2, 9: L13C1, 13: L13C2,
        0: L13C1, 4: L13C2, 8: L13C1, 12: L13C2
    },
    'keycodes': {
        3: Keycode.B, 7: Keycode.D, 11: Keycode.F, 15: Keycode.H,
        2: Keycode.Q, 6: Keycode.E, 10: Keycode.T, 14: Keycode.U,
        1: Keycode.A, 5: Keycode.C, 9: Keycode.E, 13: Keycode.G,
        0: None, 4: Keycode.W, 8: Keycode.R, 12: Keycode.Y
    }
}

# LAYER_14
L14C1 = (0, 0, 0)
L14C2 = (0, 0, 0)

LAYER_14 = {
    'name': 'LAYER_14',
    'color_map': {
        3: L14C1, 7: L14C2, 11: L14C1, 15: L14C2,
        2: L14C2, 6: L14C1, 10: L14C2, 14: L14C1,
        1: L14C1, 5: L14C2, 9: L14C1, 13: L14C2,
        0: L14C2, 4: L14C1, 8: L14C2, 12: L14C1
    },
    'keycodes': {
        3: Keycode.B, 7: Keycode.D, 11: Keycode.F, 15: Keycode.H,
        2: Keycode.Q, 6: Keycode.E, 10: Keycode.T, 14: Keycode.U,
        1: Keycode.A, 5: Keycode.C, 9: Keycode.E, 13: Keycode.G,
        0: None, 4: Keycode.W, 8: Keycode.R, 12: Keycode.Y
    }
}

# LAYER_15
L15C1 = (0, 0, 0)
L15C2 = (186, 85, 211)
L15C3 = (0, 255, 127)

LAYER_15 = {
    'name': 'LAYER_15',
    'color_map': {
        3: L01C1, 7: L02C1, 11: L03C2, 15: L15C1,
        2: L05C2, 6: L06C2, 10: L07C2, 14: L15C1,
        1: L15C1, 5: L15C1, 9: L15C1, 13: L15C3,
        0: L15C1, 4: L15C1, 8: L15C1, 12: L15C1
    },
    'keycodes': {
        3: "RIVI", 7: "CUSTOM1", 11: None, 15: None,
        2: "HELLO", 6: "CHROME1", 10: "CHROME2", 14: None,
        1: None, 5: None, 9: None, 13: (Keycode.WINDOWS, Keycode.E),
        0: None, 4: None, 8: None, 12: None
    }
}

# LAYER_100
LAYER_100 = {
    'name': 'LAYER_100',
    'color_map': {
        3: L01C1, 7: L02C1, 11: L03C2, 15: L04C2,
        2: L05C2, 6: L06C2, 10: L07C2, 14: L08C2,
        1: L09C1, 5: L10C1, 9: L11C1, 13: L12C1,
        0: L00C1, 4: L13C1, 8: L14C1, 12: L15C3
    },
    'keycodes': {}
}
