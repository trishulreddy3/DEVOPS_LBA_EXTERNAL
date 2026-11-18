# DevOps Lab External Examination

Comprehensive implementation of all 4 DevOps Laboratory experiments covering **Git, Jenkins, Docker, Kubernetes, and Selenium**.

---

## Repository Structure

```
├── Experiment-1_Factorial/
│   ├── factorial.py            # Python Factorial program
│   ├── test_factorial.py       # Unit tests
│   ├── Dockerfile              # Container definition
│   ├── Jenkinsfile             # Jenkins CI pipeline
│   └── README.md               # Step-by-step instructions
│
├── Experiment-2_Prime_Number/
│   ├── prime.py                # Python Prime checker
│   ├── test_prime.py           # Unit tests
│   ├── app.py                  # HTTP microservice
│   ├── Dockerfile              # Container definition
│   ├── Jenkinsfile             # Jenkins CI/CD pipeline
│   ├── k8s/
│   │   ├── deployment.yaml     # Kubernetes Deployment
│   │   └── service.yaml        # Kubernetes Service (NodePort)
│   └── README.md               # Guide
│
├── Experiment-3_Student_Registration/
│   ├── index.html              # Registration web form
│   ├── style.css               # Styling
│   ├── script.js               # Client validation
│   ├── Dockerfile              # Nginx web server container
│   ├── requirements.txt        # Selenium dependencies
│   ├── test_form.py            # Automated Selenium testing script
│   └── README.md               # Guide
│
├── Experiment-4_Arithmetic_Operations/
│   ├── arithmetic.py           # Arithmetic operations in Python
│   ├── test_arithmetic.py      # Unit tests
│   ├── app.py                  # HTTP microservice
│   ├── Dockerfile              # Container definition
│   ├── Jenkinsfile             # Jenkins CI/CD pipeline
│   ├── k8s/
│   │   ├── deployment.yaml     # Kubernetes Deployment
│   │   └── service.yaml        # Kubernetes Service (NodePort)
│   └── README.md               # Guide
│
└── LAB_VIVA_AND_EXECUTION_GUIDE.md  # Viva questions, concepts, and cheat sheet
```

---

## Experiments Summary

### 1. Factorial Program
- **1.a**: Python calculation with unit tests & GitHub version control.
- **1.b**: Jenkins automated job and Docker containerization.

### 2. Prime Number Program
- **2.a**: Prime verification with Git version control (`add`, `commit`, `push`).
- **2.b**: Jenkins Continuous Integration & Kubernetes deployment (`Deployment` & `Service`).

### 3. Student Registration Form
- **3.a**: HTML5 + CSS + JavaScript registration form.
- **3.b**: Docker container using Nginx and automated browser testing with Selenium WebDriver.

### 4. Arithmetic Operations
- **4.a**: Addition, Subtraction, Multiplication, Division with unit testing.
- **4.b**: Jenkins automated pipeline execution & Kubernetes application deployment.
