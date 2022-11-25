def main():
    script.input(30,('KEY_X',),0,0,0,0)
    script.input(1,('KEY_X',),0,0,0,0)
    script.input(1,('KEY_X',),0,0,0,0)
    script.input(30,('KEY_PLUS',),0,0,0,0)
    script.wait(140)
    for i in range(90):
        script.input(1,('KEY_B',),-12881,30110,0,0) # Bad angle, runs slightly too long
    script.input(1,('KEY_A',),0,0,0,0)
    for i in range(1101):
        if i % 4 > 1:
            script.input(1,('KEY_B',),0,0,0,0)
        else:
            script.input(1,('NONE',),0,0,0,0)

from core.main import script
script = script()
script.run(main)
