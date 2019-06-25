## happy path
* greet
    - utter_greet
* request_hotel
    - hotel_form
    - form{"name": "hotel_form"}
    - form{"name": null}
* thankyou
    - utter_noworries
    - action_restart

## unhappy path
* greet
    - utter_greet
* request_hotel
    - hotel_form
    - form{"name": "hotel_form"}
* chitchat
    - utter_chitchat
    - hotel_form
    - form{"name": null}
* thankyou
    - utter_noworries
    - action_restart

## very unhappy path
* greet
    - utter_greet
* request_hotel
    - hotel_form
    - form{"name": "hotel_form"}
* chitchat
    - utter_chitchat
    - hotel_form
* chitchat
    - utter_chitchat
    - hotel_form
* chitchat
    - utter_chitchat
    - hotel_form
    - form{"name": null}
* thankyou
    - utter_noworries
    - action_restart

## stop but continue path
* greet
    - utter_greet
* request_hotel
    - hotel_form
    - form{"name": "hotel_form"}
* stop
    - utter_ask_continue
* affirm
    - hotel_form
    - form{"name": null}
* thankyou
    - utter_noworries
    - action_restart

## stop and really stop path
* greet
    - utter_greet
* request_hotel
    - hotel_form
    - form{"name": "hotel_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - action_restart

## chitchat stop but continue path
* request_hotel
    - hotel_form
    - form{"name": "hotel_form"}
* chitchat
    - utter_chitchat
    - hotel_form
* stop
    - utter_ask_continue
* affirm
    - hotel_form
    - form{"name": null}
* thankyou
    - utter_noworries
    - action_restart

## stop but continue and chitchat path
* greet
    - utter_greet
* request_hotel
    - hotel_form
    - form{"name": "hotel_form"}
* stop
    - utter_ask_continue
* affirm
    - hotel_form
* chitchat
    - utter_chitchat
    - hotel_form
    - form{"name": null}
* thankyou
    - utter_noworries
    - action_restart

## chitchat stop but continue and chitchat path
* greet
    - utter_greet
* request_hotel
    - hotel_form
    - form{"name": "hotel_form"}
* chitchat
    - utter_chitchat
    - hotel_form
* stop
    - utter_ask_continue
* affirm
    - hotel_form
* chitchat
    - utter_chitchat
    - hotel_form
    - form{"name": null}
* thankyou
    - utter_noworries
    - action_restart

## chitchat, stop and really stop path
* greet
    - utter_greet
* request_hotel
    - hotel_form
    - form{"name": "hotel_form"}
* chitchat
    - utter_chitchat
    - hotel_form
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - action_restart

## Generated Story 5877317745845911027
* greet
    - utter_greet
* request_hotel{"property_type": "hotel", "position": "center", "city": "rome"}
    - slot{"city": "rome"}
    - slot{"position": "center"}
    - slot{"property_type": "hotel"}
    - hotel_form
* thankyou
    - utter_noworries
    - action_restart

## Generated Story 3494217169294297253
* greet
    - utter_greet
* request_hotel{"property_type": "apartment", "num_people": "2"}
    - slot{"num_people": "2"}
    - slot{"property_type": "apartment"}
    - hotel_form
* thankyou
    - utter_noworries
    - action_restart

## Generated Story 2803206485468560834
* greet
    - utter_greet
* request_hotel{"property_type": "hostel", "num_people": "6", "city": "berlin"}
    - slot{"city": "berlin"}
    - slot{"num_people": "6"}
    - slot{"property_type": "hostel"}
    - hotel_form
* thankyou
    - utter_noworries
    - action_restart

## Generated Story -2428595096935927906
* greet
    - utter_greet
* request_hotel{"property_type": "hotel", "stars": "3"}
    - slot{"property_type": "hotel"}
    - slot{"stars": "3"}
    - hotel_form
* thankyou
    - utter_noworries
    - action_restart
