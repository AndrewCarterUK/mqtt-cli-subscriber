from unittest import TestCase
import subscriber

class TestSubscriber(TestCase):
    def test_parse_args_default(self):
        args = subscriber.parse_args(['echo'])

        self.assertEqual('echo', args.command)
        self.assertEqual('localhost', args.host)
        self.assertEqual(1883, args.port)
        self.assertIsNone(args.username)
        self.assertIsNone(args.password)
        self.assertEqual('#', args.subscription)
        self.assertEqual('', args.client_id)
        self.assertTrue(args.clean_session)

    def test_parse_args_provided(self):
        args = subscriber.parse_args([
            'echo',
            '-H', 'host',
            '-P', '9999',
            '-u', 'foo',
            '-p', 'bar',
            '-s', 'topic',
            '-i', 'id',
            '--no-clean-session'
        ])

        self.assertEqual('echo', args.command)
        self.assertEqual('host', args.host)
        self.assertEqual(9999, args.port)
        self.assertEqual('foo', args.username)
        self.assertEqual('bar', args.password)
        self.assertEqual('topic', args.subscription)
        self.assertEqual('id', args.client_id)
        self.assertFalse(args.clean_session)
