@echo off
.\venv\Scripts\activate && waitress-serve --listen=*:8000 --threads=10 --channel-timeout=1800 Kensa.wsgi:application
