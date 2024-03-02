from fastapi import FastAPI

from server.routes.products import router_products
from server.routes.tasks import router_tasks


app = FastAPI()


app.include_router(router_tasks)
app.include_router(router_products)
