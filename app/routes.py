from app.models import product_classifier
from app import app
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.responses import PlainTextResponse, RedirectResponse,JSONResponse



templates = Jinja2Templates(directory='app/templates')

@app.route('/',methods=['GET','POST'])
async def homepage(request):
    return templates.TemplateResponse('index.html', {'request': request})
    
    
@app.route('/predict',methods=['GET','POST'])
async def predict(request):
    result = product_classifier.predict('text')
    return JSONResponse({'result': result})
    