# Argonne National Labs 2017 Cyber Defense Competition HMI Web Application

This application runs on a Raspberry Pi simulating a water pump and power grid. To test locally run the `HMI_no_gpio.py` version.

## Dependencies:

- `sudo apt-get install python3`
- `sudo apt-get install python3-pip`
- `sudo pip3 install flask`
- `sudo pip3 install RPi.GPIO`
- `sudo pip install flask_login`
- `sudo pip install python-ldap`

Note: LDAP may need `sudo apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev`