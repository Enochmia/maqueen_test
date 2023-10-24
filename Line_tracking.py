""" #V1
while True: #0 is when sensor light is off
  maqueen.motor_run(maqueen.Motors.All, maqueen.Dir.CW, 50)
  
  if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0:
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
  elif maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
"""    

""" #V2
while True: #0 is when sensor light is off
  maqueen.motor_run(maqueen.Motors.All, maqueen.Dir.CW, 50)
  
  if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0:
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
  elif maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)

#maqueen.motor_run(maqueen.Motors.All, maqueen.Dir.CW, 0)
"""








"""

while True:
    if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
    if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1:
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)



def on_button_pressed_b():
    servos.P0.set_angle(105)
input.on_button_pressed(Button.B, on_button_pressed_b)

# Request latest result from HUSKYLENS at start of FOREVER so that each time it repeats it has the latest result
# 
# If MOVE variable is set to TRUE - show the recognised ID# from the HUSKYLENS & display its number / light LED based on the result
# 
# If MOVE is set to FALSE turn off BOTH MaQueen LED & Display X on MicroBit
def Line_patrol():
    if maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_L1) == 0 and (maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_M) == 1 and maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_R1) == 0):
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.ALL_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            80)
    if maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_L1) == 1 and (maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_M) == 1 and maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_R1) == 0):
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            30)
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            80)
    if maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_L1) == 1 and (maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_M) == 0 and maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_R1) == 0):
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            0)
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            80)
    if maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_L1) == 0 and (maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_M) == 1 and maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_R1) == 1):
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            80)
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            30)
    if maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_L1) == 0 and (maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_M) == 0 and maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_R1) == 1):
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            80)
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            0)
huskylens.init_i2c()
huskylens.init_i2c()
huskylens.init_mode(protocolAlgorithm.ALGORITHM_TAG_RECOGNITION)
basic.clear_screen()
servos.P0.set_angle(0)

def on_forever():
    while maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_L1) == 0 or (maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_M) == 0 or maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_R1) == 0):
        Line_patrol()
basic.forever(on_forever)

def on_forever2():
    Move = 0
    huskylens.request()
    if Move:
        if huskylens.is_appear(5, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
            servos.P0.set_angle(105)
        elif huskylens.is_appear(7, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
            servos.P0.set_angle(145)
        elif huskylens.is_appear(2, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
            servos.P0.set_angle(165)
        elif huskylens.is_appear(1, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
            servos.P0.set_angle(180)
        else:
            pass
basic.forever(on_forever2)
"""
