make debug:
	python server.py

clean:
	rm *.pyc
	rm database/*.pyc

restart:
	python database/database_create.py
	sudo systemctl restart cuas

monitor:
	tail -f cuas-server.log | less

test tests:
	python -m pytest tests/

