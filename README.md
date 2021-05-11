####Setup steps:

    1. Setup a Twilio account.
    2. Fill in the "from" and "to" numbers in the sms.json file.
    3. Set environment variables "TWILIO_ACCOUNT_SID" and "TWILIO_AUTH_TOKEN" with your credentials.
    

####Ways to run the scripts:
    
    1. Invoke any one of the following scripts(slots_by_district/slots_by_pincode)
        E.g. python slots_by_district.py
        The above command will prompt values to be entered by the user.
        
    2. Run the "slots_by_district" script by passing the following arguments(state, district, day, duration(hours))
        E.g. python slots_by_district.py maharashtra pune today 1 

    3. Run the "slots_by_pincode" script by passing the following arguments(pin code, day, duration(hours))\
        E.g. python slots_by_pincode.py 411052 today 1
