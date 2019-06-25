# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union, Optional

from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT


class HotelForm(FormAction):
    def name(self):
        return "hotel_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        if tracker.get_slot('property_type') == 'hotel':
            return ["city", "position", "num_people", "check_in", "check_out",
                "stars", "property_type"]
        else:
            return ["city", "position", "num_people", "check_in", "check_out",
                "property_type"]

    def slot_mappings(self):
        return {"city": self.from_entity(entity="city",
                                            not_intent="chitchat"),
                "position": self.from_entity(entity="position",
                                            not_intent="chitchat"),
                "num_people": [self.from_entity(entity="num_people",
                                                not_intent=["chitchat"]),
                               self.from_entity(entity="number")],
                "check_in": self.from_entity(entity="check_in",
                                            not_intent="chitchat"),
                "check_out": self.from_entity(entity="check_out",
                                            not_intent="chitchat"),
                "property_type": self.from_entity(entity="property_type",
                                            not_intent="chitchat"),
                "stars": self.from_entity(entity="stars",
                                            not_intent="chitchat")}

    @staticmethod
    def position_db():
        return ["center",
                "north",
                "east",
                "south",
                "west",
                "suburbs"]
                
    @staticmethod
    def property_type_db():
        return ["apartment",
                "hotel",
                "guest house",
                "hostel",
                "b&b",
                "villa"
                "boat"]

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_position(self,
                         value: Text,
                         dispatcher: CollectingDispatcher,
                         tracker: Tracker,
                         domain: Dict[Text, Any]) -> Optional[Text]:

        if value.lower() in self.position_db():
            # validation succeeded
            return {"position": value}
        else:
            dispatcher.utter_template('utter_wrong_option', tracker)
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"position": None}

    def validate_property_type(self,
                         value: Text,
                         dispatcher: CollectingDispatcher,
                         tracker: Tracker,
                         domain: Dict[Text, Any]) -> Optional[Text]:

        if value.lower() in self.property_type_db():
            # validation succeeded
            return {"property_type": value}
        else:
            dispatcher.utter_template('utter_wrong_option', tracker)
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"property_type": None}

    def validate_num_people(self,
                            value: Text,
                            dispatcher: CollectingDispatcher,
                            tracker: Tracker,
                            domain: Dict[Text, Any]) -> Optional[Text]:
        """Validate num_people value."""

        if self.is_int(value) and int(value) > 0:
            return {"num_people": value}
        else:
            dispatcher.utter_template('utter_wrong_num_people', tracker)
            # validation failed, set slot to None
            return {"num_people": None}

    def validate_stars(self,
                            value: Text,
                            dispatcher: CollectingDispatcher,
                            tracker: Tracker,
                            domain: Dict[Text, Any]) -> Optional[Text]:
        """Validate stars value."""

        if self.is_int(value) and int(value) > 0 and int(value) < 6:
            return {"stars": value}
        else:
            dispatcher.utter_template('utter_wrong_stars', tracker)
            # validation failed, set slot to None
            return {"stars": None}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template('utter_submit', tracker)
        return []

