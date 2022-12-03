import numpy as np
import matplotlib.pyplot as mp
import os
import pdb

ch3_diode = np.genfromtxt('processed_data/ch3_clamp_diode_031222.csv', delimiter=',')
ch2_pwm = np.genfromtxt('processed_data/ch2_pwm_031222.csv', delimiter=',')
ch1_thermo = np.genfromtxt('processed_data/ch1_thermo_031222.csv', delimiter=',')



time = ch2_pwm[:,0]
time = time[1:] + -1*time[1]        # Removing "nan"


ch3_diode = ch3_diode[:,1]
ch3_diode = ch3_diode[1:]
ch2_pwm = ch2_pwm[:,1]
ch2_pwm = ch2_pwm[1:]
ch1_thermo = ch1_thermo[:,1]
ch1_thermo = ch1_thermo[1:]


 #  _____  _       _   _   _             
 # |  __ \| |     | | | | (_)            
 # | |__) | | ___ | |_| |_ _ _ __   __ _ 
 # |  ___/| |/ _ \| __| __| | '_ \ / _` |
 # | |    | | (_) | |_| |_| | | | | (_| |
 # |_|    |_|\___/ \__|\__|_|_| |_|\__, |
 #                                  __/ |
 #                                 |___/ 

fig1, (ax1, ax2, ax3) = mp.subplots(3, constrained_layout=True)
fig1.suptitle('Thermocoupler voltage when heater on 2022-12-03')
ax1.plot(time, ch2_pwm) 
ax2.plot(time, ch1_thermo)
ax3.plot(time, ch3_diode)


ax1.set_title('12V PWM Supply')
ax1.set_xlabel('Time [S]')
ax1.set_ylabel('Voltage [V]')

ax2.set_title('Thermocoupler Voltage')
ax2.set_xlabel('Time [S]')
ax2.set_ylabel('Voltage [V]')

ax3.set_title('Clamping Diode Voltage')
ax3.set_xlabel('Time [S]')
ax3.set_ylabel('Voltage [V]')

ax1.set_ylim(-.1, np.amax(ch2_pwm) * 1.1)
ax2.set_ylim(-.01, np.amax(ch1_thermo) * 1.1)
ax3.set_ylim(-.01, np.amax(ch3_diode) * 1.1)

mp.figure()
mp.title('Thermocoupler voltage when heater on 2022-12-03')
mp.plot(time[1000:2000], ch2_pwm[1000:2000], label='12V PWM') 
mp.plot(time[1000:2000], ch1_thermo[1000:2000], label='Thermocoupler voltage')
mp.plot(time[1000:2000], ch3_diode[1000:2000], label='Diode voltage')
mp.grid()
mp.legend()

#pdb.set_trace()

mp.show()

