## e2e1
* greet: hi
    - utter_greet
* request_hotel: i need an accommodation
    - hotel_form
    - form{"name": "hotel_form"}
* chitchat: are you feeling ok?
    - utter_chitchat
    - hotel_form
    - form{"name": null}
* thankyou: thanks
    - utter_noworries
    - action_restart

## e2e2
* greet: hello
    - utter_greet
* request_hotel: i need a [5](stars:5) star [hotel](property_type) in the [center](location) of [london](city)
    - hotel_form
    - form{"name": "hotel_form"}
    - form{"name": null}
* thankyou: thank you
    - utter_noworries
    - action_restart

## e2e3
* greet: hi there
    - utter_greet
* chitchat:  how are you?
    - utter_chitchat
* request_hotel: find an [apartment](property_type)
    - hotel_form
    - form{"name": "hotel_form"}
    - form{"name": null}
* thankyou: ok thanks you
    - utter_noworries
    - action_restart
    
## e2e4
* greet: hey
    - utter_greet
* request_hotel: find a [hotel](property_type) for 5 people from june 1st to june 15th
    - hotel_form
    - form{"name": "hotel_form"}
    - form{"name": null}
* thankyou: thanks for your help
    - utter_noworries
    - action_restart
    
## e2e5
* greet: good morning
    - utter_greet
* request_hotel: i need an accommodation for 3 people in the south of Madrid
    - hotel_form
    - form{"name": "hotel_form"}
* stop: you can't help me
    - utter_ask_continue
* deny: no
    - action_deactivate_form
    - form{"name": null}
    - action_restart
    
## e2e6
* greet: hello
    - utter_greet
* request_hotel: i'm looking for a b&b for 2 people
    - hotel_form
    - form{"name": "hotel_form"}
* stop: you can't help me
    - utter_ask_continue
* deny: yes
    - hotel_form
    - form{"name": null}
    - action_restart
