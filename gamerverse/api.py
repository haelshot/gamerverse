from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

from app.api import router as app_router

from app.controllers.news.news import router as news_router
from app.controllers.authentication.auth import router as auth_router
from app.controllers.authentication.signin import router as signin_router
from app.controllers.wager.wager import router as wager_router
from app.controllers.sellers.sellers import router as sellers_router
from app.controllers.streaming.streaming import router as streaming_router
from app.controllers.tournaments.tournament import router as tournament_router

api = NinjaExtraAPI()

api.add_router("/v1/", app_router)
api.add_router("/v1/", news_router)
api.add_router("/v1/", auth_router)
api.add_router("/v1/", signin_router)
api.add_router("/v1/", wager_router)
api.add_router("/v1/", sellers_router)
api.add_router("/v1/", streaming_router)
api.add_router("/v1/", tournament_router)

api.register_controllers(NinjaJWTDefaultController)
