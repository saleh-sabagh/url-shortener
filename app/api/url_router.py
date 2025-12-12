"""API routes for URL shortener operations."""

from typing import Dict, Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.repositories.url_repository import URLRepository
from app.schemas.url_schema import URLCreate, URLOut, ResponseModel
from app.services.url_service import URLService

router = APIRouter(tags=["urls"])


@router.post("/urls", response_model=ResponseModel, status_code=201)
def create_url(payload: URLCreate, db: Session = Depends(get_db)) -> Dict[str, Any]:
    """Create a new shortened URL.

    Args:
        payload: URL creation request payload.
        db: Database session dependency.

    Returns:
        Response containing the created shortened URL.

    Raises:
        HTTPException: If URL validation fails (400) or internal error occurs (500).
    """
    repo = URLRepository(db)
    service = URLService(repo)
    try:
        url_obj = service.create_short_url(str(payload.original_url))
        return {
            "status": "success",
            "data": {"url": URLOut.model_validate(url_obj).model_dump()},
        }
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail={"status": "failure", "message": str(e)},
        )
    except RuntimeError as e:
        raise HTTPException(
            status_code=500,
            detail={"status": "failure", "message": str(e)},
        )
    except Exception:
        raise HTTPException(
            status_code=500,
            detail={"status": "failure", "message": "Internal error"},
        )


@router.get("/u/{code}", status_code=302)
def redirect_to_original(code: str, db: Session = Depends(get_db)) -> RedirectResponse:
    """Redirect to the original URL using the short code.

    Args:
        code: The short code of the URL.
        db: Database session dependency.

    Returns:
        RedirectResponse to the original URL.

    Raises:
        HTTPException: If short code not found (404).
    """
    repo = URLRepository(db)
    url_obj = repo.get_by_short_code(code)
    if not url_obj:
        raise HTTPException(
            status_code=404,
            detail={"status": "failure", "message": "URL not found"},
        )
    return RedirectResponse(url_obj.original_url, status_code=302)


@router.get("/urls", response_model=ResponseModel)
def get_all_urls(db: Session = Depends(get_db)) -> Dict[str, Any]:
    """Retrieve all shortened URLs.

    Args:
        db: Database session dependency.

    Returns:
        Response containing list of all shortened URLs.
    """
    repo = URLRepository(db)
    data = repo.get_all()

    return {
        "status": "success",
        "data": {"urls": [URLOut.model_validate(x).model_dump() for x in data]},
    }

@router.delete("/urls/{code}", response_model=ResponseModel)
def delete_url(code: str, db: Session = Depends(get_db)) -> Dict[str, Any]:
    """Delete a shortened URL by short code.

    Args:
        code: The short code of the URL to delete.
        db: Database session dependency.

    Returns:
        Response confirming deletion.

    Raises:
        HTTPException: If short code not found (404).
    """
    repo = URLRepository(db)
    obj = repo.delete_by_short_code(code)
    if not obj:
        raise HTTPException(
            status_code=404,
            detail={"status": "failure", "message": "URL not found"},
        )
    return {"status": "success", "message": "URL deleted successfully"}
