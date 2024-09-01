I purchased a Keybow 2040 macro pad from Pimoroni. It was challenging to set up multiple layers for different applications, but I managed to create something close to my ideal setup. The most surprising part is that I created everything using ChatGPT's Code Copilot. I can't write code at all, and I'm not a programmer.

I was able to create multiple layers using QMK Configurator and generate a UF2 file, but I gave up halfway because I couldn't figure out how to configure the LEDs in detail. With CircuitPython, it might not be the smartest method, but I was able to customize the LED layout to my liking.

Usage: By default, it is set to Layer 1. When you press the Fn key in the bottom left corner, it transitions to the layer selection screen. From there, you can move to your desired layer. The Fn key can be moved to any position, but it cannot overlap with the layer position on the layer selection screen. The keycode has not been set yet.

I referred to the following site for key codes: https://docs.circuitpython.org/projects/hid/en/latest/index.html

I tried to incorporate the icons I often use in Blender and MagicaVoxel into the layers.
