import random
import string
import os
import sys

ENV_FILE = ".env"

def generate_password(length=16):
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    if len(sys.argv) < 2:
        print("Использование: python script.py <app_image>")
        return

    app_image = sys.argv[1]  # первый аргумент командной строки после имени скрипта[web:31][web:34][web:41]

    if os.path.exists(ENV_FILE):
        print(f"Файл {ENV_FILE} уже существует, генерация пропущена. Замена image")
        with open(ENV_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            new_lines = []
            for line in lines:
                if "APP_IMAGE" not in line.strip():
                    new_lines.append(line)
        with open(ENV_FILE, "a", encoding="utf-8") as f:
            f.writelines(new_lines)
            f.write(f"\nAPP_IMAGE={app_image}")
        #return

    port = random.choice(range(8000, 8010))
    password = generate_password()

    env_content = f"""APP_PORT={port}
DB_USER=note-user
DB_PORT=5432
DB_PASSWORD={password}
DB_HOST=db
DB_NAME=notes
APP_IMAGE={app_image}
"""

    with open(ENV_FILE, "w", encoding="utf-8") as f:
        f.write(env_content)

    print(f"Файл {ENV_FILE} успешно создан.")

if __name__ == "__main__":
    main()