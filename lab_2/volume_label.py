def cube_vol(height, width, depth):
    volume = height * width * depth
    return volume
def vol_lab(volume):
    if volume <= 10:
        return "Extra Small"
    elif 11 <= volume <= 25:
        return "Small"
    elif 26 <= volume <= 75:
        return "Medium"
    elif 76 <= volume <= 100:
        return "Large"
    elif 101 <= volume <= 250:
        return "Extra Large"
    else:
        return "Extra-Extra Large"
height = float(input("Enter the height of the cube: "))
width = float(input("Enter the width of the cube: "))
depth = float(input("Enter the depth of the cube: "))
vol = cube_vol(height, width, depth)
label = vol_lab(vol)
print("Volume of cube:", vol, "cm3")
print("Label:", label)
