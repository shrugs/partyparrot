import unittest
import partyparrot


class TestPartyParrot(unittest.TestCase):

    # every good open source project has tests
    # whether or not they actually matter is up for discussion

    partyparrot_result = """:partyparrot::partyparrot::partyparrot::partyparrot::partyparrot:\n  :partyparrot:  \n  :partyparrot:  \n  :partyparrot:  \n  :partyparrot:  \n\n\n:partyparrot::partyparrot::partyparrot::partyparrot::partyparrot:\n:partyparrot:    \n:partyparrot::partyparrot::partyparrot::partyparrot::partyparrot:\n:partyparrot:    \n:partyparrot::partyparrot::partyparrot::partyparrot::partyparrot:\n\n\n :partyparrot::partyparrot::partyparrot::partyparrot:\n:partyparrot:    \n :partyparrot::partyparrot::partyparrot: \n    :partyparrot:\n:partyparrot::partyparrot::partyparrot::partyparrot: \n\n\n:partyparrot::partyparrot::partyparrot::partyparrot::partyparrot:\n  :partyparrot:  \n  :partyparrot:  \n  :partyparrot:  \n  :partyparrot:  \n\n\n"""

    joy_result = """:joy::joy::joy::joy::joy:\n  :joy:  \n  :joy:  \n  :joy:  \n  :joy:  \n\n\n:joy::joy::joy::joy::joy:\n:joy:    \n:joy::joy::joy::joy::joy:\n:joy:    \n:joy::joy::joy::joy::joy:\n\n\n :joy::joy::joy::joy:\n:joy:    \n :joy::joy::joy: \n    :joy:\n:joy::joy::joy::joy: \n\n\n:joy::joy::joy::joy::joy:\n  :joy:  \n  :joy:  \n  :joy:  \n  :joy:  \n\n\n"""

    def test_conversion(self):
        self.assertEqual(
            partyparrot.convert_str_to_emoji('TEST', emojis=[':partyparrot:']),
            self.partyparrot_result
        )

    def test_arbitrary_emojis(self):
        self.assertEqual(
            partyparrot.convert_str_to_emoji('TEST', emojis=[':joy:']),
            self.joy_result
        )


if __name__ == '__main__':
    unittest.main()
