# ใช้ Python 3.9 เป็น base image
FROM python:3.9

# ตั้งค่า Working Directory
WORKDIR /app

# คัดลอกไฟล์ requirements.txt และติดตั้ง Dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกโค้ดทั้งหมดไปยัง Container
COPY . /app/

# เปิดพอร์ต 8000
EXPOSE 8000

# คำสั่งเริ่มต้นของ Container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
