# Spec2Test Agent (Robot Framework AI Automation)

## 📌 Project Overview
This project is an **Enterprise-Scale API Automation Testing Framework** powered by Robot Framework and enhanced with an **Agentic AI Workflow (Gemini)**. 
It is designed to automatically generate Data-Driven and Keyword-Driven test cases directly from Jira/Confluence specifications while strictly preserving the team's coding conventions, file structures, and indexing formats.

## 🚀 Key Features
- **Data-Driven Architecture:** Complete separation of Test Data (`.json`), Test Suites (`.robot`), and core validation logic (Keywords) to cleanly support massive scale repositories (100+ API definitions).
- **Context-Aware AI Generation:** Includes an embedded IDE AI workflow that actively scans existing project files to flawlessly mimic the exact coding style, spacing, and variable structures of your workspace.
- **Safe Execution (Approval Gate):** The Agent provides a "Code Preview" mechanism in chat and waits for explicit explicit human approval before securely mutating and injecting code directly into the workspace storage.
- **Scalable Modularization:** Master keywords cleanly act as proxies while sub-checkers validate respective Status Codes (200, 401, 500), preserving maintainability over time.

## 📁 Project Structure
```text
Agent testcase/ 
│── JsonFile/         # Contains external Data-Driven schema payloads keyed by iteration strings.
│── Keywords/         # Contains master executing keywords (Entry Points) for routing payload executions.
│   └── [Module]/     # Contains detailed schema assertion logic and validation routers.
│── TestSuite/        # Runnable .robot execution suites.
│── .agents/          # Encapsulates contextual AI Agent behaviors and custom IDE slash commands.
└── AgentForCreateTestcase.md # The Golden Rulebook (System Instructions) defining the AI formatting and validation rules.
```

## 🤖 Automations & Workflow
1. Provide the IDE AI with a natural language specification snippet (e.g. Jira Acceptance Criteria).
2. The agent independently reads `AgentForCreateTestcase.md` alongside targeted project files.
3. The system maps the appropriate data row indexing, constructs payload expectations, and drafts execution lines.
4. After visual verification via chat, the pipeline injects the code into the correct directories. Run `robot TestSuite/` downstream to witness test execution.

## 🛠 Tech Stack Overview
- **Robot Framework** (Core Automation framework)
- **JSONLibrary / Collections** (Data ingestion & extraction algorithms)
- **Google Generative AI / Gemini Copilot** (Natural-language-to-code generative proxying)
