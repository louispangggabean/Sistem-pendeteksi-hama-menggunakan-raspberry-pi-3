import RPi.GPIO as GPIO
import time

# Setup GPIO
pir_sensor = 17  # Ubah menjadi pin GPIO yang Anda gunakan untuk sensor PIR
buzzer_pin = 18  # Ubah menjadi pin GPIO yang Anda gunakan untuk buzzer
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_sensor, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)
    try:

  while True:
        if GPIO.input(pir_sensor):
            print("Gerakan terdeteksi!")
            GPIO.output(buzzer_pin, GPIO.HIGH)  # Aktifkan buzzer
            time.sleep(1)  # Buzzer berbunyi selama 1 detik
            GPIO.output(buzzer_pin, GPIO.LOW)  # Matikan buzzer
        else:
            GPIO.output(buzzer_pin, GPIO.LOW)  # Pastikan buzzer mati jika tidak ada gerakan
        time.sleep(0.1)  # Berhenti sebentar sebelum memeriksa lagi
except KeyboardInterrupt:
    GPIO.cleanup()
