import math

def crop(width, height, rows, columns, index):
    if(index >= columns * rows):
        print("index cannot be greater total cells, setting to 0")
        index = 0

    croppedWidth = width / columns

    xOffset = math.floor(croppedWidth * (index % columns))
    croppedWidth = math.floor(xOffset + croppedWidth)

    croppedHeight = math.floor(height / rows)
    yOffset = math.floor(croppedHeight * math.floor(index / rows))
    croppedHeight = math.floor(yOffset + croppedHeight)

    return [xOffset, croppedWidth, yOffset, croppedHeight]
