class ServoMotor:
    """
    Power Width Modulation drive.

    Definitions for PWM drive connected to
    MotorShield (with H-bridge)
    driven by ESP8266.
    """
    print('INFO: class {} running'.format(
        'servomotor.ServoMotor')
    )

    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        print('INFO: {} initialized'.format(
            self.__class__.__name__)
        )

    def __str__(self):
        return 'INFO: object: {}\n' \
               '       class: {}\n' \
               '        name: {}\n' \
               '         pin: {}' \
            .format(self.__dict__,
                    self.__class__.__name__,
                    self.name,
                    str(self.pin))

    def brrr(self):
        return 'pwmbrrrrr'

    def brv(self, val):
        return 'pwmbrrrrr' + str(val)