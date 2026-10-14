from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv

load_dotenv()

from src.modules.intent_classifier.model import Mensagem, ResultadoModelo, PredicaoMensagem
from src.modules.intent_classifier import service

from src.shared.database.engine import prediction_collection

router = APIRouter()

@router.post('/predictions')
def post_predictions(msg: Mensagem):
    outputs = service.predict_all(msg.text)
    prediction_collection.insert_one(outputs)
    outputs.pop('_id', None)
    outputs['message'] = msg.__dict__
    return outputs

@router.get('/predictions')
def get_predictions():
    res = prediction_collection.find({})
    for i in res:
        i.pop('_id', None)
    return res
