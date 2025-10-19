import re
import requests
import logging

from src.utils.get_secret import get_secret


def extract(sm_client, search_term: str, date_from=None):
    """Function retrieves records from the Guardian API

    Given a search term and "date from", retrieves relevant
    records from the API. It also retrieves the API key from
    secrets manager

    Args:
      search_term: the term that will be searched
      date_from: an optional date field

    Returns: list of dictionaries containing returned filtered api data
    """
    # logic to validate the search_term data type and validity
    if not isinstance(search_term, str) or not search_term:
        raise TypeError("Search Terms must be a non-empty string")

    # secret name
    secret_name = "guardian-api"

    # Retrieve Secret
    key_retrieval = get_secret(sm_client, secret_name)

    params = {
        "q": f'"{search_term}"',
        "page-size": 10,
        "show-fields": "body",
        "api-key": key_retrieval,
    }
    # Logic to add date_from parameter to the request params dictionary
    if date_from:
        regex = re.compile(r"[0-9]{4}\-[0-9]{2}\-[0-9]{2}")
        match = re.match(regex, date_from)

        if not (match):
            raise TypeError("Date format should be as follows: YYYY-MM-DD")
        else:
            params["from-date"] = date_from

    try:
        response = requests.get(
            "https://content.guardianapis.com/search?", params=params
        )
        data = response.json()
        response.raise_for_status()  # triggers the exceptions
        results = data.get("response", {}).get("results", [])
        return results
    except requests.exceptions.HTTPError as errh:
        logging.error("HTTP Error: %s", errh)
        raise
    except requests.exceptions.ConnectionError as errc:
        logging.error("Connection Error: %s", errc)
        raise
    except requests.exceptions.Timeout as errt:
        logging.error("Timeout Error: %s", errt)
        raise
    except requests.exceptions.RequestException as err:
        logging.error("Something Else: %s", err)
        raise
