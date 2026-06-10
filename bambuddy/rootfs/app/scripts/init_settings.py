import os
import sqlite3
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("init_settings")

DB_PATH = "/share/bambuddy/data/bambuddy.db"

def upsert_setting(cursor, key, value):
    """Insert or update a single setting. Skips None/empty values."""
    if not value:
        return

    cursor.execute("SELECT id FROM settings WHERE key = ?", (key,))
    row = cursor.fetchone()

    if row:
        # Don't overwrite MQTT settings if they already exist in the database.
        # This ensures the user's manual UI overrides survive restarts.
        if key.startswith("mqtt_"):
            logger.info(f"Setting {key} already exists in database, skipping override from supervisor")
            return
        logger.info(f"Updating setting {key}")
        cursor.execute("UPDATE settings SET value = ?, updated_at = CURRENT_TIMESTAMP WHERE key = ?", (str(value), key))
    else:
        logger.info(f"Inserting setting {key}")
        cursor.execute("INSERT INTO settings (key, value, created_at, updated_at) VALUES (?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)", (key, str(value)))

def main():
    if not os.path.exists(DB_PATH):
        logger.info("Database not found, skipping settings initialization")
        return

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS settings (
                id INTEGER PRIMARY KEY,
                key TEXT UNIQUE,
                value TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Only sync env vars that are actually set (non-empty).
        # This preserves any values the user configured in the Bambuddy web UI
        # when the corresponding add-on config field was left blank.
        settings_to_sync = {
            "mqtt_enabled": os.environ.get("MQTT_ENABLED"),
            "mqtt_broker": os.environ.get("MQTT_BROKER"),
            "mqtt_port": os.environ.get("MQTT_PORT"),
            "mqtt_username": os.environ.get("MQTT_USERNAME"),
            "mqtt_password": os.environ.get("MQTT_PASSWORD"),
            "mqtt_topic_prefix": os.environ.get("MQTT_TOPIC_PREFIX"),
            "mqtt_use_tls": os.environ.get("MQTT_USE_TLS"),
            "obico_ml_url": os.environ.get("OBICO_ML_URL"),
        }

        for key, value in settings_to_sync.items():
            upsert_setting(cursor, key, value)

        conn.commit()
        conn.close()
        logger.info("Settings synchronized successfully")
    except Exception as e:
        logger.error(f"Failed to synchronize settings: {e}")

if __name__ == "__main__":
    main()
