from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from app.schemas.url_schema import URLCreate, URLOut, ResponseModel
from app.core.deps import get_db
from app.repositories.url_repository import URLRepository
from app.services.url_service import URLService

router = APIRouter(tags=["urls"])

@router.post("/urls", response_model=ResponseModel, status_code=201)
def create_url(payload: URLCreate, db=Depends(get_db)):
    repo = URLRepository(db)
    service = URLService(repo)
    try:
        url_obj = service.create_short_url(str(payload.original_url))
        return {"status": "success", "data": {"url": URLOut.from_orm(url_obj).dict()}}
    except ValueError as e:
        raise HTTPException(status_code=400, detail={"status":"failure","message":str(e)})
    except Exception as e:
        raise HTTPException(status_code=500, detail={"status":"failure","message":"Internal error"})

@router.get("/u/{code}")
def redirect_to_original(code: str, db=Depends(get_db)):
    repo = URLRepository(db)
    url_obj = repo.get_by_short_code(code)
    if not url_obj:
        raise HTTPException(status_code=404, detail={"status":"failure","message":"URL not found"})
    return RedirectResponse(url_obj.original_url, status_code=302)
