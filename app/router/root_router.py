from fastapi import APIRouter
from router.employee_router import router as employee_router
from router.departments_router import router as departments_router
from router.attendance_router import router as attendance_router
from router.projects_router import router as projects_router
from router.role_router import router as role_router

def rootRouter():
    api_router = APIRouter(prefix="/api")
    api_router.include_router(employee_router)
    # Include other routers here as needed
    api_router.include_router(departments_router)
    api_router.include_router(attendance_router)
    api_router.include_router(projects_router)
    api_router.include_router(role_router)
    return api_router

