from ninja import Router

router = Router()


@router.get("/hello")
def hello_world(request):
    return {"message": "Hello, GamerVerse360!"}
