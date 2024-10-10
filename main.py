from Controllers.CameraController import CameraController
from Controllers.HealthController import HealthController
from Controllers.RepairController import RepairController
from Controllers.SettingsController import SettingsController
from Controllers.NotificationController import NotificationController


def main():
    camera_controller = CameraController()
    health_controller = HealthController()
    repair_controller = RepairController()
    settings_controller = SettingsController()
    notification_controller = NotificationController()

    while True:
        print("\n𝘾𝙖𝙢𝙚𝙧𝙖𝙈𝙤𝙣𝙞𝙩𝙤𝙧𝙑1.1")
        print("[1] Просмотр всех камер")
        print("[2] Добавить камеру")
        print("[3] Изменить камеру")
        print("[4] Удалить камеру")
        print("[5] Управление состоянием камер")
        print("[6] Управление ремонтами камер")
        print("[7] Управление настройками камер")
        print("[8] Управление уведомлениями")
        print("[9] Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            cameras = camera_controller.get_all_cameras()
            for camera in cameras:
                print(
                    f"ID: {camera.camera_id}, Название: {camera.camera_name}, Статус: {camera.status}, Местоположение: {camera.location}")

        elif choice == '2':
            name = input("Введите название камеры: ")
            installation_date = input("Введите дату установки (YYYY-MM-DD): ")
            status = input("Введите статус камеры (working/not_working/repairing): ")
            location = input("Введите местоположение: ")
            camera_controller.add_camera(name, installation_date, status, location)

        elif choice == '3':
            camera_id = input("Введите ID камеры для изменения: ")
            name = input("Введите новое название камеры (оставьте пустым для пропуска): ")
            status = input("Введите новый статус камеры (оставьте пустым для пропуска): ")
            location = input("Введите новое местоположение (оставьте пустым для пропуска): ")
            camera_controller.update_camera(camera_id, name, status, location)

        elif choice == '4':
            camera_id = input("Введите ID камеры для удаления: ")
            camera_controller.delete_camera(camera_id)

        # Работа с состоянием камеры
        elif choice == '5':
            print("\nУправление состоянием камер:")
            print("[1] Просмотр состояния камер")
            print("[2] Добавить запись о состоянии камеры")
            print("[3] Удалить запись о состоянии камеры")
            sub_choice = input("Выберите действие: ")

            if sub_choice == '1':
                health_records = health_controller.get_camera_health()
                for record in health_records:
                    print(
                        f"ID: {record.health_id}, Камера ID: {record.camera_id}, Дата проверки: {record.check_date}, Работает: {record.is_operational}, Описание: {record.issue_description}")

            elif sub_choice == '2':
                camera_id = input("Введите ID камеры: ")
                check_date = input("Введите дату проверки (YYYY-MM-DD HH:MM:SS): ")
                is_operational = input("Камера работает? (1 - Да, 0 - Нет): ")
                issue_description = input("Введите описание проблемы (если есть): ")
                health_controller.add_health_record(camera_id, check_date, is_operational, issue_description)

            elif sub_choice == '3':
                health_id = input("Введите ID записи о состоянии камеры для удаления: ")
                health_controller.delete_health_record(health_id)

        # Работа с ремонтами камер
        elif choice == '6':
            print("\nУправление ремонтами камер:")
            print("[1] Просмотр записей о ремонтах")
            print("[2] Добавить запись о ремонте камеры")
            print("[3] Удалить запись о ремонте камеры")
            sub_choice = input("Выберите действие: ")

            if sub_choice == '1':
                repairs = repair_controller.get_repairs()
                for repair in repairs:
                    print(
                        f"ID: {repair.repair_id}, Камера ID: {repair.camera_id}, Начало ремонта: {repair.repair_start}, Окончание ремонта: {repair.repair_end}, Описание: {repair.repair_description}, Заменённые части: {repair.replaced_parts}")

            elif sub_choice == '2':
                camera_id = input("Введите ID камеры: ")
                repair_start = input("Введите дату начала ремонта (YYYY-MM-DD HH:MM:SS): ")
                repair_end = input("Введите дату окончания ремонта (оставьте пустым, если ремонт не завершён): ")
                repair_description = input("Введите описание ремонта: ")
                replaced_parts = input("Введите заменённые части (если есть): ")
                repair_controller.add_repair(camera_id, repair_start, repair_end, repair_description, replaced_parts)

            elif sub_choice == '3':
                repair_id = input("Введите ID записи о ремонте для удаления: ")
                repair_controller.delete_repair(repair_id)

        # Работа с настройками камер
        elif choice == '7':
            print("\nУправление настройками камер:")
            print("[1] Просмотр настроек камер")
            print("[2] Добавить настройку камеры")
            print("[3] Удалить настройку камеры")
            sub_choice = input("Выберите действие: ")

            if sub_choice == '1':
                settings = settings_controller.get_settings()
                for setting in settings:
                    print(
                        f"ID: {setting.setting_id}, Камера ID: {setting.camera_id}, Настройка: {setting.setting_name}, Значение: {setting.setting_value}")

            elif sub_choice == '2':
                camera_id = input("Введите ID камеры: ")
                setting_name = input("Введите название настройки: ")
                setting_value = input("Введите значение настройки: ")
                settings_controller.add_setting(camera_id, setting_name, setting_value)

            elif sub_choice == '3':
                setting_id = input("Введите ID настройки для удаления: ")
                settings_controller.delete_setting(setting_id)

        # Работа с уведомлениями камер
        elif choice == '8':
            print("\nУправление уведомлениями камер:")
            print("[1] Просмотр уведомлений")
            print("[2] Добавить уведомление")
            print("[3] Удалить уведомление")
            sub_choice = input("Выберите действие: ")

            if sub_choice == '1':
                notifications = notification_controller.get_notifications()
                for notification in notifications:
                    print(
                        f"ID: {notification.notification_id}, Камера ID: {notification.camera_id}, Тип: {notification.notification_type}, Сообщение: {notification.notification_message}, Дата: {notification.notification_date}")

            elif sub_choice == '2':
                camera_id = input("Введите ID камеры: ")
                notification_type = input("Введите тип уведомления (error/repair/maintenance): ")
                notification_message = input("Введите сообщение уведомления: ")
                notification_date = input("Введите дату уведомления (YYYY-MM-DD HH:MM:SS): ")
                notification_controller.add_notification(camera_id, notification_type, notification_message,
                                                         notification_date)

            elif sub_choice == '3':
                notification_id = input("Введите ID уведомления для удаления: ")
                notification_controller.delete_notification(notification_id)

        elif choice == '9':
            break


if __name__ == "__main__":
    main()
