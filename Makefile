install:
	python3 -m venv env &&\
		. env/bin/activate &&\
		pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt &&\
		pip3 install -e .

clean:
	rm -rf env
	rm -rf nucli.egg-info

test:
	pytest tests/test_*

lint:
	flake8 app tests
