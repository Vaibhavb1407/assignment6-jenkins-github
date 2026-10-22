# Assignment 6 - Jenkins and GitHub Integration

This repository demonstrates source checkout and CI build execution with Jenkins.

## Contents

- `app.py`: Small Python application whose output confirms execution.
- `tests/test_app.py`: Automated check for the application's output.
- `Jenkinsfile`: Declarative pipeline with Build and Test stages. Configure the Pipeline job to load this file from the repository (Pipeline script from SCM).

## Run locally (Windows PowerShell)

```powershell
python app.py
python -m pip install pytest
python -m pytest -q
```

## Publish to GitHub

Create an empty GitHub repository named `assignment6-jenkins-github` (do not initialize it with a README), then run these commands from this folder:

```powershell
git init
git branch -M main
git add .
git commit -m "Add Jenkins GitHub integration demo"
git remote add origin https://github.com/YOUR-USERNAME/assignment6-jenkins-github.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. GitHub may open a browser sign-in prompt.

## Jenkins job

Create a **Pipeline** job and select **Pipeline script from SCM**. Choose **Git**, enter your repository URL, set branch to `*/main`, and set script path to `Jenkinsfile`. Save, then select **Build Now** and capture the actual Console Output showing checkout, Build, Test, and `Finished: SUCCESS`.

