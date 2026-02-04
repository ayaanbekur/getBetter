// Loading Bar Animation
window.addEventListener('load', function() {
    const loadingBar = document.getElementById('loading-bar');
    if (loadingBar) {
        setTimeout(() => {
            loadingBar.style.display = 'none';
        }, 1000);
    }
});

// Show loading bar on page transitions
window.addEventListener('beforeunload', function() {
    const loadingBar = document.getElementById('loading-bar');
    if (loadingBar) {
        loadingBar.style.display = 'block';
        loadingBar.style.left = '-100%';
    }
});

// Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const mobileMenu = document.querySelector('.mobile-menu');

    if (hamburger) {
        hamburger.addEventListener('click', function() {
            hamburger.classList.toggle('active');
            mobileMenu.classList.toggle('active');
        });
    }

    // Close mobile menu when clicking on a link
    const mobileLinks = document.querySelectorAll('.mobile-menu a');
    mobileLinks.forEach(link => {
        link.addEventListener('click', function() {
            if (hamburger) hamburger.classList.remove('active');
            if (mobileMenu) mobileMenu.classList.remove('active');
        });
    });

    // Dropdown functionality
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
    dropdownToggles.forEach(toggle => {
        toggle.addEventListener('click', function() {
            const content = this.nextElementSibling;
            this.classList.toggle('active');
            content.classList.toggle('active');
        });
    });
});

// Onboarding Overlay Functions
function showOnboarding() {
    const overlay = document.querySelector('.overlay');
    if (overlay) {
        overlay.classList.add('active');
    }
}

function closeOnboarding() {
    const overlay = document.querySelector('.overlay');
    if (overlay) {
        overlay.classList.remove('active');
    }
}

// Selection handler
function toggleSelection(element, category) {
    element.classList.toggle('active');
    updateOnboardingForm();
}

function updateOnboardingForm() {
    const selections = Array.from(document.querySelectorAll('.selection-btn.active'))
        .map(btn => btn.dataset.value);
    
    const substanceForm = document.getElementById('substance-form');
    const lifestyleForm = document.getElementById('lifestyle-form');
    const looksForm = document.getElementById('looks-form');

    if (substanceForm) substanceForm.style.display = selections.some(s => ['vaping', 'nicotine', 'alcohol', 'tobacco', 'weed', 'drugs'].includes(s)) ? 'block' : 'none';
    if (lifestyleForm) lifestyleForm.style.display = selections.includes('lifestyle') ? 'block' : 'none';
    if (looksForm) looksForm.style.display = selections.includes('looks') ? 'block' : 'none';
}

// Form submission
async function submitOnboarding() {
    const selections = Array.from(document.querySelectorAll('.selection-btn.active'))
        .map(btn => btn.dataset.value);

    if (selections.length === 0) {
        alert('Please select at least one option');
        return;
    }

    const data = { selections };

    // Collect substance frequencies
    const substanceFrequencies = document.querySelectorAll('[data-substance]');
    substanceFrequencies.forEach(input => {
        const substance = input.dataset.substance;
        const frequency = input.value;
        data[`${substance}_frequency`] = frequency;
    });

    // Collect lifestyle data
    if (selections.includes('lifestyle')) {
        data.age = document.getElementById('age')?.value || 25;
        data.height = document.getElementById('height')?.value || 180;
        data.weight = document.getElementById('weight')?.value || 75;
        data.activity_level = document.getElementById('activity-level')?.value || 'moderate';
        data.fitness_goal = document.getElementById('fitness-goal')?.value || 'weight_loss';
    }

    try {
        const response = await fetch('/api/save-plan', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        if (result.success) {
            window.location.href = result.redirect;
        } else {
            alert('Error: ' + result.error);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred');
    }
}

// Auth functions
async function handleLogin(event) {
    event.preventDefault();
    
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        const result = await response.json();
        if (result.success) {
            window.location.href = result.redirect;
        } else {
            document.getElementById('error-message').textContent = result.error;
            document.getElementById('error-message').style.display = 'block';
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

async function handleSignup(event) {
    event.preventDefault();
    
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;

    if (password !== confirmPassword) {
        document.getElementById('error-message').textContent = 'Passwords do not match';
        document.getElementById('error-message').style.display = 'block';
        return;
    }

    try {
        const response = await fetch('/signup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        const result = await response.json();
        if (result.success) {
            window.location.href = result.redirect;
        } else {
            document.getElementById('error-message').textContent = result.error;
            document.getElementById('error-message').style.display = 'block';
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

async function handleContact(event) {
    event.preventDefault();
    
    const name = document.getElementById('name')?.value || '';
    const email = document.getElementById('email')?.value || '';
    const message = document.getElementById('message')?.value || '';

    try {
        const response = await fetch('/contact', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, email, message })
        });

        const result = await response.json();
        if (result.success) {
            alert('Message sent successfully!');
            event.target.reset();
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error sending message');
    }
}
