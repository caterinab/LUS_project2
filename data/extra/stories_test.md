## test1
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
* chitchat
    - utter_chitchat
    - hotel_form
    - form{"name": null}
* thankyou
    - utter_noworries
    - action_restart

## test2
* greet
    - utter_greet
* chitchat
    - utter_chitchat
* chitchat
    - utter_chitchat
* request_hotel
    - hotel_form
    - form{"name": "hotel_form"}
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

## test3
* greet
    - utter_greet
* chitchat
    - utter_chitchat
* chitchat
    - utter_chitchat
* request_hotel
    - hotel_form
    - form{"name": "hotel_form"}
    - form{"name": null}
* thankyou
    - utter_noworries
    - action_restart

## test4
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

## test5
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
* stop
    - utter_ask_continue
* affirm
    - hotel_form
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - action_restart

