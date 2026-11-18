# Experiment 2: Prime Number Checker, CI with Jenkins & Kubernetes Deployment

## Objectives
- **2.a**: Write a Python program to check whether a given number is prime or not. Perform basic Git operations (`git add`, `git commit`, `git push`).
- **2.b**: Configure Jenkins for Continuous Integration and deploy a sample application using Kubernetes.

---

## 1. Project Files
- `prime.py`: CLI and modular prime verification algorithm with detailed output.
- `test_prime.py`: Unit tests for negative, zero, 1, small primes, composites, and large primes.
- `app.py`: Standalone microservice with HTTP health endpoint (`/healthz`) and query endpoint (`/check?num=...`).
- `Dockerfile`: Packages the microservice into a container image.
- `k8s/deployment.yaml`: Kubernetes Deployment (2 replicas, resource limits, readiness/liveness probes).
- `k8s/service.yaml`: Kubernetes Service (`NodePort` on port `30080` targeting port `8000`).
- `Jenkinsfile`: Complete CI/CD Pipeline (Checkout -> Test -> Docker Build -> Kubectl Apply -> Status Check).

---

## 2. Basic Git Operations (2.a)

```bash
# 1. Initialize local repository
git init

# 2. Check repository status
git status

# 3. Add all files to the staging area
git add .

# 4. Commit changes with a meaningful message
git commit -m "feat: Add prime number checker, REST microservice, Dockerfile, and k8s manifests"

# 5. Link to your GitHub remote repository
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/devops-prime-app.git

# 6. Push code to remote repository
git push -u origin main
```

---

## 3. Local Testing & Verification

### Test Python Script
```bash
# Direct execution (interactive)
python prime.py

# Command-line argument
python prime.py 29
# Output: [Result] Number 29 is PRIME

# Run unit tests
python -m unittest test_prime.py
```

### Build & Run Docker Container
```bash
# Build Docker image
docker build -t prime-app:latest .

# Run container on port 8000
docker run -d -p 8000:8000 --name prime-container prime-app:latest

# Test via curl or browser
curl http://localhost:8000/check?num=31
curl http://localhost:8000/healthz

# Stop container
docker stop prime-container && docker rm prime-container
```

---

## 4. Kubernetes Deployment & Jenkins Configuration (2.b)

### Manual Kubernetes Deployment (Minikube / Kind / Docker Desktop K8s)
```bash
# 1. Ensure cluster is active
kubectl cluster-info

# 2. Apply deployment and service
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# 3. Check status of pods and services
kubectl get pods -l app=prime-app
kubectl get svc prime-app-service

# 4. Access the service
# If using Minikube:
minikube service prime-app-service

# Or port-forward directly:
kubectl port-forward svc/prime-app-service 8000:8000
# Then visit: http://localhost:8000/check?num=17
```

### Jenkins CI/CD Setup
1. Open Jenkins -> **New Item** -> `prime-ci-k8s` -> Choose **Pipeline** -> Click **OK**.
2. Under **Pipeline**:
   - Definition: **Pipeline script from SCM**
   - SCM: **Git**
   - Repo URL: `https://github.com/<YOUR_GITHUB_USERNAME>/devops-prime-app.git`
   - Script Path: `Jenkinsfile`
3. Click **Save** and trigger **Build Now**.
4. Observe each stage: *Checkout*, *Run Unit Tests*, *Build Docker Image*, *Deploy to Kubernetes*, and *Verify Deployed Application*.
