# 🎸 Dashboard - The Band

> 🧠 *"The idea is that each ontology-based service in the architecture is like a musician that plays an instrument (representing ontology concepts, relations, and rules). Together, these services create music (information) from musical notes (application data) to satisfy a public (the organization)."*

**Dashboard - The Band** is the orchestrator of a semantic, modular, and intelligent service architecture. Each service acts like a band member, transforming structured and unstructured data into meaningful insights — like musicians creating harmony from notes.

---

## 🚀 Tech Stack

- [Python 3.10](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Gunicorn](https://gunicorn.org/)
- [Docker & Docker Compose](https://docs.docker.com/)
- PostgreSQL (via Docker)

---

## 📦 Project Structure

```

src/
├── dashboard/          # Django settings and core
├── apps/               # Business apps
├── features/           # Functional modules
├── static/             # Static files
├── staticfiles/        # Collected by collectstatic
├── manage.py
├── requirements.txt

````

---

## ⚙️ Running with Docker

### 1. Create the environment file

```bash
cp .env.example .env
````

### 2. Build and start the app

```bash
docker compose up --build
```

The app will be available at: [http://localhost:8000](http://localhost:8000)

---

## 👤 Creating a superuser

You can create a Django superuser with:

```bash
./create_superuser.sh
```

> This runs the `create_superuser.py` script inside the Docker container.

---

## 🐍 Running Django commands

Access the container and run:

```bash
docker exec -it dashboard_the_band bash
python manage.py migrate
python manage.py createsuperuser
```

---

## 🧪 Running tests

```bash
docker exec -it dashboard_the_band python manage.py test
```

---

## 🛠️ Scripts and utilities

* `create_superuser.py`: Creates the superuser if it doesn't exist.
* `create_superuser.sh`: Executes the script inside the container.
* `Makefile` (coming soon): Build, dev, test, and deploy commands.

---

## 📁 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## ✨ Author

Made with 💙 by The Band Dev Team.

