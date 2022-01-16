import pigpio
import time

pi1 = pigpio.pi()

pi1.write(13, 0)
pi1.write(19, 0)

pi1.write(26, 0)

while True:
	for i in range(0, 101):
		pi1.set_PWM_dutycycle(19, i)
		time.sleep(0.005)
		

	for i in range(100, -1, -1):
		pi1.set_PWM_dutycycle(19, i)
		time.sleep(0.005)

	for i in range(0, 101):
		pi1.set_PWM_dutycycle(26, i)
		time.sleep(0.005)
		

	for i in range(100, -1, -1):
		pi1.set_PWM_dutycycle(26, i)
		time.sleep(0.005)

	for i in range(0, 101):
		pi1.set_PWM_dutycycle(13, i)
		time.sleep(0.005)
		

	for i in range(100, -1, -1):
		pi1.set_PWM_dutycycle(13, i)
		time.sleep(0.005)

	for i in range(0, 101):
		pi1.set_PWM_dutycycle(19, i)

		pi1.set_PWM_dutycycle(13, i)
		pi1.set_PWM_dutycycle(26, i)
		time.sleep(0.005)
		

	for i in range(100, -1, -1):
		pi1.set_PWM_dutycycle(19, i)

		pi1.set_PWM_dutycycle(13, i)
		pi1.set_PWM_dutycycle(26, i)
		time.sleep(0.005)
