def main():
    for i in range(90):
        script.input(1,('KEY_B',),-6113,32033,0,0) # Bad angle, runs slightly too long
    script.input(1,('KEY_A',),0,0,0,0)

from core.main import script
script = script()
script.run(main)
