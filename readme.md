## Project Information
- **IRB 340 Delta Robot Simulation**
- **Description**
    ทางผู้จัดทำได้พัฒนา Simulation เพื่อจำลองการเคลื่อนที่ของ Delta Robot ในรูปแบบ Pick and Paste โดยเริ่มต้นจากการสร้างหน้า GUI ด้วยภาษา Python จาก Library Tkinter เป็นระบบส่วน Front-End ให้รับค่า Input พิกัดในแกน X Y และ Z จากผู้ใช้ โดยมี 2 โหมดด้วยกันได้แก่ โหมดที่ 1 คือ การกำหนดพิกัดในการเคลื่อนที่ให้กับ Delta Robot เป็นจุด และ โหมดที่ 2 คือ กำหนดพิกัดจุดในการเคลื่อนที่ทั้งหมดที่ต้องการที่จะให้ Delta Robot เคลื่อนที่ไป จากนั้นระบบจะทำการนำพิกัดเหล่านี้ส่งค่าไปยังระบบส่วน Back-End ที่มีการเขียนโปรแกรมเพื่อนำพิกัด Path ของตำแหน่งปลายที่ได้ไปใช้ในการ Generate Trajectory angle ออกมาใช้ในการควบคุม Joint แต่ละ Joint ของหุ่นยนต์ ซึ่งจะเริ่มจากการนำพิกัดตำแหน่งปลายไป Generate Trajectory ด้วยหลักการ linearly interpolating ในส่วนของตำแหน่งในการเคลื่อนที่ออกมาจากตำแหน่งปัจจุบันไปจนถึงตำแหน่งปลายที่ต้องการ จากนั้นนำค่า Trajectory ในแต่ละช่วงไปคำนวณ Inverse kinematics เพื่อให้ได้องศาในการเคลื่อนที่ของแต่ละ Joint ที่จะต้องเคลื่อนที่ในแต่ละช่วง เพื่อนำค่านั้นไป Generate Trajectory angle ออกมา ถ้าหากคำนวณแล้วเกิด Singularity ค่านั้นจะไม่ถูกนำไปใช้ ระบบจะทำการแจ้งเตือน และนำตำแหน่งก่อนหน้าที่จะเกิด Singularity มาใช้คำนวณแทน
- **Features**
    โหมดที่ 1 (Point Mode)คือ การกำหนดพิกัดในการเคลื่อนที่ให้กับ Delta Robot เป็นจุด 
    โหมดที่ 2 (Pose Mode)คือ กำหนดพิกัดจุดในการเคลื่อนที่ทั้งหมดที่ต้องการที่จะให้ Delta Robot เคลื่อนที่ไป 

## Table of Contents
- Provide a structured outline of your README for easy navigation.

## Installation
- Python
- Tkinter Library
- Matplotlib Library
- Numpy Library

## Usage
- ไฟล์ประกอบด้วย 7 ไฟล์ โดยมีรายละเอียด ดังนี้
    - README File
    - Front End Files
        -  mainpage.py คือ การเขียน GUI หน้าหลักของระบบ Simulation
        -  mode1.py คือ หน้ารับ input พิกัด X Y และ Z จากผู้ใช้ ของ Point Mode
        -  mode2.py คือ หน้ารับ input ว่าผู้ใช้ต้องการแสดงกี่ pose และกรอกพิกัด X Y และ Z จากผู้ใช้ ของ Pose Mode
    - Back End Files
        -  plotting_simulation.py คือ โปรแกรม Plot การเคลื่อนที่ของ Delta Robot
        -  robot_computation.py คือ โปรแกรมคำนวณ inverse kinematic / singularity / trajectory generator    
        -  pose_mode.py คือ โปรแกรมที่รับค่ามาจากส่วนของ Front End แล้วนำไปเข้าคำนวณใน robot_computation.py ในส่วน Pose Mode
        -  point_mode.py คือ โปรแกรมที่รับค่ามาจากส่วนของ Front End แล้วนำไปเข้าคำนวณใน robot_computation.py ในส่วน Point Mode
- **วิธีการใช้:** กด run ที่ไฟล์ mainpage ระบบจะทำการแสดงหน้ารวมโหมดที่มีใน Delta Robot Simulation โดยประกอบไปด้วย
        -  โหมดที่ 1 คือ การกำหนดพิกัดในการเคลื่อนที่ให้กับ Delta Robot เป็นจุด 
        -  โหมดที่ 2 คือ กำหนดพิกัดจุดในการเคลื่อนที่ทั้งหมดที่ต้องการที่จะให้ Delta Robot เคลื่อนที่ไป

## Contact n Support
- ณัฐชนนท์ สิงหา 64340500017
- ธนพรรณ เรืองสุข 64340500025

## Versioning
- Version 1 13/12/2023

## Credits and Acknowledgments
- Big thanks to ...
(1)	X.Chen. (2020). Delta Robot kinematics 3dprinting–Building by learning, University of Washington
(2)	Chinedum Okwudire. (2020). Vibration Compensation of Delta 3D Printer with Position-varying Dynamics using Filtered B-Splines, University of Michigan
(3)	Meryam Rachadi. (2015). Design of an H∞ controller for the Delta robot: experimental results
(4) Sebastian. (2016). Delta Robot Simulation

## Conclusion
- ภายในโปรแกรม Delta Robot Simulation ที่จัดทำขึ้นเพื่อจำลองการเคลื่อนที่ของหุ่นยนต์รุ่น IRB 340 เท่านั้น ประกอบไปด้วยกัน 2 โหมดคือ โหมดที่ 1 คือ การกำหนดพิกัดในการเคลื่อนที่ให้กับ Delta Robot เป็นจุด และ โหมดที่ 2 คือ กำหนดพิกัดจุดในการเคลื่อนที่ทั้งหมดที่ต้องการที่จะให้ Delta Robot เคลื่อนที่ไป โดยผู้ใช้สามารถเลือกใช้โหมดตามความต้องการของผู้ใช้ผ่านหน้า Main Page
