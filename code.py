import board
from keybow2040 import Keybow2040
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# キーボードとレイアウトのセットアップ
i2c = board.I2C()
keybow = Keybow2040(i2c)
keys = keybow.keys

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# レイヤーの定義
LAYER_1 = [
    Keycode.ZERO, Keycode.K, Keycode.J, Keycode.I,
    "CTRL_X", Keycode.G, Keycode.F, Keycode.A,
    "CTRL_C", Keycode.C, Keycode.B, Keycode.N,
    "CTRL_V", Keycode.A, Keycode.A, Keycode.F
]

LAYER_2 = [ # Blener
    Keycode.ZERO, Keycode.ONE, Keycode.FOUR, Keycode.SEVEN,
    "CTRL_KP3", Keycode.TWO, Keycode.FIVE, Keycode.EIGHT,
    Keycode.KEYPAD_ONE, Keycode.KEYPAD_SEVEN, Keycode.SIX, Keycode.NINE,
    Keycode.KEYPAD_THREE, Keycode.ZERO, Keycode.ZERO, "SHIFT_A"
]

LAYER_3 = [ # MagicaVoxel 最初のKeycode.ZEROはただのレイヤー切り替えキー
    Keycode.ZERO, Keycode.ONE, Keycode.FOUR, Keycode.SEVEN,
    Keycode.ZERO, Keycode.TWO, Keycode.FIVE, Keycode.EIGHT,
    Keycode.ZERO, Keycode.THREE, Keycode.SIX, Keycode.NINE,
    Keycode.ZERO, Keycode.ZERO, Keycode.ZERO, Keycode.B
]

LAYER_4 = [ #
    Keycode.ZERO, Keycode.ZERO, Keycode.ZERO, Keycode.ZERO,
    Keycode.ZERO, Keycode.ZERO, Keycode.ZERO, Keycode.ZERO,
    Keycode.ZERO, Keycode.ZERO, Keycode.ZERO, Keycode.E,
    Keycode.ZERO, Keycode.ZERO, Keycode.ZERO, Keycode.E
]

LAYER_5 = [ #
    Keycode.ZERO, Keycode.ZERO, Keycode.ZERO, Keycode.ZERO,
    Keycode.ZERO, Keycode.ZERO, Keycode.ZERO, Keycode.ZERO,
    Keycode.ZERO, Keycode.ZERO, Keycode.ZERO, Keycode.Z,
    Keycode.ZERO, Keycode.ZERO, Keycode.ZERO, Keycode.Q
]

# レイヤーとLEDの色を関連付け   ここはとりあえず追加しとけばよい
LAYERS = [LAYER_1, LAYER_2, LAYER_3, LAYER_4, LAYER_5]
LED_COLORS = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]

# レイヤーごとの特定キーのLED設定　LEDでそれぞれのアイコンを作ってみた
SPECIAL_LED_SETTINGS = {
    0: [(3, (255, 60, 0))],  # レイヤー1
    1: [(1, (255, 128, 0)), (3, (255, 128, 0)), (4, (255, 128, 0)), (5, (255, 128, 0)), (6, (255, 128, 0)), (8, (255, 128, 0)),
        (10, (255, 128, 0)), (11, (255, 128, 0)), (12, (255, 128, 0)), (13, (255, 128, 0)), (14, (255, 128, 0)), (9, (0, 109, 143))],
    2: [(0, (53, 2, 87)),(1, (53, 2, 87)),(2, (53, 2, 87)),(3, (53, 2, 87)),(6, (53, 2, 87)),(0, (53, 2, 87)),(10, (53, 2, 87)),
        (12, (53, 2, 87)),(13, (53, 2, 87)),(14, (53, 2, 87)),(15, (53, 2, 87)),
        (5, (247, 213, 158)),(9, (247, 213, 158)),(4, (255, 128, 0)),(8, (255, 128, 0))],
    3: [(15, (140, 0, 55))],
    4: [(2, (140, 220, 0))]
}

# 現在のレイヤー
current_layer = 0

# Fnキーの定義（インデックス0のキーをFnキーに設定）
FN_KEY_INDEX = 3

# 押下時のLEDの色（黄色）
PRESS_LED_COLOR = (255, 255, 0)

def update_special_led():
    """特定のレイヤーに応じて特定のキーのLEDを常に点灯させる"""
    led_settings = SPECIAL_LED_SETTINGS.get(current_layer, [])
    for i, key in enumerate(keys):
        key.led_off()  # 全てのキーを一度消灯
        for index, color in led_settings:
            if i == index:
                key.set_led(*color)  # 指定された色で点灯12

# ハンドラの設定
for key in keys:
    @keybow.on_press(key)
    def press_handler(key):
        global current_layer
        if key.number == FN_KEY_INDEX:
            # レイヤーの切り替え
            current_layer = (current_layer + 1) % len(LAYERS)
            update_special_led()
        else:
            keycode = LAYERS[current_layer][key.number]
            if keycode == "CTRL_X":  # カスタム識別子でCtrl+Xを送信
                print("Ctrl+X is being sent")  # デバッグメッセージ
                keyboard.press(Keycode.CONTROL, Keycode.X)
                keyboard.release_all()  # すべてのキーをリリース
            elif keycode == "CTRL_C":
                print("Ctrl+C is being sent")  # デバッグメッセージ
                keyboard.press(Keycode.CONTROL, Keycode.C)
                keyboard.release_all()  # すべてのキーをリリース
            elif keycode == "CTRL_V":
                print("Ctrl+V is being sent")  # デバッグメッセージ
                keyboard.press(Keycode.CONTROL, Keycode.V)
                keyboard.release_all()  # すべてのキーをリリース
            elif keycode == "CTRL_KP3":  # カスタム識別子でCtrl+KP3を送信
                print("Ctrl+Keypad 3 is being sent")  # デバッグメッセージ
                keyboard.press(Keycode.CONTROL, Keycode.KEYPAD_THREE)
                keyboard.release_all()
            elif keycode == "SHIFT_A":  # カスタム識別子でShift+Aを送信
                print("SHIFT_A is being sent")  # デバッグメッセージ
                keyboard.press(Keycode.SHIFT, Keycode.A)
                keyboard.release_all()
            else:
                key.set_led(*PRESS_LED_COLOR)  # 押下したキーを黄色に点灯
                if isinstance(keycode, int):  # キーコードが整数である場合のみ送信
                    keyboard.send(keycode)
                    print(f"Key {key.number} sent: {keycode}")  # デバッグメッセージ

    @keybow.on_release(key)
    def release_handler(key):
        key.led_off()
        update_special_led()

# 初期設定でLEDを点灯
update_special_led()

# メインループ
while True:
    keybow.update()
