from celery import shared_task
import logging
logger = logging.getLogger(__name__)

@shared_task
def retrieve_github_eo_data(organization, secret, repositories):
    logger.info (f" Retrieve EO Data")
    logger.info (f"{organization} - {secret} - {repositories}")

@shared_task
def retrieve_github_cmpo_data(organization, secret, repositories):
    logger.info (f" Retrieve CMPO Data")
    logger.info (f"{organization} - {secret} - {repositories}")

@shared_task
def retrieve_github_ciro_data(organization, secret, repositories):
    logger.info (f" Retrieve CIRO Data")
    logger.info (f"{organization} - {secret} - {repositories}")