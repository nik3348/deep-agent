from google.adk.agents import Agent
from appointment_agent.prompts import location_confirmation_prompt, timeslot_confirmation_prompt, schedule_appointment_prompt, coordinator_prompt
from appointment_agent.tools import get_appointment_timeslots, get_locations, save_location, save_timeslot, schedule_appointment

MODEL = "gemini-2.0-flash"


location_confirmation = Agent(
    name="LocationConfirmation",
    model=MODEL,
    description="Confirms location from the user.",
    instruction=location_confirmation_prompt,
    tools=[
        get_locations,
        save_location
    ],
)


timeslot_confirmation = Agent(
    name="TimeslotConfirmation",
    model=MODEL,
    description="Confirms the timeslot from the user using the selected location.",
    instruction=timeslot_confirmation_prompt,
    tools=[
        get_appointment_timeslots,
        save_timeslot
    ],
)


appointment_scheduler = Agent(
    name="AppointmentScheduler",
    model=MODEL,
    description="Schedules the appointment with the gathered data.",
    instruction=schedule_appointment_prompt,
    tools=[schedule_appointment]
)


root_agent = Agent(
    name="AppointmentSchedulerCoordinator",
    model=MODEL,
    description="Main coordinator that orchestrates the appointment scheduling process by delegating to specialized agents for location and timeslot selection.",
    instruction=coordinator_prompt,
    sub_agents=[
        location_confirmation,
        timeslot_confirmation,
        appointment_scheduler
    ],
)
