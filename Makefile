up:
	docker-compose up

celery:
	celery worker -A btre --loglevel=info --concurrency=4
