up:
	docker-compose up

celery:
	celery worker -A btre --loglevel=debug --concurrency=4
