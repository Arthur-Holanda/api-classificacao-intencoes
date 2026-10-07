from fastapi import FastAPI
from dotenv import load_dotenv

from model import Dados, Predicao

from shared.database.engine import banco


load_dotenv()
WANDB_MODEL_CLASSIFIER = os.getenv("WANDB_MODEL_CLASSIFIER")

classifier = IntentClassifier(
    config="models/confusion_config.yml", 
    load_model=WANDB_MODEL_CLASSIFIER
)


intent_classifier_router = FastAPI()

@intent_classifier_router.post('/predicao')
def predicao(dados: Dados):
    _, probs = classifier.predict(dados)
    dados.predicao = probs
    banco.insert(dados)
    return dados

