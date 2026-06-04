from app.workers.celery_app import celery_app
@celery_app.task
def ping_market_task(): return 'market worker ok'
