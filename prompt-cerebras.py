from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from langchain import PromptTemplate
from langchain import LLMChain
import sys

# Model creation (adjust depending on your RAM memory)
#model_name = "cerebras/Cerebras-GPT-13B"
#model_name = "cerebras/Cerebras-GPT-6.7B"
#model_name = "cerebras/Cerebras-GPT-2.7B"
model_name = "cerebras/Cerebras-GPT-111M"

model = AutoModelForCausalLM.from_pretrained(model_name)

# LangChain tokenizer, pipeline and HuggingFace Model
tokenizer = AutoTokenizer.from_pretrained(model_name)
pipe = pipeline(
    "text-generation", model=model, tokenizer=tokenizer,
    max_new_tokens=100, early_stopping=True, no_repeat_ngram_size=2
)
llm = HuggingFacePipeline(pipeline=pipe)

# Prompt generation
template = """
{input}
"""

prompt = PromptTemplate(
    input_variables=["input"],
    template=template,
)

chain = LLMChain(
    llm=llm,
    verbose=True,
    prompt=prompt
)

# Prompt execution from Command Line Arguments
commandstring = '';  
for arg in sys.argv[1:]:
    if ' ' in arg:
        commandstring+= '"{}"  '.format(arg) ;
    else:
        commandstring+="{}  ".format(arg) ; 

response = chain.run(commandstring)
print(response)
