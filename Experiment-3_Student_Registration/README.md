# Experiment 3: Student Registration Form & Automated Selenium Testing

## Objectives
- **3.a**: Create a simple student registration form using HTML and JavaScript. Maintain the source code using Git and GitHub.
- **3.b**: Create a Docker container for the application and perform automated form testing using Selenium.

---

## 1. Project Files
- `index.html`: Responsive student registration form with input validation hooks.
- `style.css`: Clean, modern dark-themed styling.
- `script.js`: Client-side validation (regex for email & phone, length checks) and dynamic table insertion.
- `Dockerfile`: Production-ready Nginx image hosting the web form on port 80.
- `test_form.py`: Python Selenium automated test suite validating field interactions and assertions.
- `requirements.txt`: Python dependencies (`selenium`, `webdriver-manager`).

---

## 2. Git & GitHub Operations (3.a)

```bash
# Initialize git in Experiment-3 directory
git init

# Stage all files
git add .

# Commit files
git commit -m "feat: Add student registration form, Nginx Dockerfile, and Selenium tests"

# Link to GitHub and push
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/devops-student-form.git
git push -u origin main
```

---

## 3. Docker Containerization (3.b)

### Build the Docker Image
```bash
docker build -t student-registration-app:latest .
```

### Run the Container
```bash
docker run -d -p 8080:80 --name student-form-container student-registration-app:latest
```

### Verify Container in Browser
Open your browser and navigate to:
```
http://localhost:8080
```

---

## 4. Automated Testing Using Selenium (3.b)

### Install Prerequisites
```bash
pip install -r requirements.txt
```

### Execute Selenium Automated Tests

**Option 1: Test Against Running Docker Container (Recommended)**
```bash
python test_form.py http://localhost:8080
```

**Option 2: Test Against Local HTML File Directly**
```bash
python test_form.py
```

### Expected Output
```text
============================================================
      DevOps Lab - Selenium Automated Form Testing      
============================================================
[Target URL] http://localhost:8080

[Driver] Initialized Chrome WebDriver successfully (Headless).
Step 1: Navigating to student registration form...
Step 2: Locating input fields...
Step 3: Entering student registration details...
Step 4: Clicking 'Register Student' submit button...
Step 5: Waiting for status response...

[Observed Message] "Student registered successfully!"

============================================================
TEST PASSED: Student Registration Form successfully validated via Selenium!
============================================================

[Browser] WebDriver session closed.
```

### Stop & Remove Docker Container After Testing
```bash
docker stop student-form-container && docker rm student-form-container
```
