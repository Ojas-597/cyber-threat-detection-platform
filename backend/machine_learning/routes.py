from fastapi import APIRouter, Depends
from backend.authentication.dependencies import get_current_user
from backend.machine_learning.service import predict_threat

router = APIRouter(
    prefix="/ml",
    tags=["Machine Learning"]
)

@router.post("/predict")
def predict(
    data: dict,
    current_user=Depends(get_current_user)
):
    return {
        "prediction":
        predict_threat(data["score"])
    }