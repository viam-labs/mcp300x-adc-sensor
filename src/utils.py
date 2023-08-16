def get_gpio_from_pin(pin:int):
    map_pin_gpio = dict()
    map_pin_gpio[3] = 2
    map_pin_gpio[5] = 3
    map_pin_gpio[7] = 4
    map_pin_gpio[11] = 17
    map_pin_gpio[13] = 27
    map_pin_gpio[15] = 22
    map_pin_gpio[19] = 10
    map_pin_gpio[21] = 9
    map_pin_gpio[23] = 11
    map_pin_gpio[27] = 0
    map_pin_gpio[29] = 5
    map_pin_gpio[31] = 6
    map_pin_gpio[33] = 13
    map_pin_gpio[35] = 19
    map_pin_gpio[37] = 26
    map_pin_gpio[8] = 14
    map_pin_gpio[10] = 15
    map_pin_gpio[12] = 18
    map_pin_gpio[16] = 23
    map_pin_gpio[18] = 24
    map_pin_gpio[22] = 25
    map_pin_gpio[24] = 8
    map_pin_gpio[26] = 7
    map_pin_gpio[28] = 1
    map_pin_gpio[32] = 12
    map_pin_gpio[36] = 16
    map_pin_gpio[38] = 20
    map_pin_gpio[40] = 21

    return map_pin_gpio[pin]
