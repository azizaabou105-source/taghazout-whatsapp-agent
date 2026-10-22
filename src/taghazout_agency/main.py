#!/usr/bin/env python
import sys
import warnings
from taghazout_agency.crew import TaghazoutAgency

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    inputs = {
        'user_message': 'Salam, chhal katssawbo site de reservation?',
        'sender_phone': '212600000000'
    }
    TaghazoutAgency().crew().kickoff(inputs=inputs)
