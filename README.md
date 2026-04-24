# 🧪 Jenkins CI/CD Python Lab

## 📌 Project Overview

This is a beginner-friendly CI/CD pipeline project using Jenkins.

It demonstrates:

* Code checkout from GitHub
* Dependency installation
* Running unit tests using pytest
* Publishing test reports in Jenkins

---

## 🧮 Application

A simple Python calculator with functions:

* Add
* Subtract
* Multiply
* Divide

---

## 📁 Project Structure

```
jenkins-python-lab/
│
├── app.py
├── test_app.py
├── requirements.txt
├── Jenkinsfile
└── README.md
```

---

## ⚙️ How to Run Locally

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run tests

```
pytest
```

---

## 🚀 Jenkins Pipeline Stages

1. Checkout code from GitHub
2. Install dependencies
3. Run unit tests
4. Generate test report

---

## 📊 Test Reports

Jenkins generates a report using:

```
pytest --junitxml=report.xml
```

---

## 🎯 Objective

To understand how CI (Continuous Integration) works using Jenkins.

---

## 🔮 Future Enhancements

* Add security scans (Gitleaks, pip-audit)
* Add SonarQube for code quality
* Add deployment stage

---

## 👨‍💻 Author

Your Name
