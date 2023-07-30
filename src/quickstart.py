"""module quickstart"""

import logging
import requests
from config_logger import configure_logger

configure_logger()
logger = logging.getLogger("module quickstart")


def get_rest_api_response(rest_api_endpoint, bearer_token) -> dict:
    """
    Returns a REST API response.

    Args:
        rest_api_endpoint (str): The REST API endpoint to call.
        bearer_token (str): The bearer token to use for authentication.

    Returns:
        A dictionary containing the response status and content.

    Raises:
        requests.exceptions.ConnectionError: If the API endpoint could not be connected to.
        requests.exceptions.HTTPError: If the request failed.

    """
    response_content = {
        "status": "failed",
        "content": {},
    }
    headers = {
        "Authorization": f"Bearer {bearer_token}",
    }
    try:
        response = requests.get(rest_api_endpoint, headers=headers, timeout=10)
        if response.status_code == 200:
            response_content["status"] = "success"
            response_content["content"] = response.json()
            return response_content
        else:
            response_content["content"] = response.status_code
            return response_content
    except requests.exceptions.ConnectionError as err:
        logger.exception(
            "Could not connect to the API endpoint %s, error: %s", rest_api_endpoint, err
        )
        return response_content
    except requests.exceptions.HTTPError as err:
        logger.exception(
            "The request failed with status code %s, error: %s", response.status_code, err
        )
        return response_content


def get_my_person(rest_api_endpoint, bearer_token) -> dict:
    """
    Returns the user's person data from the REST API.

    Args:
        rest_api_endpoint: The REST API endpoint to call.
        bearer_token: The bearer token to use for authentication.

    Returns:
        A dictionary containing the user's person data.

    """
    response = get_rest_api_response(rest_api_endpoint, bearer_token)
    if response["status"] == "success":
        return response["content"]
    else:
        return {}
