# DevOps Lab External Examination - Master Execution & Viva Guide

This workspace contains complete implementations for all 4 external lab experiments organized into distinct modular directories.

---

## Workspace Structure

```
E:\Deops_Lab_External\
│
├── Experiment-1_Factorial/
│   ├── factorial.py            # Factorial Python program (interactive + CLI)
│   ├── test_factorial.py       # Unit tests
│   ├── Dockerfile              # Container definition
│   ├── Jenkinsfile             # CI pipeline script
│   └── README.md               # Step-by-step guide
│
├── Experiment-2_Prime_Number/
│   ├── prime.py                # Prime number checker (interactive + CLI)
│   ├── test_prime.py           # Unit tests
│   ├── app.py                  # HTTP microservice (health + check endpoints)
│   ├── Dockerfile              # Docker container definition
│   ├── Jenkinsfile             # CI/CD pipeline
│   ├── k8s/
│   │   ├── deployment.yaml     # Kubernetes Deployment (2 replicas, probes)
│   │   └── service.yaml        # Kubernetes NodePort Service (port 30080)
│   └── README.md               # Detailed execution steps
│
├── Experiment-3_Student_Registration/
│   ├── index.html              # Modern registration form
│   ├── style.css               # Form styling
│   ├── script.js               # Client validation & table rendering
│   ├── Dockerfile              # Nginx web server container
│   ├── requirements.txt        # Selenium & webdriver dependencies
│   ├── test_form.py            # Selenium automated test script
│   └── README.md               # Execution steps
│
├── Experiment-4_Arithmetic_Operations/
│   ├── arithmetic.py           # +, -, *, / calculations
│   ├── test_arithmetic.py      # Unit tests covering operations & exceptions
│   ├── app.py                  # HTTP calculation API
│   ├── Dockerfile              # Container definition
│   ├── Jenkinsfile             # Jenkins CI/CD pipeline
│   ├── k8s/
│   │   ├── deployment.yaml     # Kubernetes Deployment (2 replicas)
│   │   └── service.yaml        # Kubernetes NodePort Service (port 30081)
│   └── README.md               # Detailed guide
│
└── LAB_VIVA_AND_EXECUTION_GUIDE.md
```

---

## Quick Command Cheat Sheet for the External Exam

### Experiment 1: Factorial Program (Git + Jenkins + Docker)
```bash
cd Experiment-1_Factorial

# 1.a: Test Python program locally
python factorial.py 5

# 1.a: Git Commands
git init
git add .
git commit -m "Add Factorial program and Dockerfile"
git branch -M main
git remote add origin https://github.com/<YOUR_USER>/factorial-app.git
git push -u origin main

# 1.b: Docker Build & Run
docker build -t factorial-app:latest .
docker run --rm factorial-app:latest python factorial.py 6
```

### Experiment 2: Prime Number Program (Git + Jenkins + Kubernetes)
```bash
cd Experiment-2_Prime_Number

# 2.a: Test Python program
python prime.py 19

# 2.a: Git Commands
git init
git add .
git commit -m "Add Prime number checker and K8s manifests"
git branch -M main
git remote add origin https://github.com/<YOUR_USER>/prime-app.git
git push -u origin main

# 2.b: Docker & Kubernetes Deployment
docker build -t prime-app:latest .
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get pods
kubectl get svc
# Test access via port forward:
kubectl port-forward svc/prime-app-service 8000:8000
# In another terminal or browser: http://localhost:8000/check?num=23
```

### Experiment 3: Student Registration Form (Git + Docker + Selenium)
```bash
cd Experiment-3_Student_Registration

# 3.a: Git Commands
git init
git add .
git commit -m "Add Student Registration Form"
git branch -M main
git remote add origin https://github.com/<YOUR_USER>/student-form.git
git push -u origin main

# 3.b: Docker Container
docker build -t student-form-app:latest .
docker run -d -p 8080:80 --name student-form-container student-form-app:latest

# 3.b: Selenium Automated Testing
pip install -r requirements.txt
# Run test against Docker container:
python test_form.py http://localhost:8080
# Or directly against local HTML file:
python test_form.py
```

### Experiment 4: Arithmetic Operations (Git + Jenkins + Kubernetes)
```bash
cd Experiment-4_Arithmetic_Operations

# 4.a: Run arithmetic program
python arithmetic.py add 12 18
python arithmetic.py mul 6 7
python -m unittest test_arithmetic.py

# 4.a: Git Commands
git init
git add .
git commit -m "Add Arithmetic operations and K8s configuration"
git branch -M main
git remote add origin https://github.com/<YOUR_USER>/arithmetic-app.git
git push -u origin main

# 4.b: Docker & Kubernetes Deployment
docker build -t arithmetic-app:latest .
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get pods
kubectl get svc
kubectl port-forward svc/arithmetic-app-service 8080:8080
# In browser: http://localhost:8080/calc?op=add&a=50&b=25
```

---

## Jenkins Configuration Guide for Examiner Demo

### Creating a Pipeline Job (Recommended for all experiments)
1. Open Jenkins in browser: `http://localhost:8080`
2. Click **New Item** -> Enter Job Name (e.g. `DevOps-Experiment-1`).
3. Select **Pipeline** and click **OK**.
4. Scroll down to **Pipeline** section:
   - **Definition**: Select **Pipeline script from SCM**
   - **SCM**: Select **Git**
   - **Repository URL**: Paste your GitHub repository URL.
   - **Branch Specifier**: `*/main` (or `*/master`)
   - **Script Path**: `Jenkinsfile`
5. Click **Save** -> Click **Build Now**.
6. View the **Stage View** and click on **Console Output** to demonstrate success to the examiner.

### Creating a Freestyle Job (If examiner specifically asks for Freestyle)
1. **New Item** -> Name -> **Freestyle project** -> **OK**.
2. **Source Code Management**: Select **Git** and enter Repo URL.
3. Under **Build Steps**:
   - Add **Execute shell** (Linux) or **Execute Windows batch command** (Windows):
     ```bash
     python -m unittest test_factorial.py
     python factorial.py 5
     docker build -t factorial-app:latest .
     docker run --rm factorial-app:latest
     ```
4. Click **Save** and **Build Now**.

---

## DevOps Lab External Viva Questions & Answers

### 1. Git & GitHub
- **Q: What is the difference between `git pull` and `git fetch`?**
  - *Ans:* `git fetch` downloads commits, files, and refs from a remote repository into your local repo without merging. `git pull` does a `git fetch` followed immediately by a `git merge`.
- **Q: What is the purpose of staging area (`git add`)?**
  - *Ans:* The staging area allows developers to preview, format, and organize changes before committing them permanently to the repository history.

### 2. Jenkins (Continuous Integration & Continuous Deployment)
- **Q: What is Continuous Integration (CI)?**
  - *Ans:* CI is a DevOps practice where developers frequently commit code to a shared repository, and automated builds and tests run to detect defects early.
- **Q: What is the difference between Declarative and Scripted Jenkinsfile?**
  - *Ans:* Declarative pipeline uses structured, simpler syntax with predefined sections (`pipeline`, `agent`, `stages`, `steps`), whereas Scripted pipeline is Groovy-based with procedural flow control (`node`, `stage`).
- **Q: What are Jenkins plugins?**
  - *Ans:* Modular extensions that enhance Jenkins capabilities, e.g., Git plugin, Docker plugin, Kubernetes plugin, HTML Publisher plugin.

### 3. Docker Containerization
- **Q: What is the difference between a Docker Image and a Docker Container?**
  - *Ans:* An image is a read-only, immutable template with instructions for creating a Docker container. A container is a runnable, isolated instance of an image.
- **Q: What is the difference between `COPY` and `ADD` in a Dockerfile?**
  - *Ans:* `COPY` copies local files/directories into the container. `ADD` does the same, but can also unpack local tar archives and fetch URLs. Best practice is to use `COPY`.
- **Q: What does `-p 8080:80` mean in `docker run`?**
  - *Ans:* It maps host port `8080` to container port `80`.

### 4. Kubernetes (Container Orchestration)
- **Q: What is a Pod in Kubernetes?**
  - *Ans:* The smallest deployable computing unit in Kubernetes, representing a single instance of a running process (one or more containers sharing network and storage).
- **Q: What is a Deployment?**
  - *Ans:* A Kubernetes controller that provides declarative updates for Pods and ReplicaSets, managing rolling updates, rollbacks, and scaling.
- **Q: What is a Kubernetes Service and why is it needed?**
  - *Ans:* Pods are ephemeral and their IP addresses change when recreated. A Service provides a stable IP address and DNS name with built-in load balancing.
- **Q: What is NodePort?**
  - *Ans:* A Service type that exposes the service on each Node's IP at a static port (typically between 30000–32767).

### 5. Automated Testing with Selenium
- **Q: What is Selenium WebDriver?**
  - *Ans:* A web automation framework that allows executing tests against different browsers directly using browser native support.
- **Q: Why use headless mode in CI/CD?**
  - *Ans:* In headless mode, browsers run without a graphical user interface (GUI), consuming less memory/CPU and running on headless CI build servers like Jenkins.
- **Q: What is the difference between Implicit Wait and Explicit Wait?**
  - *Ans:* Implicit wait sets a global timeout for locating elements. Explicit wait waits for a specific condition (e.g. element visibility, clickability) to be satisfied before proceeding.
