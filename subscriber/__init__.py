import paho.mqtt.client as mqtt
import argparse
import subprocess
import base64

parser = argparse.ArgumentParser(description='Subscribe to an MQTT broker with a command line program')
parser.add_argument('command', type=str)
parser.add_argument('-H', '--host', type=str, default='localhost')
parser.add_argument('-P', '--port', type=int, default=1883)
parser.add_argument('-u', '--username', type=str, default=None)
parser.add_argument('-p', '--password', type=str, default=None)
parser.add_argument('-s', '--subscription', type=str, default='#')
parser.add_argument('-i', '--client-id', type=str, default='')
parser.add_argument('-c', '--clean-session', type=bool, default=True)

args = parser.parse_args()

def on_connect(client, userdata, flags, rc):
    client.subscribe(args.subscription)

def on_message(client, userdata, msg):
    p = subprocess.Popen([args.command, '-t', msg.topic, '-p', base64.b64encode(msg.payload)])
    p.wait()

def main():
    client = mqtt.Client(client_id=args.client_id, clean_session=args.clean_session)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(args.host, args.port, 60)

    client.loop_forever()
