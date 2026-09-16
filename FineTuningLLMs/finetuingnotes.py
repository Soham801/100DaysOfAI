'''
                 Llama 3.2
                     │
                     ▼
              Training Dataset
                     │
                     ▼
               Loss Calculation
                     │
                     ▼
              Gradient Updates
                     │
                     ▼
             Modified Parameters
                     │
                     ▼
             Fine-tuned Model
'''

## After lesson1.py

'''
Python
  │
  ▼
Ollama API
  │
  ▼
Llama 3.2
  │
  ├── System instruction
  │
  └── User instruction
  │
  ▼
Generated response

'''


"""
              Same Base Model
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
      llama3.2              python-tutor
                               │
                        System instructions
                               │
                               ▼
                       Different behavior

"""

"""
What is the difference between prompting and fine-tuning?

Prompting changes the input/instructions given to a model, whereas fine-tuning trains the model's parameters using a dataset.


"""


"""

                  LLM DEVELOPMENT
                        │
                        ▼
                 ┌─────────────┐
                 │   Ollama    │ ← here
                 └──────┬──────┘
                        │
                        ▼
                 ┌─────────────┐
                 │ Llama 3.2   │
                 └──────┬──────┘
                        │
                        ▼
                 ┌─────────────┐
                 │ Prompting   │
                 └──────┬──────┘
                        │
                        ▼
                 ┌─────────────┐
                 │ Python API  │
                 └─────────────┘

        Later :

                 Hugging Face
                      ↓
                 Transformers
                      ↓
                    PyTorch
                      ↓
                Dataset
                      ↓
                  Training
                      ↓
                 PEFT / LoRA
                      ↓
                  QLoRA
                      ↓
               Fine-tuned LLM
                      ↓
                    GGUF
                      ↓
                   Ollama


"""


"""

                 USER TEXT
                    │
                    ▼
               TOKENIZER
                    │
                    ▼
               TOKEN IDs
                    │
                    ▼
               EMBEDDINGS
                    │
                    ▼
          ┌───────────────────┐
          │    TRANSFORMER    │
          │                   │
          │ Self-Attention    │
          │       ↓           │
          │ Feed Forward      │
          │       ↓           │
          │ Normalization     │
          │       ↓           │
          │ Repeated Layers   │
          └─────────┬─────────┘
                    │
                    ▼
                  LOGITS
                    │
                    ▼
             PROBABILITY
               DISTRIBUTION
                    │
                    ▼
             NEXT TOKEN
                    │
                    ▼
             Repeat process


"""

"""

PROBLEM
   ↓
REQUIREMENTS
   ↓
SYSTEM DESIGN
   ↓
TECHNOLOGY SELECTION
   ↓
PROJECT STRUCTURE
   ↓
IMPLEMENTATION
   ↓
TESTING
   ↓
INTEGRATION
   ↓
DEPLOYMENT
   ↓
MONITORING / ITERATION

"""