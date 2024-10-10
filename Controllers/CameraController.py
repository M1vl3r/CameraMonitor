from Connection.db_config import create_connection
from Models.Camera import Camera

class CameraController:
    def __init__(self):
        self.connection = create_connection()

    def get_all_cameras(self):
        query = "SELECT * FROM cameras"
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cameras = [Camera(*result) for result in results]
        return cameras

    def add_camera(self, name, installation_date, status, location):
        query = "INSERT INTO cameras (camera_name, installation_date, status, location) VALUES (%s, %s, %s, %s)"
        cursor = self.connection.cursor()
        cursor.execute(query, (name, installation_date, status, location))
        self.connection.commit()
        print("Камера добавлена")

    def update_camera(self, camera_id, name=None, status=None, location=None):
        query = "UPDATE cameras SET "
        params = []
        if name:
            query += "camera_name = %s, "
            params.append(name)
        if status:
            query += "status = %s, "
            params.append(status)
        if location:
            query += "location = %s, "
            params.append(location)
        query = query.rstrip(', ') + " WHERE camera_id = %s"
        params.append(camera_id)

        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        print("Информация о камере обновлена")

    def delete_camera(self, camera_id):
        query = "DELETE FROM cameras WHERE camera_id = %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (camera_id,))
        self.connection.commit()
        print("Камера удалена")
