import board
from keybow2040 import Keybow2040
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS  # 追加
import time
from layers import (
    LAYER_1, LAYER_2, LAYER_3, LAYER_4, LAYER_5,
    LAYER_6, LAYER_7, LAYER_8, LAYER_9, LAYER_10,
    LAYER_11, LAYER_12, LAYER_13, LAYER_14, LAYER_15,
    LAYER_100
)

# Keybow 2040のセットアップ
i2c = board.I2C()
keybow = Keybow2040(i2c)
keys = keybow.keys

# キーボードのセットアップ
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # 追加

# Fnキーのインデックス
FN_KEY_INDEX = 0

# 現在のレイヤー（初期状態はLAYER_1）
current_layer = LAYER_1

# 各キーの押下状態とタイミングを追跡するリスト
key_state = [False] * 16  # 各キーの押下状態
last_keypress_time = [0] * 16  # 最後にキーが押された時間
initial_keypress_delay = 0.5  # 最初のキー押下後の遅延時間（秒）
repeat_interval = 0.03  # 長押し時の繰り返し間隔（秒）
initial_delay_done = [False] * 16  # 初回遅延が完了したかどうか

def set_layer_leds():
    """現在のレイヤーの色でキーのLEDを設定する"""
    color_map = current_layer.get('color_map', {})
    for i in range(16):
        if i in color_map:
            keys[i].set_led(*color_map[i])
        else:
            keys[i].set_led(0, 0, 0)  # 消灯

def handle_keypress(index):
    """キーの押下状態を処理し、必要に応じてアクションを実行する"""
    global current_layer

    current_time = time.monotonic()

    if keys[index].pressed:
        if not key_state[index]:
            key_state[index] = True
            last_keypress_time[index] = current_time
            initial_delay_done[index] = False
            process_key(index)
        else:
            if not initial_delay_done[index]:
                if current_time - last_keypress_time[index] >= initial_keypress_delay:
                    initial_delay_done[index] = True
                    last_keypress_time[index] = current_time
                    process_key(index)
            elif current_time - last_keypress_time[index] >= repeat_interval:
                last_keypress_time[index] = current_time
                process_key(index)
    else:
        key_state[index] = False
        initial_delay_done[index] = False

# カスタムキーコードの関数
def send_hello():
    """大文字で'HELLO'と入力する"""
    for char in "HELLO":
        keycode = getattr(Keycode, char)
        keyboard.press(Keycode.SHIFT, keycode)
        keyboard.release_all()
        time.sleep(0.05)
    time.sleep(0.3)  # n秒待機

def send_rivi():
    """Uキー、DOWN_ARROWキーを3回、その後ENTERキーを送信する"""
    keyboard.send(Keycode.U)
    time.sleep(0.05)
    for _ in range(3):
        keyboard.send(Keycode.DOWN_ARROW)
        time.sleep(0.15)
    keyboard.send(Keycode.ENTER)
    time.sleep(0.3)

def send_custom1():
    """Win+Xを押した後にTキーを送信する"""
    keyboard.press(Keycode.WINDOWS, Keycode.X)
    keyboard.release_all()
    time.sleep(0.05)
    keyboard.send(Keycode.T)
    time.sleep(0.3)

# カスタム関数の定義
def send_f23():
    """F23キーを送信する"""
    keyboard.send(Keycode.F23)
    time.sleep(0.1)

# カスタム関数の定義
def send_f24():
    """F24キーを送信する"""
    keyboard.send(Keycode.F24)
    time.sleep(0.1)

# カスタムキーコードと関数のマッピングに追加
custom_key_actions = {
    "HELLO": send_hello,
    "RIVI": send_rivi,
    "CUSTOM1": send_custom1,
    "CHROME1": send_f23,
    "CHROME2": send_f24
}

def process_key(index):
    """キーが押されたときのアクションを処理する"""
    global current_layer

    if index == FN_KEY_INDEX:
        # Fnキーが押された場合、LAYER_100に切り替える
        current_layer = LAYER_100
        set_layer_leds()
    elif current_layer['name'] == 'LAYER_100':
        # キーインデックスからレイヤー変数へのマッピングを定義
        key_to_layer = {
            3: LAYER_1,
            7: LAYER_2,
            11: LAYER_3,
            15: LAYER_4,
            2: LAYER_5,
            6: LAYER_6,
            10: LAYER_7,
            14: LAYER_8,
            1: LAYER_9,
            5: LAYER_10,
            9: LAYER_11,
            13: LAYER_12,
            4: LAYER_13,
            8: LAYER_14,
            12: LAYER_15
        }
        if index in key_to_layer:
            current_layer = key_to_layer[index]
            set_layer_leds()
            time.sleep(0.05)
    else:
        if index in current_layer['keycodes']:
            keycode = current_layer['keycodes'][index]
            if keycode in custom_key_actions:
                custom_key_actions[keycode]()
            elif isinstance(keycode, tuple):
                keyboard.press(*keycode)
                keyboard.release_all()
            elif isinstance(keycode, int):
                keyboard.send(keycode)


# メインループ
set_layer_leds()
while True:
    keybow.update()
    for i in range(16):
        handle_keypress(i)
