---
# Sistem Pendeteksi Gerakan dengan Raspberry Pi

Proyek ini bertujuan untuk membuat sistem pendeteksi gerakan menggunakan Raspberry Pi, sensor PIR, dan buzzer. Sistem ini akan mendeteksi gerakan dan mengaktifkan buzzer sebagai tanda adanya gerakan yang terdeteksi.

## Daftar Isi

- [Latar Belakang](#latar-belakang)
- [Tujuan Proyek](#tujuan-proyek)
- [Komponen yang Dibutuhkan](#komponen-yang-dibutuhkan)
- [Instalasi](#instalasi)
- [Cara Menggunakan](#cara-menggunakan)
- [Struktur Kode](#struktur-kode)
- [Hasil dan Kesimpulan](#hasil-dan-kesimpulan)
- [Tim Pengembang](#tim-pengembang)

## Latar Belakang

Proyek ini dikembangkan sebagai bagian dari program studi Teknologi Internet of Things (TIoT) di Institut Teknologi Del. Sistem ini dirancang untuk mendeteksi gerakan menggunakan sensor PIR dan memberikan notifikasi dengan mengaktifkan buzzer.

## Tujuan Proyek

- Mempelajari dan mengimplementasikan sistem pendeteksi gerakan dengan Raspberry Pi.
- Mengembangkan kemampuan dalam mengintegrasikan perangkat keras dan perangkat lunak.
- Menyediakan solusi sederhana untuk pendeteksian gerakan yang dapat digunakan untuk berbagai aplikasi seperti keamanan dan otomatisasi rumah.

## Komponen yang Dibutuhkan

- Raspberry Pi 3
- Sensor PIR
- Buzzer
- Kabel Jumper
- Breadboard

## Instalasi

1. **Setup Raspberry Pi**: Pastikan Raspberry Pi Anda sudah terinstall Raspbian OS dan memiliki akses ke terminal.

2. **Instalasi Library GPIO**:
   ```bash
   sudo apt-get update
   sudo apt-get install python3-rpi.gpio
   ```

3. **Download atau Clone Repository Ini**:
   ```bash
   git clone https://github.com/username/repository-name.git
   cd repository-name
   ```

## Cara Menggunakan

1. **Menyusun Rangkaian**:
   - Hubungkan sensor PIR ke GPIO 17 (BCM).
   - Hubungkan buzzer ke GPIO 18 (BCM).
   - Pastikan semua sambungan sudah benar dan sesuai dengan gambar rangkaian.

2. **Menjalankan Program**:
   ```bash
   python3 motion_detector.py
   ```

3. **Kode Program**:
   Berikut adalah kode program yang digunakan:
   ```python
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
   ```

## Struktur Kode

- `motion_detector.py`: Script utama yang mengatur pendeteksi gerakan dan buzzer.

## Hasil dan Kesimpulan

Proyek ini berhasil mengimplementasikan sistem pendeteksi gerakan menggunakan Raspberry Pi dan sensor PIR. Sistem ini dapat mendeteksi gerakan dan mengaktifkan buzzer sebagai notifikasi. Implementasi ini dapat digunakan sebagai dasar untuk aplikasi keamanan dan otomatisasi rumah  .

## Tim Pengembang

- Thalia Aniceta Saragih
- Dion Saputra Manurung
- Louis Cristiano Panggabean

Proyek ini dikembangkan sebagai bagian dari program studi Teknologi Internet of Things (TIoT) di Institut Teknologi Del.

---
