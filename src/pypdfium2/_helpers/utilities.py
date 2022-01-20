# SPDX-FileCopyrightText: 2022 geisserml <geisserml@gmail.com>
# SPDX-License-Identifier: Apache-2.0 OR BSD-3-Clause


def translate_rotation(rotation: int) -> int:
    """
    Convert a rotation value in degrees to a PDFium rotation constant.
    """
    
    if rotation == 0:
        return 0
    elif rotation == 90:
        return 1
    elif rotation == 180:
        return 2
    elif rotation == 270:
        return 3
    else:
        raise ValueError(f"Invalid rotation {rotation}") 


def _hex_digits(c):
    
    hxc = hex(c)[2:]
    
    if len(hxc) == 1:
        hxc = "0" + hxc
    
    return hxc
    

def colour_as_hex(r, g, b, a=255) -> int:
    """
    Convert a colour given as integers of ``red, green, blue, alpha`` ranging from 0 to 255
    to a single value in 8888 ARGB format.
    """
    
    colours = (a, r, g, b)
    
    for c in colours:
        assert isinstance(c, int)
        assert 0 <= c <= 255
    
    hxc_str = "0x"
    for c in colours:
        hxc_str += _hex_digits(c)
    
    hxc_int = int(hxc_str, 0)
    
    return hxc_int
