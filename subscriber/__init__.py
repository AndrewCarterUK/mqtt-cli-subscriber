import paho.mqtt.client as mqtt
import argparse
import subprocess
import base64
import sys

def parse_args(argv):
    parser = argparse.ArgumentParser(description='Subscribe to an MQTT broker with a command line program')
    parser.add_argument('command', type=str)
    parser.add_argument('-H', '--host', type=str, default='localhost')
    parser.add_argument('-P', '--port', type=int, default=1883)
    parser.add_argument('-u', '--username', type=str, default=None)
    parser.add_argument('-p', '--password', type=str, default=None)
    parser.add_argument('-s', '--subscription', type=str, default='#')
    parser.add_argument('-i', '--client-id', type=str, default='')
    parser.add_argument('--no-clean-session', dest='clean_session', action='store_false')
    parser.set_defaults(clean_session=True)

    return parser.parse_args(argv)

def on_connect(client, userdata, flags, rc):
    client.subscribe(userdata.subscription)

def on_message(client, userdata, msg):
    p = subprocess.Popen([userdata.command, '-t', msg.topic, '-p', base64.b64encode(msg.payload)])
    p.wait()

def main():
    args = parse_args(sys.argv[1:])

    client = mqtt.Client(client_id=args.client_id, clean_session=args.clean_session, userdata=args)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(args.host, args.port, 60)

    client.loop_forever()
