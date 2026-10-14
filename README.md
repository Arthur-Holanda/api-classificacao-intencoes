# API do Intent Classifier

Como rodar?

```
conda create --name intent_clf python=3.11
conda activate intent_clf
pip install -r requirements.txt
uvicorn src.app:app --port 8000
```

Assegure que as suas variáveis de ambiente estão corretamente descritas em um arquivo privado `.env` na raiz do projeto.