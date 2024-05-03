from ninja import Router
from rest_framework.request import Request

from app.models import User

from gamerverse import settings

router = Router()

base_url = settings.BASE_URL
api_url = settings.API_URL


@router.get("/status/")
def check_db(request: Request):
    try:
        # Query the User model to count the records
        count = User.objects.all().count()
        response_data = {"status": "ok1"}
    except Exception as e:
        # If there was an error, return "ok2"
        response_data = {"status": "ok2"}

    return response_data
