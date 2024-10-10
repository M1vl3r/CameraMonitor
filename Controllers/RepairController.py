from Connection.db_config import create_connection
from Models.CameraRepair import CameraRepair

class RepairController:
    def __init__(self):
        self.connection = create_connection()

    def get_repairs(self):
        query = "SELECT * FROM camera_repairs"
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        repairs = [CameraRepair(*result) for result in results]
        return repairs

    def add_repair(self, camera_id, repair_start, repair_end, repair_description, replaced_parts):
        query = "INSERT INTO camera_repairs (camera_id, repair_start, repair_end, repair_description, replaced_parts) VALUES (%s, %s, %s, %s, %s)"
        cursor = self.connection.cursor()
        cursor.execute(query, (camera_id, repair_start, repair_end, repair_description, replaced_parts))
        self.connection.commit()
        print("Запись о ремонте добавлена")

    def delete_repair(self, repair_id):
        query = "DELETE FROM camera_repairs WHERE repair_id = %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (repair_id,))
        self.connection.commit()
        print("Запись о ремонте удалена")
