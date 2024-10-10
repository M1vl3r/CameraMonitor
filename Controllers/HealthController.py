from Connection.db_config import create_connection
from Models.CameraHealth import CameraHealth

class HealthController:
    def __init__(self):
        self.connection = create_connection()

    def get_camera_health(self):
        query = "SELECT * FROM camera_health"
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        health_data = [CameraHealth(*result) for result in results]
        return health_data

    def add_health_record(self, camera_id, check_date, is_operational, issue_description):
        query = "INSERT INTO camera_health (camera_id, check_date, is_operational, issue_description) VALUES (%s, %s, %s, %s)"
        cursor = self.connection.cursor()
        cursor.execute(query, (camera_id, check_date, is_operational, issue_description))
        self.connection.commit()
        print("Запись о состоянии камеры добавлена")

    def delete_health_record(self, health_id):
        query = "DELETE FROM camera_health WHERE health_id = %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (health_id,))
        self.connection.commit()
        print("Запись о состоянии камеры удалена")
