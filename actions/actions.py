from typing import Any, Text, Dict, List, Union
#from dotenv import load_dotenv


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType

# import requests
# import json
# import os

#load_dotenv()

# airtable_api_key = "keygndbwgYAXGKCM0"#os.getenv("AIRTABLE_API_KEY")
# base_id = "appK9sTQeYGRttlxy"#os.getenv("BASE_ID")
# table_name = "Table%201"#os.getenv("TABLE_NAME")


# def create_health_log(confirm_exercise, exercise, sleep, diet, stress, goal):
#     request_url = f"https://api.airtable.com/v0/{base_id}/{table_name}?api_key={airtable_api_key}"

#     headers = {
#         "Content-Type": "application/json",
#         "Accept": "application/json",
#         "Authorization": f"Bearer {airtable_api_key}",
#     }
#     data = {
#         "fields": {
#             "Exercised?": confirm_exercise,
#             "Type of exercise": exercise,
#             "Amount of sleep": sleep,
#             "Stress": stress,
#             "Diet": diet,
#             "Goal": goal,
#         }
#     }
#     try:
#         response = requests.post(
#             request_url, headers=headers, data=json.dumps(data)
#         )
#         response.raise_for_status()
#     except requests.exceptions.HTTPError as err:
#         raise SystemExit(err)

#     print(response.status_code)
#     return response


# class ValidateHealthForm(Action):

#     def name(self) -> Text:
#         return "health_form"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         requried_slots = ["confirm_exercise", "exercise",
#                           "sleep", "stress", "diet", "goal","option_selection","address","payment_options"]

#         for slot_name in requried_slots:
#             if tracker.slots.get(slot_name) is None:
#                 return[SlotSet("requested_slot", slot_name)]

#         return[SlotSet("requested_slot", "None")]


# class ActionSubmit(Action):

#     def name(self) -> Text:
#         return "action_submit"

#     def run(
#         self,
#         dispatcher,
#         tracker: Tracker,
#         domain: "DomainDict"
#     ) -> List[Dict[Text, Any]]:

#         confirm_exercise = tracker.get_slot("confirm_exercise")
#         exercise = tracker.get_slot("exercise")
#         sleep = tracker.get_slot("sleep")
#         stress = tracker.get_slot("stress")
#         diet = tracker.get_slot("diet")
#         goal = tracker.get_slot("goal")
        

#         response = create_health_log(
#             confirm_exercise=confirm_exercise,
#             exercise=exercise,
#             sleep=sleep,
#             stress=stress,
#             diet=diet,
#             goal=goal
#         )

#         dispatcher.utter_message(
#             text="Thanks, your answers have been recorded!")
#         return []

class ActionRecommender(Action):

    def name(self) -> Text:
        return "action_recommend_products"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict"
    ) -> List[Dict[Text, Any]]:

        option_select = tracker.get_slot("option_select")
        
        dispatcher.utter_message(
           response ="utter_ask_user_to_selected_product")
        return[SlotSet("requested_slot", option_select)]

class ActionLookupAddress(Action):

    def name(self) -> Text:
        return "action_address_lookup"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict"
    ) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(
           text="Address added!")
        return[]

class ActionAddAddress(Action):

    def name(self) -> Text:
        return "action_address_lookup"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict"
    ) -> List[Dict[Text, Any]]:

        current_address = tracker.get_slot("address")
        
        dispatcher.utter_message(
           text="We could not Found address Can you please enter address here!")
        return[SlotSet("address", current_address)]
    
class ActionPlaceOrder(Action):

    def name(self) -> Text:
        return "action_place_order"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict"
    ) -> List[Dict[Text, Any]]:

        Payment_selected = tracker.get_slot("payment_type")
        
        if Payment_selected == "Cod":
            dispatcher.utter_message(text="Please Confirm Your Cod Order by typing Yes")
        else:
            dispatcher.utter_message(text="Here goes your Link")
        return []
