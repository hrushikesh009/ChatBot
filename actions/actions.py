from typing import Any, Text, Dict, List, Union


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType

class ValidateHealthForm(Action):

    def name(self) -> Text:
        return "health_form"
    
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
        ) -> List[EventType]:
            requried_slots = ["confirm_exercise","exercise","sleep","stress","diet","goal"]

            for slot_name in requried_slots:
                if tracker.slots.get(slot_name) is None:
                    return[SlotSet("requested_slot", slot_name)]
            
            return[SlotSet("requested_slot", "None")]

class ActionSubmit(Action):

    def name(self) -> Text:
        return "action_submit"

    def run(
        self, 
        dispatcher,
        tracker:Tracker,
        domain: "DomainDict"
        ) -> List[Dict[Text, Any]]:
             dispatcher.utter_message(template="utter_slots_values",
             confirm_exercise = tracker.get_slot("confirm_exercise"),
             exercise = tracker.get_slot("exercise"),
             sleep = tracker.get_slot("sleep"),
             stress = tracker.get_slot("stress"),
             diet = tracker.get_slot("diet"),
             goal = tracker.get_slot("goal"))