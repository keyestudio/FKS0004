# I2C LCD library for the micro:bit
# Thanks to adafruit_Python_SSD1306 library by Dmitrii (dmitryelj@gmail.com)
# Thanks to lopyi2c.py
# Thanks to ssd1306.py
# Author: 
# v1.0
# Only supports display type I2C128x64

from microbit import Image, i2c
from ustruct import pack_into

# LCD Control constants
ADDR = 0x3C
screen = bytearray(513)  # send byte plus pixels
screen[0] = 0x40
zoom = 1


def command(c):
    i2c.write(ADDR, b'\x00' + bytearray(c))


def initialize():
    cmd = [
        [0xAE],                     # SSD1306_DISPLAYOFF
        [0xA4],                     # SSD1306_DISPLAYALLON_RESUME
        [0xD5, 0xF0],               # SSD1306_SETDISPLAYCLOCKDIV
        [0xA8, 0x3F],               # SSD1306_SETMULTIPLEX
        [0xD3, 0x00],               # SSD1306_SETDISPLAYOFFSET
        [0 | 0x0],                  # line #SSD1306_SETSTARTLINE
        [0x8D, 0x14],               # SSD1306_CHARGEPUMP
        # 0x20 0x00 horizontal addressing
        [0x20, 0x00],               # SSD1306_MEMORYMODE
        [0x21, 0, 127],             # SSD1306_COLUMNADDR
        [0x22, 0, 63],              # SSD1306_PAGEADDR
        [0xa0 | 0x1],               # SSD1306_SEGREMAP
        [0xc8],                     # SSD1306_COMSCANDEC
        [0xDA, 0x12],               # SSD1306_SETCOMPINS
        [0x81, 0xCF],               # SSD1306_SETCONTRAST
        [0xd9, 0xF1],               # SSD1306_SETPRECHARGE
        [0xDB, 0x40],               # SSD1306_SETVCOMDETECT
        [0xA6],                     # SSD1306_NORMALDISPLAY
        [0xd6, 1],                  # zoom on
        [0xaf]                      # SSD1306_DISPLAYON
    ]
    for c in cmd:
        command(c)


def set_pos(col=0, page=0):
    command([0xb0 | page])  # page number
    # take upper and lower value of col * 2
    c1, c2 = col * 2 & 0x0F, col >> 3
    command([0x00 | c1])  # lower start column address
    command([0x10 | c2])  # upper start column address


def clear_oled(c=0):
    global screen
    set_pos()
    for i in range(1, 513):
        screen[i] = 0
    draw_screen()


def set_zoom(v):
    global zoom
    if zoom != v:
        command([0xd6, v])  # zoom on/off
        command([0xa7 - v])  # inverted display
        zoom = v


def draw_screen():
    set_zoom(1)
    set_pos()
    i2c.write(ADDR, screen)

def add_text(x, y, text, draw=1):
    for i in range(0, min(len(text), 12 - x)):
        for c in range(0, 5):
            col = 0
            for r in range(1, 6):
                p = Image(text[i]).get_pixel(c, r - 1)
                col = col | (1 << r) if (p != 0) else col
            ind = x * 10 + y * 128 + i * 12 + c * 2 + 1
            screen[ind], screen[ind + 1] = col, col
    if draw == 1:
        set_zoom(1)
        set_pos(x * 5, y)
        ind0 = x * 10 + y * 128 + 1
        i2c.write(ADDR, b'\x40' + screen[ind0:ind + 1])

def set_px(x, y, color, draw=1):    #按照2*2点阵绘制，x范围[0~63]，y范围[0,31]
    page, shift_page = divmod(y, 8)
    ind = x * 2 + page * 128 + 1
    b = screen[ind] | (1 << shift_page) if color else screen[ind] & ~ (1 << shift_page)
    pack_into(">BB", screen, ind, b, b)
    if draw:
        set_pos(x, page)
        i2c.write(0x3c, bytearray([0x40, b, b]))


def get_px(x, y):
    page, shift_page = divmod(y, 8)
    ind = x * 2 + page * 128 + 1
    b = (screen[ind] & (1 << shift_page)) >> shift_page
    return b

def draw_square(x1,y1,x2,y2,color,draw=1):
    for i in range(x1,x2+1):
        set_px(i,y1,color,0)
    for i in range(y1,y2+1):
        set_px(x1,i,color,0)
    for i in range(x1,x2+1):
        set_px(i,y2,color,0)
    for i in range(y1,y2+1):
        set_px(x2,i,color,0)
    if(draw):
        draw_screen()

def reverse():
    for i in range(1,513):
        screen[i]=255-screen[i]
    draw_screen()
