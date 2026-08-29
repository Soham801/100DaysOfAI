# 100 Days of AI

> **A structured 100-day journey through Artificial Intelligence, Machine Learning, Generative AI, LLMs, AI Agents, and modern AI engineering.**

This repository documents my **100 Days of AI challenge** — a hands-on learning journey focused on understanding AI concepts by **building, experimenting, implementing, and writing code**.

Rather than treating AI as a collection of theoretical concepts, this repository focuses on turning what I learn into working implementations, experiments, and small projects.

The goal is to build a strong foundation across the modern AI ecosystem while developing the practical skills required to design and build AI-powered applications.

---

## About the Challenge

**100 Days of AI** is a self-driven learning challenge where I consistently dedicate time to learning and implementing concepts related to Artificial Intelligence.

The repository serves as a **technical learning log and codebase** containing the implementations, experiments, notebooks, projects, and experiments developed throughout the journey.

### Core Objectives

* Build strong foundations in Artificial Intelligence and Machine Learning
* Understand how modern AI systems work internally
* Develop practical experience through implementation
* Learn Generative AI and Large Language Models
* Explore AI Agents and agentic workflows
* Work with modern AI frameworks and APIs
* Understand model interaction, prompting, evaluation, and orchestration
* Develop better software engineering practices for AI applications
* Build a portfolio demonstrating continuous technical growth

---

## Learning Roadmap

The learning journey is organized progressively, moving from fundamental concepts toward modern AI engineering.

```text
AI Fundamentals
      │
      ▼
Machine Learning
      │
      ▼
Deep Learning
      │
      ▼
Natural Language Processing
      │
      ▼
Generative AI
      │
      ▼
Large Language Models
      │
      ▼
Prompt Engineering
      │
      ▼
RAG & Vector Databases
      │
      ▼
AI Agents
      │
      ▼
Agentic Workflows
      │
      ▼
AI Application Engineering
```

The exact order may evolve as new concepts and technologies are explored.

---

## Repository Structure

The repository is organized around the learning journey rather than a single production application.

```text
100DaysOfAI/
│
├── Day01/
├── Day02/
├── Day03/
├── ...
├── Day100/
│
├── projects/
│   └── ...
│
├── experiments/
│   └── ...
│
├── notebooks/
│   └── ...
│
├── requirements.txt
└── README.md
```

> The directory structure may evolve as the challenge progresses.

Each day's directory contains the code and experiments associated with the concepts studied on that day.

---

## Topics Covered

The repository is intended to progressively cover areas such as:

### Artificial Intelligence

* AI fundamentals
* Intelligent systems
* Search and problem solving
* Knowledge representation
* Reasoning
* AI system design

### Machine Learning

* Supervised Learning
* Unsupervised Learning
* Classification
* Regression
* Clustering
* Feature Engineering
* Model Evaluation
* Probability & Statistics
* Optimization

### Deep Learning

* Neural Networks
* Forward & Backward Propagation
* Activation Functions
* Loss Functions
* Optimization
* CNNs
* RNNs
* Representation Learning

### Natural Language Processing

* Text preprocessing
* Tokenization
* Embeddings
* Text classification
* Semantic similarity
* Language models
* NLP pipelines

### Generative AI

* Generative models
* LLM fundamentals
* Prompt Engineering
* Structured prompting
* Context management
* Model evaluation
* AI application development

### LLM Engineering

* LLM APIs
* Model selection
* Prompt design
* Structured outputs
* Function/tool calling
* Context management
* Streaming
* Model orchestration

### Retrieval-Augmented Generation

* Embeddings
* Vector databases
* Similarity search
* Document processing
* Retrieval pipelines
* Context injection
* RAG architectures

### AI Agents

* Agent architecture
* Tools
* Tool calling
* Memory
* Planning
* Agent workflows
* Multi-step reasoning
* Agent orchestration
* Autonomous task execution

### AI Engineering

* AI application architecture
* API integration
* Environment management
* Dependency management
* Error handling
* Testing
* Git & GitHub workflows
* Modular application design

---

## Technology Stack

The technologies used throughout the challenge may change as different concepts are explored.

### Languages

* **Python**
* SQL
* JavaScript / TypeScript where required

### AI / ML

* NumPy
* Pandas
* Scikit-learn
* PyTorch
* TensorFlow / Keras

### Generative AI

* OpenAI APIs
* AWS Bedrock
* Hugging Face
* LLM-based frameworks and SDKs

### AI Engineering

* LangChain
* LangGraph
* Agent frameworks
* REST APIs
* FastAPI

### Data & Infrastructure

* Jupyter Notebook
* Git
* GitHub
* Virtual environments
* Cloud AI services
* Vector databases

> Technologies listed above represent the areas being explored during the learning journey and may not all be used in every part of the repository.

---

## Daily Progress

The challenge follows a simple principle:

> **Learn → Implement → Experiment → Document → Repeat**

Each day focuses on a specific concept, implementation, experiment, or project.

| Day     | Focus                            | Status    |
| ------- | -------------------------------- | --------- |
| Day 01  | AI Learning Setup & Fundamentals | Completed |
| Day 02  | —                                | Completed |
| Day 03  | —                                | Completed |
| ...     | ...                              | ...       |
| Day 100 | —                                | Planned   |

The progress table will be continuously updated as the challenge progresses.

---

## Projects & Experiments

Alongside daily implementations, the challenge includes larger experiments and projects that combine multiple concepts.

These projects are intended to move beyond isolated tutorials and demonstrate how individual AI concepts can be combined into practical systems.

Examples of areas explored include:

* AI-powered applications
* Prompt optimization
* LLM applications
* Retrieval systems
* AI agents
* Agentic workflows
* AI automation
* Model experimentation

---

## Engineering Principles

This repository follows a few principles throughout the challenge.

### 1. Learn by Building

Concepts are implemented rather than only studied theoretically.

### 2. Understand Before Abstracting

Frameworks are used as tools, but the underlying concepts are studied wherever possible.

### 3. Incremental Complexity

The learning path progresses from simple implementations toward more complex AI systems.

### 4. Reproducibility

Experiments should be structured so they can be understood and reproduced later.

### 5. Clean Code

Code quality, readability, modularity, and maintainability are treated as important parts of the learning process.

### 6. Continuous Improvement

Earlier implementations may be revisited and improved as understanding increases.

---

## What This Repository Represents

This repository is **not intended to be a collection of copy-pasted tutorials**.

It represents a continuous attempt to understand:

```text
How AI works
      ↓
How models are built
      ↓
How models are used
      ↓
How LLM applications are engineered
      ↓
How AI systems interact with tools and data
      ↓
How autonomous AI agents can be designed
```

The objective is to gradually move from **using AI APIs** toward understanding and engineering the systems built around them.

---

## Development Environment

Most experiments are developed using:

```text
Python
Virtual Environment
VS Code
Jupyter Notebook
Git
GitHub
```

A typical setup can be created using:

```bash
git clone <repository-url>

cd 100DaysOfAI

python -m venv .venv
```

Activate the environment:

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

API keys and credentials should **never be committed to the repository**.

Use environment variables or a local `.env` file when required.

Example:

```env
OPENAI_API_KEY=your_api_key
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
```

Ensure sensitive files are included in `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
.ipynb_checkpoints/
```

---

## Git & Version Control

Git is used throughout the challenge to maintain a history of the learning process.

The repository follows a simple workflow:

```text
Learn
  ↓
Code
  ↓
Test
  ↓
Commit
  ↓
Push
  ↓
Continue
```

This allows the repository to function not only as an AI learning archive but also as evidence of consistent software development practice.

---

## Learning Philosophy

The challenge is built around a simple idea:

> **Consistency compounds.**

One day of learning may produce a small script.

Ten days may produce several experiments.

Fifty days may produce a collection of reusable components.

One hundred days should produce a substantially stronger understanding of how modern AI systems are built.

The objective is therefore not simply to reach **Day 100**, but to develop the ability to independently:

* Understand AI concepts
* Read technical documentation
* Implement algorithms
* Work with AI models
* Debug AI applications
* Evaluate approaches
* Design AI architectures
* Build practical AI systems

---

## Current Status

**Challenge:** 100 Days of AI
**Progress:** `In Progress`
**Focus:** Artificial Intelligence & AI Engineering
**Primary Language:** Python

```text
[████████████████░░░░░░░░░░░░░░] Learning in Progress
```

The repository will continue evolving throughout the challenge.

---

## Future Direction

After completing the 100-day challenge, the focus will shift toward deeper engineering and research-oriented work, including:

* Building production-oriented AI applications
* Advanced LLM architectures
* Agentic systems
* RAG optimization
* Model evaluation
* AI system reliability
* AI research experimentation
* Open-source contributions
* Larger end-to-end projects

---

## Author

**Soham Deshmukh**

Computer Science Student | AI & Software Engineering Enthusiast

This repository represents my ongoing journey toward becoming a stronger **AI Engineer and Software Developer**.

---

## Disclaimer

This repository is primarily a **learning and experimentation workspace**.

Some implementations may be simplified for educational purposes, while others may evolve significantly as my understanding improves. Code quality and architecture are continuously refined throughout the challenge.

---

## ⭐ If You Find This Useful

If you're also learning AI, feel free to explore the repository, experiment with the code, and use the implementations as learning references.

**Learn. Build. Experiment. Improve. Repeat.**
