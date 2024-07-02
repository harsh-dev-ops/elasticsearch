from elasticsearch_dsl import async_connections

from app.conf.settings import settings

async_connections.create_connection(alias="default", hosts=settings.ELASTIC_HOSTS, timeout=30)

