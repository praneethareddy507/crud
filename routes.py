from fastapi import APIRouter, status
from schemas import Response,Student

import services
router = APIRouter(
    prefix="/student",
    tags=["STUDENT"]
)

# @router.get("/" ,response_model=Response,

#     status_code=status.HTTP_200_OK)
# def getresponse():
#     return services.createstudent()

# @router.post("/",response_model=Response, status_code=status.HTTP_200_OK)
# def create():
#     return services.createstudent()

@router.get(
    "/",
    response_model=list[Response],
    status_code=status.HTTP_200_OK
)
def getresponse():
    return services.getstudents()


@router.post(
    "/",
    response_model=Response,
    status_code=status.HTTP_201_CREATED
)
def create(student:Student):
   
    return services.createstudent(student)
@router.put(
    "/{student_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK
)
def update(student_id: str,student: Student):
    return services.updatestudent(student_id,student)


@router.delete(
    "/{student_id}",
    status_code=status.HTTP_200_OK
)
def delete(student_id: str):
    return services.deletestudent(student_id)