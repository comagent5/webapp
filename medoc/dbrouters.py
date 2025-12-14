"""
DATABASE ROUTERS.
Перенаправлення запитів додатка medoc до БД PostgreSQL.
Всі інші додатки до sqlite3
"""

class MedocDBRouter:
    """
    Перенаправлення запитів додатка medoc до БД PostgreSQL.
    Всі інші додатки до sqlite3
    """

    route_db_map = {
        'medoc_app': 'postgresql',
    }

    # База данных по умолчанию для всех остальных приложений
    default_db = 'default'  # sqlite3

    def db_for_read(self, model, **hints):
        """Визначає БД для операції читання."""

        # Перевірка:, чи є додаток у списку для postgresql
        return self.route_db_map.get(model._meta.app_label, self.default_db)

    def db_for_write(self, model, **hints):
        """Визначає БД для операції запису."""

        # Перевірка:, чи є додаток у списку для postgresql
        return self.route_db_map.get(model._meta.app_label, self.default_db)

    def allow_relation(self, obj1, obj2, **hints):
        """Разрешает ли отношение между двумя объектами."""

        # Получаем БД, к которым привязаны модели
        db_1 = self.db_for_read(obj1)
        db_2 = self.db_for_read(obj2)

        # Дозволяємо відношення, якщо обидві моделі знаходяться в одній БД.
        if db_1 and db_2 and db_1 == db_2:
            return True

        # Не дозволяємо якщо обидві моделі знаходяться в різних БД, для запобігання помилок цілістності
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Визначає, чи може міграція бути використана для цієї БД."""

        target_db = self.route_db_map.get(app_label)

        # Якщо додаток прив'язан PostgreSQL ('postgresql'):
        if target_db == 'postgresql':
            # Дозволяємо міграції тільки на 'postgresql'
            return db == 'postgresql'

        # Для всіх інших дозволяємо тільки на 'default' (SQlite3)
        return db == self.default_db