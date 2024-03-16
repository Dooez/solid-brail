from copy import *
import numpy as np
bits_l = np.array([1, 2, 4, 64])
bits_r = np.array([8, 16, 32, 128])

arr0 = [[True,False,True,False],[True,True,False,True]]
out = ''


def foo(num):
    values = [bits_l & num, bits_r & num]
    start_y = 1100
    start_x = 0
    height_step = -350
    width_step = 300
    started = False
    start_point = [0,0]

    out = 'StartChar: uni' + str(2800 + num) + '\n'
    encoding = str(10240 + num)
    out += 'Encoding: ' + encoding + ' ' + encoding + ' ' + str(10845 + num)
    out += 'Width: ' + str(width_step * 2) + '''
Flags: W
LayerCount: 2
Fore
SplineSet
'''
    
    current_point = [start_x, start_y]
    idx_col = 0
    for idx_left in range(5):
        if (started and (idx_left == 4 or not values[idx_col][idx_left])):
            out += str(current_point[0]) + ' ' + str(current_point[1])+ ' l 1 \n' 
            next_point = copy(current_point)
            next_point[0] += width_step
            out += str(next_point[0]) +' ' + str(next_point[1])+ ' l 1 \n' 
            next_point = copy(start_point)
            next_point[0] += width_step
            out += str(next_point[0]) +' ' + str(next_point[1]) + ' l 1 \n' 
            out += str(start_point[0]) +' ' + str(start_point[1]) + ' l 1 \n' 
            started = False
        elif(idx_left < 4 and values[idx_col][idx_left]):
            if (not started):
                out +=  str(current_point[0]) + ' ' + str(current_point[1])+ ' m 1 \n'
                start_point = copy(current_point)
                started = True
        current_point[1] += height_step


    current_point = [start_x + width_step, start_y]
    idx_col = 1
    for idx_left in range(5):
        if (started and (idx_left == 4 or not values[idx_col][idx_left])):
            out += str(current_point[0]) + ' ' + str(current_point[1])+ ' l 1 \n' 
            next_point = copy(current_point)
            next_point[0] += width_step
            out += str(next_point[0]) +' ' + str(next_point[1])+ ' l 1 \n' 
            next_point = copy(start_point)
            next_point[0] += width_step
            out += str(next_point[0]) +' ' + str(next_point[1]) + ' l 1 \n' 
            out += str(start_point[0]) +' ' + str(start_point[1]) + ' l 1 \n' 
            started = False
        elif(idx_left < 4 and values[idx_col][idx_left]):
            if (not started):
                out +=  str(current_point[0]) + ' ' + str(current_point[1])+ ' m 1 \n'
                start_point = copy(current_point)
                started = True
        current_point[1] += height_step
    out += '''
EndSplineSet
EndChar
    '''
    return out

header = '''
SplineFontDB: 3.2
FontName: SolidBraile
FullName: SolidBraile
FamilyName: SolidBraile
Weight: Regular
Copyright: Copyright (c) 2024, marifey
UComments: "2024-3-15: Created with FontForge (http://fontforge.org)"
Version: 001.000
ItalicAngle: 0
UnderlinePosition: -100
UnderlineWidth: 50
Ascent: 800
Descent: 200
InvalidEm: 0
LayerCount: 2
Layer: 0 0 "Back" 1
Layer: 1 0 "Fore" 0
XUID: [1021 140 -1927802171 14722573]
OS2Version: 0
OS2_WeightWidthSlopeOnly: 0
OS2_UseTypoMetrics: 1
CreationTime: 1710516307
ModificationTime: 1710576171
OS2TypoAscent: 0
OS2TypoAOffset: 1
OS2TypoDescent: 0
OS2TypoDOffset: 1
OS2TypoLinegap: 0
OS2WinAscent: 0
OS2WinAOffset: 1
OS2WinDescent: 0
OS2WinDOffset: 1
HheadAscent: 0
HheadAOffset: 1
HheadDescent: 0
HheadDOffset: 1
OS2Vendor: 'PfEd'
DEI: 91125
Encoding: UnicodeFull
UnicodeInterp: none
NameList: AGL For New Fonts
DisplaySize: -48
AntiAlias: 1
FitToEm: 0
WinInfo: 10175 37 6
beginchars: 1114112 255
'''
footer = '''
EndChars
EndSplineFont
'''

font = header
for i in range(1,256):
    font += foo(i)

font += footer

file = open('SolidBraile.sfd', 'w')
file.write(font)

