install:
	pip install -r requirements.txt
test:
	python3 -m unittest discover -v
run:
	python3 main.py