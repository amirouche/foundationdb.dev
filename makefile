all:
	./venv python3 foundationdb.dev.py
	python3 -m http.server
