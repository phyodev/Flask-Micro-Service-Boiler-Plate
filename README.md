# Flask Microservice Boiler Plate
.
├── app.py                # Flask app + endpoints
├── wsgi.py               # Gunicorn entry
├── wsgi_conf.py      # Gunicorn config

├── config.py             # App configuration (env)
├── db.py                 # SQLAlchemy engine & session
├── models.py             # DB models (SQLAlchemy + optional SQLModel)
├── repository.py         # DB access layer (CRUD, bulk)
├── services.py           # Business logic

├── log_handler.py        # Concurrent-safe logging
├── utils.py              # Helpers placeholder

├── alembic/              # Alembic migrations folder
│   └── env.py
│   └── versions/
├── requirements.txt
├── .env.example
├── README.md
└── logs/

https://chatgpt.com/c/69777b36-9ee8-8322-961b-ee3133052e3a


## Tech stacks
- Python
- Flask
- Alembic
- SQLAlchemy
- poetry (for package manager)

## Features (predefined)
- DB Operation [CRUD, bulk opt, ORM, SQL]
- Routes
- Service Layer