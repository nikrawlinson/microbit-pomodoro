import microbit

def workcycle():
    
    microbit.display.scroll("Time to work")
    microbit.sleep(1000)
    for y in range(5):
        for x in range(5):
            microbit.display.set_pixel(x, y, 5)
    for y in reversed(range(5)):
        for x in reversed(range(5)):
            for stall in range(6000):
                microbit.sleep(10)
                if microbit.button_b.was_pressed():
                    return
                if microbit.button_a.was_pressed():
                    return
            microbit.display.set_pixel(x, y, 0)
    microbit.sleep(1000)
        
def restcycle():

    microbit.display.scroll("Take a break!")
    microbit.sleep(1000)
    for t in reversed(range(5)):
        time = t + 1
        microbit.display.show(time)
        for stall in range(6000):
            microbit.sleep(10)
            if microbit.button_b.was_pressed():
                return
            if microbit.button_a.was_pressed():
                return
    microbit.display.clear()
    microbit.sleep(1000)
    
def waiting():

    if microbit.button_a.was_pressed():
        while True:
            microbit.display.clear()
            if microbit.button_b.is_pressed():
                microbit.display.clear()
                return
            else:
                workcycle()
            if microbit.button_b.is_pressed():
                microbit.display.clear()
                return
            else:
                restcycle()

while True:
    waiting()
