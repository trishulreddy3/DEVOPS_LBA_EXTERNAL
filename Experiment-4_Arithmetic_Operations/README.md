# Experiment 4: Arithmetic Operations, Jenkins CI & Kubernetes Deployment

## Objectives
- **4.a**: Write a Python program to perform addition, subtraction, multiplication, and division. Create a GitHub repository and push the source code.
- **4.b**: Configure Jenkins to execute the program and demonstrate application deployment using Kubernetes.

---

## 1. Project Files
- `arithmetic.py`: Addition, subtraction, multiplication, and division functions with CLI and interactive menus.
- `test_arithmetic.py`: Unit tests validating all four operations, float logic, and zero division exceptions.
- `app.py`: REST microservice exposing `/calc?op=add&a=10&b=20` and `/healthz`.
- `Dockerfile`: Multi-stage verification and lightweight Python container.
- `k8s/deployment.yaml`: Kubernetes Deployment (2 replicas, CPU/memory limits, probes).
- `k8s/service.yaml`: Kubernetes NodePort Service on port `30081`.
- `Jenkinsfile`: Complete CI/CD Pipeline (Checkout -> Unit Tests -> Demo Execution -> Docker Build -> Kubectl Deploy -> Verify).

---

## 2. Git & GitHub Operations (4.a)

```bash
# 1. Initialize local Git repository
git init

# 2. Stage all files
git add .

# 3. Commit files
git commit -m "feat: Add arithmetic operations program, tests, Dockerfile, and k8s manifests"

# 4. Link to GitHub repository
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/devops-arithmetic-app.git

# 5. Push to GitHub
git push -u origin main
```

---

## 3. Local Execution & Testing

### Run Arithmetic Program
```bash
# Interactive menu:
python arithmetic.py

# Direct command-line execution:
python arithmetic.py add 15 25
python arithmetic.py sub 50 18
python arithmetic.py mul 6 7
python arithmetic.py div 100 4

# Run unit tests:
python -m unittest test_arithmetic.py
```

### Docker Build & Run
```bash
# Build Docker image
docker build -t arithmetic-app:latest .

# Run container on port 8080
docker run -d -p 8080:8080 --name arithmetic-container arithmetic-app:latest

# Query endpoints
curl "http://localhost:8080/calc?op=add&a=15&b=25"
curl "http://localhost:8080/calc?op=mul&a=8&b=9"
curl "http://localhost:8080/healthz"

# Stop container
docker stop arithmetic-container && docker rm arithmetic-container
```

---

## 4. Kubernetes Deployment & Jenkins Pipeline (4.b)

### Manual Kubernetes Deployment
```bash
# Apply deployment and service
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Check pods and services
kubectl get pods -l app=arithmetic-app
kubectl get svc arithmetic-app-service

# Port-forward to test locally
kubectl port-forward svc/arithmetic-app-service 8080:8080
# Visit in browser: http://localhost:8080/calc?op=add&a=50&b=25
```

### Jenkins CI/CD Pipeline Setup
1. In Jenkins, click **New Item** -> Name `arithmetic-ci-k8s` -> Choose **Pipeline** -> **OK**.
2. Under **Pipeline**:
   - Definition: **Pipeline script from SCM**
   - SCM: **Git**
   - Repository URL: `https://github.com/<YOUR_GITHUB_USERNAME>/devops-arithmetic-app.git`
   - Script Path: `Jenkinsfile`
3. Click **Save** and trigger **Build Now**.
4. Check build console logs for green stages:
   - *Checkout Code*
   - *Execute Unit Tests*
   - *Execute Program Demonstrations*
   - *Build Docker Image*
   - *Deploy to Kubernetes*
   - *Verify K8s Pods and Service*
