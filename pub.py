import paho.mqtt.client as mqtt
from datetime import datetime
import time

NUM_PUBLISHERS = 8
NUM_TOPICS = 10
TOPICS = ['topic/' + str(i) for i in range(NUM_TOPICS)]
BROKER = '192.168.3.23'


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


def on_disconnect(client, userdata, flags, rc):
    print('Reconnecting {}'.format(client))
    client.reconnect()


def on_message(client, userdata, msg):
    print('Got {}.'.format(msg.payload.decode()))


if __name__ == '__main__':
    publishers = [mqtt.Client() for i in range(NUM_PUBLISHERS)]

    for p in publishers:
        p.connect(BROKER)
        p.on_message = on_message
        p.on_disconnect = on_disconnect

    v = 0
    while True:
        pubid = v % NUM_PUBLISHERS
        topid = v % NUM_TOPICS
        msg = '{} from {}'.format(str(datetime.now()), pubid)
        print('Publishing {}'.format(msg))
        publishers[pubid].publish('topic/{}'.format(topid), msg)
        v += 1
        time.sleep(5)
