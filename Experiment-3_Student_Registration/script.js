/**
 * Student Registration Form Validation and Handling
 */

function validateForm(data) {
    let isValid = true;

    // Reset error messages
    document.querySelectorAll('.error-text').forEach(el => el.textContent = '');

    // Name Validation (at least 3 characters, alphabets & spaces)
    if (!data.fullName || data.fullName.trim().length < 3) {
        document.getElementById('nameError').textContent = 'Name must be at least 3 characters long.';
        isValid = false;
    }

    // Email Validation (Regex)
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(data.email)) {
        document.getElementById('emailError').textContent = 'Please enter a valid email address.';
        isValid = false;
    }

    // Phone Validation (10 digits)
    const phonePattern = /^[0-9]{10}$/;
    if (!phonePattern.test(data.phone.replace(/[\s-]/g, ''))) {
        document.getElementById('phoneError').textContent = 'Phone number must be exactly 10 digits.';
        isValid = false;
    }

    // DOB Validation
    if (!data.dob) {
        document.getElementById('dobError').textContent = 'Please select a valid date of birth.';
        isValid = false;
    }

    // Gender Validation
    if (!data.gender) {
        document.getElementById('genderError').textContent = 'Please select a gender.';
        isValid = false;
    }

    // Course Validation
    if (!data.course) {
        document.getElementById('courseError').textContent = 'Please select a course.';
        isValid = false;
    }

    return isValid;
}

function handleFormSubmit(event) {
    event.preventDefault();

    const statusEl = document.getElementById('statusMessage');
    statusEl.className = 'status-msg';

    const formData = {
        fullName: document.getElementById('fullName').value.trim(),
        email: document.getElementById('email').value.trim(),
        phone: document.getElementById('phone').value.trim(),
        dob: document.getElementById('dob').value,
        gender: document.getElementById('gender').value,
        course: document.getElementById('course').value
    };

    if (!validateForm(formData)) {
        statusEl.textContent = 'Please correct the highlighted errors before submitting.';
        statusEl.classList.add('error');
        return false;
    }

    // Success State
    statusEl.textContent = 'Student registered successfully!';
    statusEl.classList.add('success');

    // Add row to table
    const tableBody = document.getElementById('recordsBody');
    const row = document.createElement('tr');
    row.innerHTML = `
        <td>${formData.fullName}</td>
        <td>${formData.email}</td>
        <td>${formData.phone}</td>
        <td>${formData.gender}</td>
        <td>${formData.course}</td>
    `;
    tableBody.appendChild(row);

    // Reveal table section
    document.getElementById('recordsSection').style.display = 'block';

    // Clear inputs
    document.getElementById('registrationForm').reset();
    return true;
}

function resetForm() {
    document.getElementById('registrationForm').reset();
    document.querySelectorAll('.error-text').forEach(el => el.textContent = '');
    const statusEl = document.getElementById('statusMessage');
    statusEl.className = 'status-msg';
    statusEl.textContent = '';
}
