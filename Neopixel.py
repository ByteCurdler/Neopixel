import board,neopixel,sys

def pixelGridCreator(w,h,xFlip=False,yFlip=False):
    pixelGrid = []
    pixel = 0
    if(xFlip):
        x = w
    else:
        x = 1
    if(yFlip):
        y = h
    else:
        y = 1

    xo = w
    yo = h

    pixelGrid.append(str(x) + "," + str(y))
    while(pixel < (xo * yo) - 1):
        for i in range(yo - 1):
            if(yFlip):
                y -= 1
            else:
                y += 1
            pixelGrid.append(str(x) + "," + str(y))
            pixel += 1
        if(xFlip):
            x -= 1
        else:
            x += 1
        if(pixel < (xo * yo) - 1):
            pixelGrid.append(str(x) + "," + str(y))
            pixel += 1
            for i in range(yo - 1):
                if(yFlip):
                    y += 1
                else:
                    y -= 1
                pixelGrid.append(str(x) + "," + str(y))
                pixel += 1
            if(pixel < (xo * yo) - 1):
                if(xFlip):
                    x -= 1
                else:
                    x += 1
                pixelGrid.append(str(x) + "," + str(y))
                pixel += 1
    return pixelGrid

class Pad:
    def __init__(self,w,h,brightness=50, autoUpdate=False,order="GRB",xFlip=False,yFlip=False):
        self.grid = pixelGridCreator(w,h,xFlip,yFlip)
        
        ORDER       = eval("neopixel." + order)
        
        self.strip = neopixel.NeoPixel(board.D18, w*h, auto_write=autoUpdate, brightness=(brightness/255), pixel_order=ORDER)
        try:
            self.strip[0] = (0, 0, 0)
        except RuntimeError:
            print("Neopixel setup failed, did you run as superuser?")
            sys.exit(-5)
        
    def setPixel(self,x,y,r,g,b):
        self.strip[self.grid.index(str(x) + "," + str(y))] = (r,g,b)

    def getPixel(self,x,y):
        return self.strip[self.grid.index(str(x) + "," + str(y))]

    def fill(self,r,g,b):
        self.strip.fill((r,g,b))

    def update(self):
        self.strip.show()

class Wheel:
    def __init__(self,w,brightness=30, autoUpdate=False,order="GRB"):        
        ORDER       = eval("neopixel." + order)

        self.w = w
        
        self.strip = neopixel.NeoPixel(board.D18, w, auto_write=autoUpdate, brightness=(brightness/255), pixel_order=ORDER)
        try:
            self.strip[0] = (0, 0, 0)
        except RuntimeError:
            print("Neopixel setup failed, did you run as superuser?")
            sys.exit(-5)
        
    def setPixel(self,x,r,g,b):
        self.strip[x % self.w] = (r,g,b)

    def getPixel(self,x):
        return self.strip[x % self.w]

    def update(self):
        self.strip.show()

class Strip:
    def __init__(self,w,brightness=30, autoUpdate=False,order="GRB"):        
        ORDER       = eval("neopixel." + order)
        
        self.strip = neopixel.NeoPixel(board.D18, w, auto_write=autoUpdate, brightness=(brightness/255), pixel_order=ORDER)
        try:
            self.strip[0] = (0, 0, 0)
        except RuntimeError:
            print("Neopixel setup failed, did you run as superuser?")
            sys.exit(-5)
        
    def setPixel(self,x,r,g,b):
        self.strip[x] = (r,g,b)

    def getPixel(self,x):
        return self.strip[x]

    def update(self):
        self.strip.show()
