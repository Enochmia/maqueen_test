def on_forever():
    if maqueen.ultrasonic(PingUnit.CENTIMETERS) >= 20:
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0:
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
        elif maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
        else:
            maqueen.motor_run(maqueen.Motors.All, maqueen.Dir.CW, 50)

basic.forever(on_forever)
