# Multi-Agent-AI-App
Multi-Agents AI System building from Scratch in python without any dependency of frameworks! 🤖 
This Python-based app leverages OpenAI's GPT-4o model with a simple Streamlit web interface to tackle specialized tasks to create agentic systems without using orchestration frameworks like Crew AI or LangGraph. 🎉

![ Multi Agent AI App](logo.png)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Agents](#agents)
  - [Main Agents](#main-agents)
  - [Validator Agents](#validator-agents)
- [Logging](#logging)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Overview

The **Multi-Agents AI System from Scratch** is a Python-based application leveraging OpenAI's GPT-4o model to perform specialized tasks through a collaborative multi-agent architecture. Built with Streamlit for an intuitive web interface without any Agents frameworks/libraries, this system includes agents for summarizing medical texts, writing research articles, and sanitizing medical data (Protected Health Information - PHI). Each primary agent is paired with a corresponding validator agent to ensure the quality and accuracy of the outputs. Built it for beginners so they can understand that Agents can be built without orchestration frameworks like Crew AI, AutoGen, LangGraph, etc.

## Features

- **Summarize Medical Texts:** Generate concise summaries of lengthy medical documents.
- **Write Research Articles:** Create detailed research articles based on a given topic and optional outline.
- **Sanitize Medical Data (PHI):** Remove sensitive health information from medical datasets.
- **Quality Validation:** Each primary task is accompanied by a validator agent to assess and ensure output quality.
- **Robust Logging:** Comprehensive logging for monitoring and debugging purposes.
- **User-Friendly Interface:** Streamlit-based web app for easy interaction and task management.

## Architecture

```
+-------------------+
|       User        |
+---------+---------+
          |
          | Interacts via
          v
+---------+---------+
|    Streamlit App  |
+---------+---------+
          |
          | Sends task requests to
          v
+---------+---------+
|  Agent Manager    |
+---------+---------+
          |
          +---------------------------------------------+
          |                      |                      |
          v                      v                      v
+---------+---------+  +---------+---------+  +---------+---------+
|  Summarize Agent  |  |  Write Article    |  |  Sanitize Data    |
|  (Generates summary)| |  (Generates draft)| |  (Removes PHI)    |
+---------+---------+  +---------+---------+  +---------+---------+
          |                      |                      |
          v                      v                      v
+---------+---------+  +---------+---------+  +---------+---------+
|Summarize Validator|  | Refiner Agent      |  |Sanitize Validator |
|      Agent        |  |  (Enhances draft)  |  |      Agent        |
+---------+---------+  +---------+----------+ +----------+--------+
          |                      |                      |
          |                      |                      |
          +-----------+----------+-----------+----------+
                      |                      |
                      v                      v
                +-----+-------+        +-----+-------+
                |   Logger    |        |   Logger    |
                +-------------+        +-------------+
```

### Components Breakdown

1. **User**
   - Interacts with the system via the Streamlit web interface.
   - Selects tasks and provides input data.

2. **Streamlit App**
   - Frontend interface for user interaction.
   - Sends user requests to the Agent Manager.
   - Displays results and validation feedback.

3. **Agent Manager**
   - Central coordinator for all agents.
   - Delegates tasks to appropriate main and validator agents.

4. **Main Agents**
   - **Summarize Agent:** Generates summaries of medical texts.
   - **Write Article Agent:** Creates drafts of research articles.
   - **Sanitize Data Agent:** Removes PHI from medical data.

5. **Validator Agents**
   - **Summarize Validator Agent:** Assesses the quality of summaries.
   - **Refiner Agent:** Enhances drafts for better quality.
   - **Sanitize Validator Agent:** Ensures all PHI has been removed.

6. **Logger**
   - Records all interactions, inputs, outputs, and errors.
   - Facilitates monitoring and debugging.

## Installation

### Prerequisites

- **Python 3.8 or higher**: [Download Python](https://www.python.org/downloads/)
- **OpenAI API Access**: [Sign up for OpenAI's API](https://platform.openai.com/signup)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/milojeBtc/Multi-Ai-Agent.git
   cd Multi-Agent-AI-App
   ```

2. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the project root:

   ```dotenv
   OPENAI_API_KEY=your-api-key-here
   ```

   Alternatively, set the environment variable directly:

   - **Unix/MacOS:**

     ```bash
     export OPENAI_API_KEY='your-api-key-here'
     ```

   - **Windows:**

     ```bash
     set OPENAI_API_KEY=your-api-key-here
     ```

## Usage

1. **Activate the Virtual Environment**

   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Run the Streamlit App**

   ```bash
   streamlit run app.py
   ```

3. **Access the App**

   Open the URL provided by Streamlit (usually `http://localhost:8501`) in your web browser.

4. **Interact with the Tasks**

   - **Summarize Medical Text:** Input medical texts to receive concise summaries.
   - **Write and Refine Research Article:** Provide a topic and optional outline to generate and refine research articles.
   - **Sanitize Medical Data (PHI):** Input medical data to remove sensitive information.

## Agents

### Main Agents

- **Summarize Agent**
  - **Function:** Generates summaries of provided medical texts.
  - **Usage:** Input the text, and receive a concise summary.

- **Write Article Agent**
  - **Function:** Creates drafts of research articles based on a topic and optional outline.
  - **Usage:** Provide a topic and outline to generate an initial draft.

- **Sanitize Data Agent**
  - **Function:** Removes Protected Health Information (PHI) from medical data.
  - **Usage:** Input medical data containing PHI to receive sanitized data.

### Validator Agents

- **Summarize Validator Agent**
  - **Function:** Validates the accuracy and quality of summaries.
  - **Usage:** Receives the original text and its summary to assess quality.

- **Refiner Agent**
  - **Function:** Enhances and refines research article drafts for better clarity and coherence.
  - **Usage:** Receives a draft article and returns an enhanced version.

- **Sanitize Validator Agent**
  - **Function:** Ensures that all PHI has been removed from sanitized data.
  - **Usage:** Receives original and sanitized data to verify PHI removal.

## Logging

- **Location:** Logs are stored in the `logs/` directory.
- **Files:**
  - `multi_agent_system.log`: Contains detailed logs for monitoring and debugging.
- **Configuration:** Logging is handled using the `loguru` library, configured in `utils/logger.py`.

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**
2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add your feature"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**
   

## Acknowledgements

- [OpenAI](https://openai.com/) for providing the GPT-4 model.
- [Streamlit](https://streamlit.io/) for the web application framework.
- [Loguru](https://github.com/Delgan/loguru) for the logging library.
- Inspired by collaborative multi-agent system architectures and prompt engineering techniques like Chain-of-Thought (CoT) and ReAct.

## 👥 Contact

- Telegram [@michalstefanow](https://t.me/mylord1_1)
- Twitter [@michalstefanow](https://x.com/michalstefanow)

## ©️ License 🪪 

Distributed under the MIT License. See `LICENSE` for more information.
