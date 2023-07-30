"""module app"""

import os
import logging
import json
from config_logger import configure_logger
from quickstart import get_my_person


configure_logger()
logger = logging.getLogger("module app")


GOOGLE_CONTACTS_REST_API_URL = os.environ["GOOGLE_CONTACTS_REST_API_URL"]
GOOGLE_CONTACTS_REST_API_ENDPOINT = os.environ["GOOGLE_CONTACTS_REST_API_ENDPOINT"]
BEARER_TOKEN = os.environ["BEARER_TOKEN"]


def run() -> None:
    """
    Executes features with Google Contacts

    Returns:
        None 
    """
    print("Hello Google Contacts")
    my_person = get_my_person(
        f"{GOOGLE_CONTACTS_REST_API_URL}{GOOGLE_CONTACTS_REST_API_ENDPOINT}",
        BEARER_TOKEN
    )
    print("my_person: ", json.dumps(my_person, indent=4))


if __name__ == "__main__":
    run()
