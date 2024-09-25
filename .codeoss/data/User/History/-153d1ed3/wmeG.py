from airflow.models import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago


with DAG(
    "exercise3_fan_in_dag",
    start_date=days_ago(1),
    schedule_interval="@once",
    tags=["exercise"]
) as dag:

    # Exercise3: Fan-in Pipeline
    # ใน exercise นี้จะได้รู้จักการเขียน task ใน pipeline ขั้นตอนเยอะขึ้น
    # ใช้ DummyOperator เป็น task จำลอง
    
    t = [DummyOperator(task_id="task_{i}") for i in range(7)]

    [t[2],t[1],t[0]] >> t[4] >> t[6] << [t[5],t[3]]
    
    # TODO: สร้าง DummyOperator เพื่อสร้าง dependency ที่ซับซ้อน ตามรูป
