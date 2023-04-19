# cerebrasgpt-test
Testing the new released LLM Models from CerebrasGPT

Clone the repo:

`git clone https://github.com/jacar-javi/cerebrasgpt-test.git`

To test prompting CerebrasGPT run:

```bash
pip install -r requirements.txt
python prompt-cerebras.py "Where was he standing?"
```

Notes:
- Testing is done by default with cerebras/Cerebras-GPT-111M model, you can edit the code and use a bigger model for better results, causing a large amount of memory consumption.
- First time you execute this application it will download the selected trained model.