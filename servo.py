import machine
import time
# กำหนดขา GPIO สำหรับสั่งการ Servo Motor
servo_pin = 12  # เปลี่ยนตามขา GPIO ที่คุณใช้
# สร้างออบเจ็กต์ PWM บนขาที่ระบุ
pwm = machine.PWM(machine.Pin(servo_pin))
# กำหนดค่าความถี่และช่วงค่าหน้าที่ของ PWM
pwm.freq(50)  # ปรับค่านี้ตามความต้องการ
pwm.duty(77)  # ปรับค่านี้ตามความต้องการ

# ฟังก์ชันสำหรับเลื่อน Servo Motor ไปยังมุมที่กำหนด
def set_servo_angle(angle):
    # แปลงมุม (เป็นองศา) เป็นค่าหน้าที่ (duty cycle)
    duty = int(40 + (75 / 180) * angle)  # ปรับค่านี้ตามความต้องการ
    pwm.duty(duty)
    time.sleep_ms(500)  # รอให้ Servo Motor เคลื่อนที่ (ตัวเลือก)

# ตัวอย่างการใช้งาน: เลื่อน Servo Motor ไปยังมุม 0 องศา รอสักครู่ แล้วเลื่อนไปยังมุม 90 องศา
set_servo_angle(0)
time.sleep(1)  # รอเป็นเวลา 1 วินาที
set_servo_angle(90)

# ล้างและคืนทรัพยากร
pwm.deinit()
