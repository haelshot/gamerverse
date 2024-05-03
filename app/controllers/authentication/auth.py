from ninja import Router, Schema
from ninja.responses import Response
from ninja_jwt.authentication import JWTAuth

from app.models import User, Business, UserBusiness, Creator, UserCreator
from app.schemas import UserSchemaInput, BusinessSchemaIn

router = Router()


class UserRegisterResponse(Schema):
    is_success: bool
    message: str


@router.post("/signup", tags=["Authentication"], response=UserRegisterResponse)
def user_signup(request, payload: UserSchemaInput):
    try:
        if User.objects.filter(email=payload.email).exists():
            return Response(UserRegisterResponse(is_success=False, message="Email already exists."), status=409)

        user = User.objects.create_user(
            email=payload.email.lower().strip(),
            password=payload.password,
            role='user',
            first_name=payload.first_name,
            last_name=payload.last_name,
        )

        return Response(
            UserRegisterResponse(
                is_success=True,
                message='User registered successfully',
            )
        )
    except Exception as e:
        return Response(
            data={"error": {"name": "SIGNUP_ERROR", "details": f"An error occurred during signup, {e}"}},
            status=500
        )


@router.post("/signup/business", auth=JWTAuth(), tags=["Authentication"], response=UserRegisterResponse)
def business_signup(request, payload: BusinessSchemaIn):
    user = request.user
    if user:
        business = Business.objects.create(
            name=payload.name
        )

        user_business = UserBusiness.objects.create(
            user=user,
            business=business
        )

        return Response(
            UserRegisterResponse(
                is_success=True,
                message='Success.'
            )
        )

    return Response(
        UserRegisterResponse(
            is_success=False,
            message='User does not exist.'
        )
    )


@router.post("/signup/creator", auth=JWTAuth(), tags=["Authentication"], response=UserRegisterResponse)
def creator_signup(request, payload: BusinessSchemaIn):
    user = request.user
    if user:
        creator = Creator.objects.create(
            name=payload.name
        )

        creator_user = UserCreator.objects.create(
            user=user,
            business=creator
        )

        return Response(
            UserRegisterResponse(
                is_success=True,
                message='Success.'
            )
        )

    return Response(
        UserRegisterResponse(
            is_success=False,
            message='User does not exist.'
        )
    )