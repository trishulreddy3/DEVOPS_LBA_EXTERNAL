# Experiment 1: Factorial Program & CI with Docker

## Objectives
- **1.a**: Write a Python program to calculate the factorial of a given number. Create a GitHub repository and push the code using Git.
- **1.b**: Configure a Jenkins job to execute the program and create a Docker image for the application.

---

## 1. Project Files
- `factorial.py`: Main Python script supporting interactive or CLI input.
- `test_factorial.py`: Unit test suite verifying edge cases (0, 1, negatives, positives).
- `Dockerfile`: Multi-stage verification and lightweight Python container.
- `Jenkinsfile`: Declarative pipeline for automated test execution, Docker build, and container run.

---

## 2. Step-by-Step Git & GitHub Operations (1.a)

### Step 1: Initialize Git Repository
Open a terminal in `Experiment-1_Factorial`:
```bash
git init
```

### Step 2: Add Files & Commit
```bash
git add .
git commit -m "feat: Add factorial program, unit tests, and Dockerfile"
```

### Step 3: Create GitHub Repository & Push
1. Go to [GitHub](https://github.com/new) and create a new repository (e.g., `devops-factorial-app`).
2. Link your local repo and push:
```bash
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/devops-factorial-app.git
git push -u origin main
```

---

## 3. Configure Jenkins Job (1.b)

### Method A: Declarative Pipeline (Recommended)
1. In Jenkins Dashboard, click **New Item** -> Enter name `factorial-pipeline` -> Select **Pipeline** -> Click **OK**.
2. Scroll to the **Pipeline** section:
   - **Definition**: *Pipeline script from SCM*
   - **SCM**: *Git*
   - **Repository URL**: `https://github.com/<YOUR_GITHUB_USERNAME>/devops-factorial-app.git`
   - **Branch Specifier**: `*/main`
   - **Script Path**: `Jenkinsfile`
3. Click **Save** and click **Build Now**.

### Method B: Freestyle Project (Alternative)
1. Click **New Item** -> Name `factorial-freestyle` -> Select **Freestyle project** -> Click **OK**.
2. **Source Code Management**: Select **Git** and enter Repository URL.
3. **Build Steps**:
   - Add **Execute shell** (or **Execute Windows batch command** on Windows):
     ```bash
     python3 factorial.py 5
     docker build -t factorial-app:latest .
     docker run --rm factorial-app:latest
     ```
4. Click **Save** and **Build Now**.

---

## 4. Local Execution & Docker Verification

### Run Python Program Directly
```bash
# Interactive mode:
python factorial.py

# Command-line argument mode:
python factorial.py 6
# Output: [Result] Factorial of 6 (6!) = 720
```

### Run Unit Tests
```bash
python -m unittest test_factorial.py
```

### Build and Run Docker Image Manually
```bash
# Build the image
docker build -t factorial-app:latest .

# Run the container
docker run --rm factorial-app:latest

# Run with custom number
docker run --rm factorial-app:latest python factorial.py 10
```
