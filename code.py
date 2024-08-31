import board
from keybow2040 import Keybow2040
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time
from layers import LAYER_1, LAYER_2, LAYER_3, LAYER_100

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
    'LAYER_100': LAYER_100
}

# 現在のレイヤー（初期状態はLAYER_1）
current_layer = LAYER_1

# 各キーの押下状態を追跡するリストとタイミング
key_state = [False] * 16
last_keypress_time = [0] * 16  # キーが最後に押された時間を記録
repeat_delay = 0.3  # 長押し時の初回遅延（秒）
repeat_interval = 0.05  # 長押し時の繰り返し間隔（秒）

def set_layer_leds(layer):
    """指定されたレイヤーの色でキーのLEDを設定"""
    for i in range(16):
        if layer['name'] in ['LAYER_1', 'LAYER_2']:
            if i in layer['color_map']:
                keys[i].set_led(*layer['color_map'][i])
            else:
                keys[i].set_led(0, 0, 0)  # 消灯
        elif layer['name'] == 'LAYER_100':
            if i in layer['active_indexes']:
                keys[i].set_led(*layer['color'])
            else:
                keys[i].set_led(0, 0, 0)  # 消灯
        else:
            keys[i].set_led(*layer['color'])

def handle_keypress(layer, index):
    """押されたキーに対応するキーコードを送信し、Fnキーやレイヤー切り替えキーを処理する"""
    global current_layer

    current_time = time.monotonic()

    if keys[index].pressed:
        if not key_state[index]:
            key_state[index] = True  # キーが押されたことを記録
            last_keypress_time[index] = current_time
            process_key(layer, index)
        elif current_time - last_keypress_time[index] >= repeat_delay:
            if current_time - last_keypress_time[index] >= repeat_interval:
                last_keypress_time[index] = current_time
                process_key(layer, index)
    else:
        key_state[index] = False  # キーがリリースされたことを記録

def process_key(layer, index):
    """キー押下時の処理を実行"""
    global current_layer

    if index == FN_KEY_INDEX:
        # Fnキーが押されたらLAYER_100に切り替え
        current_layer = LAYER_100
        set_layer_leds(current_layer)

    elif current_layer['name'] == 'LAYER_100':
        # LAYER_100でのレイヤー移動
        if index == 3:
            current_layer = LAYER_1
        elif index == 7:
            current_layer = LAYER_2
        elif index == 11:
            current_layer = LAYER_3
        set_layer_leds(current_layer)

    elif layer['keycodes']:
        # 通常のキーコードを送信
        keycode = layer['keycodes'][index]

        if isinstance(keycode, tuple):
            # キーの組み合わせがタプルで定義されている場合、順次送信
            keyboard.press(*keycode)
            keyboard.release(*keycode)
        else:
            # 通常のキーコードを送信
            keyboard.send(keycode)

# メインループ
set_layer_leds(current_layer)  # 初期のLED設定
while True:
    keybow.update()
    for i in range(16):
        handle_keypress(current_layer, i)
