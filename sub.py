import paho.mqtt.client as mqtt
import time

NUM_SUBSCRIBERS = 8
BROKER = '192.168.3.23'


def on_connect(client, userdata, flags, rc):
    print("{} Connected with result code {}".format(client, rc))


def on_disconnect(client, userdata, flags, rc):
    print('Reconnecting {}'.format(client))
    client.reconnect()
    client.loop_start()


def on_message(client, userdata, msg):
    print('Got {}.'.format(msg.payload.decode()))


if __name__ == '__main__':
    subscribers = [mqtt.Client() for i in range(NUM_SUBSCRIBERS)]

    for i, s in enumerate(subscribers):
        s.connect(BROKER)
        s.subscribe('topic/#'.format(i))
        s.on_message = on_message
        s.on_connect = on_connect
        s.on_disconnect = on_disconnect
        s.loop_start()

    while True:
        time.sleep(10)
