import board
from keybow2040 import Keybow2040
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time
from layers import LAYER_1, LAYER_2, LAYER_3, LAYER_4, LAYER_5, LAYER_6, LAYER_7, LAYER_8, LAYER_100

# Keybow 2040のセットアップ
i2c = board.I2C()
keybow = Keybow2040(i2c)
keys = keybow.keys

# キーボードセットアップ
keyboard = Keyboard(usb_hid.devices)

# Fnキーのインデックス
FN_KEY_INDEX = 0

# レイヤー管理用の辞書
LAYERS = {
    'LAYER_1': LAYER_1,
    'LAYER_2': LAYER_2,
    'LAYER_3': LAYER_3,
    'LAYER_4': LAYER_4,
    'LAYER_5': LAYER_5,
    'LAYER_6': LAYER_6,
    'LAYER_7': LAYER_7,
    'LAYER_8': LAYER_8,
    'LAYER_100': LAYER_100
}

# 現在のレイヤー（初期状態はLAYER_1）
current_layer = LAYER_1

# 各キーの押下状態を追跡するリストとタイミング
key_state = [False] * 16  # 各キーの押下状態を追跡
last_keypress_time = [0] * 16  # キーが最後に押された時間を記録
initial_keypress_delay = 0.5  # 最初のキー押下後の遅延時間（秒）
repeat_interval = 0.03  # 長押し時の繰り返し間隔（秒）
initial_delay_done = [False] * 16  # 初回遅延が完了したかを追跡

def set_layer_leds(layer):
    """指定されたレイヤーの色でキーのLEDを設定"""
    color_map = layer.get('color_map', {})

    for i in range(16):
        if i in color_map:
            keys[i].set_led(*color_map[i])
        else:
            keys[i].set_led(0, 0, 0)  # 消灯

def handle_keypress(layer, index):
    """押されたキーに対応するキーコードを送信し、Fnキーやレイヤー切り替えキーを処理する"""
    global current_layer

    current_time = time.monotonic()

    if keys[index].pressed:
        if not key_state[index]:
            key_state[index] = True  # キーが押されたことを記録
            last_keypress_time[index] = current_time
            initial_delay_done[index] = False  # 初回遅延のフラグをリセット
            process_key(layer, index)
        elif key_state[index]:
            if not initial_delay_done[index]:
                if current_time - last_keypress_time[index] >= initial_keypress_delay:
                    initial_delay_done[index] = True  # 初回遅延を完了
                    last_keypress_time[index] = current_time
                    process_key(layer, index)
            elif current_time - last_keypress_time[index] >= repeat_interval:
                last_keypress_time[index] = current_time
                process_key(layer, index)
    else:
        key_state[index] = False  # キーがリリースされたことを記録
        initial_delay_done[index] = False  # 初回遅延のフラグをリセット


import time

def process_key(layer, index):
    """キー押下時の処理を実行"""
    global current_layer

    layer_switch = {
        3: LAYER_1,
        7: LAYER_2,
        11: LAYER_3,
        15: LAYER_4,
        2: LAYER_5,
        6: LAYER_6,
        10: LAYER_7,
        14: LAYER_8
    }

    if index == FN_KEY_INDEX:
        # Fnキーが押されたらLAYER_100に切り替え
        current_layer = LAYER_100
        set_layer_leds(current_layer)

    elif current_layer['name'] == 'LAYER_100':
        # LAYER_100でのレイヤー移動
        if index in layer_switch:
            current_layer = layer_switch[index]
            set_layer_leds(current_layer)
            time.sleep(0.05)

    elif layer['keycodes'] and index < len(layer['keycodes']):
        # 通常のキーコードを送信
        keycode = layer['keycodes'][index]

        if isinstance(keycode, tuple):
            keyboard.press(*keycode)
            keyboard.release(*keycode)
        else:
            keyboard.send(keycode)


    elif layer['keycodes'] and index < len(layer['keycodes']):
        # 通常のキーコードを送信
        keycode = layer['keycodes'][index]

        if isinstance(keycode, tuple):
            keyboard.press(*keycode)
            keyboard.release(*keycode)
        else:
            keyboard.send(keycode)



# メインループ
set_layer_leds(current_layer)  # 初期のLED設定
while True:
    keybow.update()
    for i in range(16):
        handle_keypress(current_layer, i)
