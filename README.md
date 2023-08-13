<h1 align="center" id="title">Raising the alarm by ringing the phone | Raspberry PICO, GSM 800L</h1>

<p id="description">A project related to calling a phone to a selected number when a signal is detected. In my case it was information about the end of the watering machine. Components used to build the circuit: Raspberry Pi Pico</p>

<h2>🛠️ Components :</h2>
<p> </p>
<p>1. Raspberry Pi Pico</p>
<p>2. GPRS GSM SIM800L V2.0</p>
<p>3. Step-down LM2596 3,2V-35V 3A</p>
<p>4. SIM card</p>
<p>5. 2x 18650 Battery</p>

<h2>💻 The concept:</h2>
The Raspberry Pico monitors the status on the GPIO. When it detects the closure of a circuit (in my case it was a magnetic reed switch) it makes three phone calls to a selected number thus alerting the detected condition. The microcontroller's communication with the GSM module is through the UART using AT commands. It is possible to configure sending SMS on detection of an alarm.
<h2>📚 Modules:</h2>
The program was written in Python.
<p> </p>
<p>· main.py </p>
<p>· sim800l.py -> you can use this module in order to configure send SMS</p>
<p>· s900l.py  -> responsible for handling calls</p>
<h2>⚡ Electrical diagram:</h2>
<a href="https://imgur.com/RagxC7A"><img src="https://i.imgur.com/RagxC7A.png" title="source: imgur.com" /></a>
<h2>📷 Photo:</h2>
<a href="https://imgur.com/pEzJboc"><img src="https://i.imgur.com/pEzJboc.jpg" title="source: imgur.com" /></a>
<a href="https://imgur.com/3nCrnjO"><img src="https://i.imgur.com/3nCrnjO.jpg" title="source: imgur.com" /></a>
<a href="https://imgur.com/HUJQ0S0"><img src="https://i.imgur.com/HUJQ0S0.jpg" title="source: imgur.com" /></a>
