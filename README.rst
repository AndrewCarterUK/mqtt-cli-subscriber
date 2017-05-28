MQTT CLI Subscriber
===================

.. image:: https://travis-ci.org/AndrewCarterUK/mqtt-cli-subscriber.svg?branch=master
   :target: https://travis-ci.org/AndrewCarterUK/mqtt-cli-subscriber

.. image:: https://scrutinizer-ci.com/g/AndrewCarterUK/mqtt-cli-subscriber/badges/quality-score.png?b=master
   :target: https://scrutinizer-ci.com/g/AndrewCarterUK/mqtt-cli-subscriber/

This tool allows subscription you to subscribe to messages from an MQTT broker
and forward them to a command line tool of your choosing.

Install
-------

``pip install mqtt-cli-subscriber``

``mqtt-cli-subscriber -h``

The program calls the provided command with two provided values, ``-t`` for the
topic and ``-p`` for the message payload (base64 encoded).
