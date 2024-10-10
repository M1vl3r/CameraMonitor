from Connection.db_config import create_connection
from Models.Notification import Notification

class NotificationController:
    def __init__(self):
        self.connection = create_connection()

    def get_notifications(self):
        query = "SELECT * FROM notifications"
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        notifications = [Notification(*result) for result in results]
        return notifications

    def add_notification(self, camera_id, notification_type, notification_message, notification_date):
        query = "INSERT INTO notifications (camera_id, notification_type, notification_message, notification_date) VALUES (%s, %s, %s, %s)"
        cursor = self.connection.cursor()
        cursor.execute(query, (camera_id, notification_type, notification_message, notification_date))
        self.connection.commit()
        print("Уведомление добавлено")

    def delete_notification(self, notification_id):
        query = "DELETE FROM notifications WHERE notification_id = %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (notification_id,))
        self.connection.commit()
        print("Уведомление удалено")
