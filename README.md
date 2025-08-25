# Assignment 2 — Team Repo

This repo is set up for coding **and** communication using GitHub.

## Quick Start
1. **Clone**: `git clone <your-repo-url>`
2. **Create a branch** (never push to `main` directly):  
   `git checkout -b feature/your-name-task`
3. Do the work inside `src/` (we copied the provided starter files here).
4. **Commit small & often** with clear messages.  
   Example: `git commit -m "ENG151: add vector addition helper and tests"`
5. **Push & open a Pull Request (PR)** to `main`.
6. Request **reviews** from teammates and address comments.
7. When approved, **Squash & Merge** the PR.

## Repo Layout
```
/src            <- assignment source files (copied from the zip)
/docs           <- design notes, decisions, meeting minutes
/.github        <- issue/PR templates and CI workflows
README.md       <- you're reading this
.gitignore
```
## Branching
- `main` is always **working** and **reviewed**.
- Use short-lived branches: `feature/<description>`, `fix/<ticket-id>`, `docs/<topic>`.

## Commit Message Convention
- Use **imperative** tone: "add X", "fix Y".
- Prefix with scope if helpful, e.g., `ENG151:` or `SMA104:`

## Issues & Project Board
- Create Issues for tasks/bugs with clear **Definition of Done**.
- Use the **Projects** board (Kanban: *Todo → In Progress → In Review → Done*).
- Link Issues in PRs (`Closes #12`).

## Reviews
- Minimum **1 reviewer**; prefer **2** on risky changes.
- Non-blocking nitpicks as comments; blocking concerns as **Request changes**.

## Communication
- Prefer **Issues** for tasks and **Discussions** (if enabled) for open-ended chats.
- Summarise live meetings in `/docs/meeting-notes-YYYY-MM-DD.md` and link them from Issues/PRs.

## Setup
- Add any environment/setup steps here (language, versions, linters, testing).
- Example for Python:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate  # Windows: .venv\Scripts\activate
  pip install -r requirements.txt
  pytest -q
  ```

## CI (optional)
- Add simple CI under `.github/workflows/` once tests exist.

## How to Submit
- Tag a release: **v1.0.0** with the final commit hash and attach required artefacts.
- Export a PDF of `/docs/REPORT.md` if needed by your rubric.

## Acknowledgements

This repository’s initial structure (README, .gitignore, issue templates, PR template, and CI setup) was generated with assistance from **ChatGPT (OpenAI, 2025)** to help establish good GitHub collaboration practices for this assignment.