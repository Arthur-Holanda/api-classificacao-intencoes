from src.modules.intent_classifier.intent_classifier import IntentClassifier
import os

WANDB_MODELS = os.environ.get('WANDB_MODELS')
WANDB_PROJECT = os.environ.get('WANDB_PROJECT')


_models = {}

def load_models():
    url_models = [url.strip() for url in WANDB_MODELS.split(',')]
    if not url_models:
        raise RunTimeError('Sem modelos em WANDB_MODELS.')

    for url in url_models:
        model_name = url.split('/')[-1].split(':')[0]
        _models[model_name] = IntentClassifier(load_model=url, 
                                               wandb_project=WANDB_PROJECT)
    return


def clear_models():
    _models.clear()


def predict_all(text: str):
    outputs = {}

    for model_name, clf in _models.items():
        intent, probs = clf.predict(text)

        outputs[model_name] = {'intent': intent, 'probs': probs}
    
    return outputs