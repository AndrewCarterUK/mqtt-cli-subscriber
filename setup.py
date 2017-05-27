from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mqtt-cli-subscriber',
    version='0.1.0',

    description='Subscribe to messages from an MQTT broker using a command',
    long_description=long_description,

    url='https://github.com/AndrewCarterUK/mqtt-cli-subscriber',

    author='Andrew Carter',
    author_email='andrewcarter1992@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='mqtt subscriber',

    packages=['subscriber'],

    install_requires=['paho-mqtt'],

    entry_points={
        'console_scripts': [
            'mqtt-cli-subscriber=subscriber:main',
        ],
    },
)
