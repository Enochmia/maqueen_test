def mf():
  maqueen.motor_run(maqueen.Motors.All, maqueen.Dir.CW, 50)
  if maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0 or maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0:
    maqueen.motor_run(maqueen.Motors.All, maqueen.Dir.CW, 0)
    return break
  else:
    basic.pause(3000)
    maqueen.motor_run(maqueen.Motors.All, maqueen.Dir.CW, 0)
    
def mb():
  maqueen.motor_run(maqueen.Motors.All, maqueen.Dir.CCW, 50)
  basic.pause(3000)
  maqueen.motor_run(maqueen.Motors.All, maqueen.Dir.CCW, 0)

def t_(a):
  if a == "l" or a == "L":
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
    basic.pause(10)
    maqueen.motor_run(maqueen.Motors.All, maqueen.Dir.CW, 0)
  elif a == "r" or a == "R":
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
    basic.pause(10)
    maqueen.motor_run(maqueen.Motors.All, maqueen.Dir.CW, 0)
  else:
    pass
  
def check_1():
  for i in range(10)
    t_(r)
    mf()
    mb()

def check_obstacle():
    if maqueen.ultrasonic(PingUnit.CENTIMETERS) >= 0 and maqueen.ultrasonic(PingUnit.CENTIMETERS) <= 30:
        mb()
    else:
        mf()

def on_forever():

    maqueen.motor_run(maqueen.Motors.All, maqueen.Dir.CW, 50)

    if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
    
    elif maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)

    else:
        pass

basic.forever(on_forever)
