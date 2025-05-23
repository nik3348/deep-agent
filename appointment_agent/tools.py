import os
import requests
from google.adk.tools.tool_context import ToolContext

CARRO_API_KEY = os.getenv('CARRO_API_KEY')


def get_appointment_options() -> dict:
    """
    Fetches available appointment options from the Carro API.
    Returns a dictionary containing the appointment options.
    """
    url = 'https://api.carro.bot/actions/staging-cx/my/v1/appointment/options'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': CARRO_API_KEY
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def get_appointment_timeslots(location_id: str) -> dict:
    """
    Fetches available appointment timeslots from the Carro API.

    Args:
        env (str): Environment (e.g., 'staging-cx')
        country_code (str): Country code (e.g., 'my')
        location_id (str): Location identifier
        slot_type (str): Type of appointment slot

    Returns:
        dict: Dictionary containing the available timeslots or error message
    """
    url = f'https://api.carro.bot/actions/staging-cx/my/v1/appointment/options/timeslots/{location_id}/inspection'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': CARRO_API_KEY
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def schedule_appointment(location_id: str, start_time: str, time_slot: str) -> dict:
    """
    Schedules an appointment using the Carro API.

    Args:
        location_id (str): The ID of the selected location from state key 'selected_location'
        start_time (str): The start time of the appointment from state key 'selected_timeslot' in format 'YYYY-MM-DD HH:MM:SS' (e.g., '2025-05-28 16:00:00')
        time_slot (str): The selected time slot from state key 'selected_timeslot' in format 'HH:MM' (e.g., '08:00')

    Returns:
        dict: Response from the API or error message
    """
    url = 'https://api.carro.bot/actions/staging-cx/my/v1/appointment'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': CARRO_API_KEY
    }
    payload = {
        'ticket_id': 2428259,
        'location_id': location_id,
        'start_time': start_time,
        'time_slot': time_slot,
        'slot_type': 'inspection'
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def save_location(location_id: str, location_name: str, tool_context: ToolContext) -> dict:
    """
    Saves the user's confirmed location in the state.

    Args:
        location_id (str): The ID of the confirmed location
        location_name (str): The name of the confirmed location
        tool_context (ToolContext): The tool context containing the state

    Returns:
        dict: Success message with the saved location details
    """
    # Save the location details in the state
    tool_context.state["selected_location"] = {
        "id": location_id,
        "name": location_name
    }
    return {"message": f"Location saved: {location_name}: {location_id}"}


def save_timeslot(selected_timeslot: str, tool_context: ToolContext) -> dict:
    """
    Saves the user's confirmed date and time in the state.

    Args:
        date (str): The selected date in YYYY/MM/DD format
        time (str): The selected time
        tool_context (ToolContext): The tool context containing the state

    Returns:
        dict: Success message or error if timeslot is invalid
    """
    # Save both date and time in the state
    tool_context.state["selected_timeslot"] = selected_timeslot

    return {
        "message": f"Timeslot saved: {selected_timeslot}",
    }


def get_locations() -> dict:
    """
    Fetches available locations from the Carro API.
    Returns a dictionary containing only the abbreviation, address, and id for each location.
    """
    url = 'https://api.carro.bot/captain-api/staging-cx/my/v1/locations'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': CARRO_API_KEY
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Filter only the required fields
        filtered_locations = []
        for location in data.get('data', []):
            filtered_location = {
                'abbreviation': location.get('abbreviation'),
                'address': location.get('address'),
                'id': location.get('id')
            }
            filtered_locations.append(filtered_location)

        return {'locations': filtered_locations}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
