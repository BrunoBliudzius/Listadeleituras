from fastapi import FastAPI
from api.routes.post import router as post_router
from api.routes.get import router as get_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post_router, prefix="/obras", tags=["Obras"])
app.include_router(get_router, prefix="/obras", tags=["Obras"])
