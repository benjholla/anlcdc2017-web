# Argonne National Labs 2017 Cyber Defense Competition HMI Web Application

This application runs on a Raspberry Pi simulating a water pump and power grid. To test locally run the `HMI_no_gpio.py` version.

## Startup
Run the application with the `python HMY.py` command. Note the user that runs the app will need to be in the `gpio` user group. Example: for the `pi` user could be `sudo adduser pi gpio`.

## Mock LDAP
To swap out the LDAP implementation with a locally mocked password hashed backed implementation rename and replace the `ldap_mock_auth.py` file to `ldap_auth.py`.

## Dependencies:

- `sudo apt-get install python3`
- `sudo apt-get install python3-pip`
- `sudo pip3 install flask`
- `sudo pip3 install RPi.GPIO`
- `sudo pip install flask_login`
- `sudo pip install python-ldap`

Note: LDAP may need `sudo apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev`

## Background
The history that of the Raspberry Pi device the HMI application was given on was not clear. It is included below for posterity.

	 1  sudo nano /etc/dhcpcd.conf
	 2  sudo reboot
	 3  ifconfig
	 4  sudo service ssh start
	 5  sudo service ssh status
	 6  ls
	 7  sudo reboot
	 8  sudo nano /etc/dhcpcd.conf
	 9  sudo reboot
	10  sudo poweroff
	11  ifconfig
	12  ping 8.8.8
	13  ping 8.8.8.8
	14  ping www.google.com
	15  sudo apt-get install python3
	16  sudo apt-get install python3-pip
	17  sudo pip3 install flask
	18  sudo pip3 install RPi.GPIO
	19  ls
	20  sudo nano /etc/dhcpcd.conf 
	21  sudo reboot
	22  sudo poweroff
	23  sudo poweroff
	24  ifconfig
	25  sudo nano /etc/dhcpcd.conf 
	26  sudo reboot
	27  sudo apt-get install vsftpd
	28  sudo nano /etc/dhcpcd.conf 
	29  sudo reboot
	30  sudo apt-get install vsftpd
	31  sudo apt-get install telnet
	32  sudo nano /etc/dhcpcd.conf 
	33  sudo passwd root
	34  sudo rm /etc/ssh/ssh_host*
	35  sudo dpkg-reconfigure openssh-server 
	36  sudo nano /etc/ssh/sshd_config 
	37  sudo nano /etc/vsftpd.conf 
	38  sudo nano /etc/issue.net 
	39  sudo nano /etc/profile.d/sshpasswd.sh 
	40  sudo adduser admin
	41  sudo adduser pumptech
	42  sudo adduser eengineer
	43  sudo usermod -aG sudo admin
	44  sudo usermod -aG sudo pumptech
	45  sudo usermod -aG sudo eengineer
	46  sudo nano /etc/passwd
	47  sudo systemctl enable vsftpd
	48  sudo systemctl enable ssh
	49  sudo reboot
	50  sudo poweroff
	51  sudo poweroff
	52  exit
