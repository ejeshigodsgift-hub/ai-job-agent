import shutil
from datetime import datetime


def backup_database():
    timestamp = datetime.now().strftime('%Y%m%d')

    shutil.copy(
        'database/schema.sql',
        f'storage/backups/db_{timestamp}.sql'
    )