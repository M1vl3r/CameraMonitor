from Connection.db_config import create_connection
from Models.CameraSetting import CameraSetting

class SettingsController:
    def __init__(self):
        self.connection = create_connection()

    def get_settings(self):
        query = "SELECT * FROM camera_settings"
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        settings = [CameraSetting(*result) for result in results]
        return settings

    def add_setting(self, camera_id, setting_name, setting_value):
        query = "INSERT INTO camera_settings (camera_id, setting_name, setting_value) VALUES (%s, %s, %s)"
        cursor = self.connection.cursor()
        cursor.execute(query, (camera_id, setting_name, setting_value))
        self.connection.commit()
        print("Настройка камеры добавлена")

    def delete_setting(self, setting_id):
        query = "DELETE FROM camera_settings WHERE setting_id = %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (setting_id,))
        self.connection.commit()
        print("Настройка камеры удалена")
