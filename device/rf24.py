from RF24 import RF24, RF24_PA_LOW

radio = RF24(17, 0)
if not radio.begin():
    raise RuntimeError("Radio hardware is not responding")
radio.setPALevel(RF24_PA_LOW)

def write(address: bytes, payload: bytes):
    radio.openWritingPipe(address)
    radio.write(payload, len(payload))
