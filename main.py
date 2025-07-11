from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from scraper import scrape_products
from models import init_db, insert_products, get_products
from utils import save_to_json, save_to_csv

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
def startup():
    init_db()

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    products = get_products()
    return templates.TemplateResponse("index.html", {"request": request, "products": products})

@app.get("/scrape")
def run_scraper():
    products = scrape_products()
    insert_products(products)
    save_to_json(products)
    save_to_csv(products)
    return {"message": "Dados extraídos com sucesso", "total": len(products)}

@app.get("/scrape-html", response_class=HTMLResponse)
def run_scraper_html(request: Request):
    products = scrape_products()
    insert_products(products)
    save_to_json(products)
    save_to_csv(products)
    return templates.TemplateResponse("index.html", {"request": request, "products": products})

@app.get("/products")
def list_products():
    return get_products()
