huskylens.init_i2c()
huskylens.init_mode(protocolAlgorithm.ALGORITHM_FACE_RECOGNITION)

def on_forever():
    huskylens.request()
    serial.write_value("x", huskylens.readeBox_index(1, 1, Content1.X_CENTER))

while True:
    
    maqueen.motor_run(maqueen.Motors.All, maqueen.Dir.CW, 0) #base speed both motors
    
    if huskylens.is_appear(1, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK) = True: #getting coordinates of box? maybe
        on_forever()
    
        if 0 < x < 160: #following face
            x = 160-x
            x = x/16
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50-x) #M1 is left side servo
        elif 0 < x <=320:
            x = x - 160
            x = x/16
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50-x) #M2 is left side servo
        else:
            pass

"""
huskylens.init_i2c()
huskylens.init_mode(protocolAlgorithm.ALGORITHM_FACE_RECOGNITION)
huskylens.request()
serial.write_value("x", huskylens.readeBox_index(1, 1, Content1.X_CENTER))


maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
huskylens.isAppear_s(HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK)
huskylens.is_appear(1, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK)
"""
