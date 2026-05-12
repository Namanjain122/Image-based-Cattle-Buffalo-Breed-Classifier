// ========================================
// Particle Animation
// ========================================
function createParticles() {
    const container = document.getElementById('particles');
    const particleCount = 50;

    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.top = Math.random() * 100 + '%';
        particle.style.animationDuration = (15 + Math.random() * 20) + 's';
        particle.style.animationDelay = Math.random() * 5 + 's';
        container.appendChild(particle);
    }
}

// ========================================
// File Upload Functionality
// ========================================
const uploadBox = document.getElementById('uploadBox');
const fileInput = document.getElementById('fileInput');
const folderInput = document.getElementById('folderInput');
const fileList = document.getElementById('fileList');
const uploadForm = document.querySelector('.upload-form');
const submitBtn = document.getElementById('submitBtn');
const loadingOverlay = document.getElementById('loadingOverlay');

let selectedFiles = [];

// Click to upload
uploadBox.addEventListener('click', (e) => {
    if (e.shiftKey) {
        folderInput.click();   // SHIFT + click → choose folder
    } else {
        fileInput.click();     // normal click → choose images
    }

});

// Drag and drop
uploadBox.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadBox.classList.add('dragging');
});

uploadBox.addEventListener('dragleave', () => {
    uploadBox.classList.remove('dragging');
});

uploadBox.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadBox.classList.remove('dragging');
    
    const files = Array.from(e.dataTransfer.files).filter(file => 
        file.type.startsWith('image/')
    );
    
    handleFiles(files);
});

// File input change
fileInput.addEventListener('change', (e) => {
    const files = Array.from(e.target.files).filter(file => 
        file.type.startsWith('image/')
    );
    
    handleFiles(files);
});
folderInput.addEventListener('change', (e) => {

    const files = Array.from(e.target.files).filter(file =>
        file.type.startsWith('image/')
    );

    handleFiles(files);

});
function handleFiles(files) {
    selectedFiles = [...selectedFiles, ...files];
    displayFileList();
}

function displayFileList() {

    fileList.innerHTML = '';

    if (selectedFiles.length === 0) {
        fileList.innerHTML = '<div class="empty-state">No files selected</div>';
        submitBtn.disabled = true;
        return;
    }

    submitBtn.disabled = false;

    selectedFiles.forEach((file, index) => {

        const fileItem = document.createElement('div');

        fileItem.className = 'file-item';

        fileItem.innerHTML = `
            <span class="file-item-name">📄 ${file.name}</span>
            <button type="button" class="file-item-remove" onclick="removeFile(${index})">Remove</button>
        `;

        fileList.appendChild(fileItem);

    });

}

function removeFile(index) {
    selectedFiles.splice(index, 1);
    displayFileList();
}

// Form submission
uploadForm.addEventListener('submit', (e) => {
    if (selectedFiles.length === 0) {
        e.preventDefault();
        alert('Please select at least one image');
    } else {
        // Create FormData and add files
        const formData = new FormData(uploadForm);
        formData.delete('files');
        selectedFiles.forEach(file => {
            formData.append('files', file);
        });

        // Replace form data
        const newForm = new FormData();
        selectedFiles.forEach(file => {
            newForm.append('files', file);
        });

        // Show loading
        loadingOverlay.classList.add('active');

        // Note: Form will naturally submit, so we let the browser handle it
        // The loading overlay will persist during page reload
    }
});

// ========================================
// Loading Simulation
// ========================================
function simulateLoading() {
    const progressFill = document.querySelector('.progress-fill');
    let progress = 0;
    
    const interval = setInterval(() => {
        progress += Math.random() * 30;
        if (progress > 100) progress = 100;
        
        progressFill.style.width = progress + '%';
        
        if (progress >= 100) {
            clearInterval(interval);
        }
    }, 500);
}

// ========================================
// Smooth Scroll Navigation
// ========================================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
        e.preventDefault();
        const target = document.querySelector(anchor.getAttribute('href'));
        
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ========================================
// Navbar Shadow on Scroll
// ========================================
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    if (window.scrollY > 10) {
        navbar.style.boxShadow = '0 10px 30px rgba(0, 212, 255, 0.2)';
    } else {
        navbar.style.boxShadow = 'none';
    }
});

// ========================================
// Intersection Observer for Animations
// ========================================
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe feature cards
document.querySelectorAll('.feature-card').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(card);
});

// Observe result cards
document.querySelectorAll('.result-card').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(card);
});

// ========================================
// Mouse Trail Effect
// ========================================
let mouseX = 0;
let mouseY = 0;

document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
});

// ========================================
// Confidence Meter Animation
// ========================================
function animateConfidenceBars() {
    const bars = document.querySelectorAll('.confidence-fill');
    
    bars.forEach((bar) => {
        const width = bar.style.width;
        bar.style.width = '0%';
        
        setTimeout(() => {
            bar.style.width = width;
        }, 100);
    });
}

// ========================================
// Results Display Enhancement
// ========================================
window.addEventListener('load', () => {
    // Scroll to results if they exist
    const resultsSection = document.getElementById('results');
    if (resultsSection && resultsSection.style.display !== 'none') {
        setTimeout(() => {
            resultsSection.scrollIntoView({ behavior: 'smooth' });
            animateConfidenceBars();
        }, 500);
    }
    
    // Hide loading overlay if it was shown
    if (loadingOverlay.classList.contains('active')) {
        loadingOverlay.classList.remove('active');
    }
});

// ========================================
// Initialize
// ========================================
document.addEventListener('DOMContentLoaded', () => {
    createParticles();
    displayFileList();
});

// ========================================
// Ripple Effect on Buttons
// ========================================
document.querySelectorAll('.submit-btn, .reset-btn, .hero-btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
        const ripple = document.createElement('span');
        const rect = this.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = e.clientX - rect.left - size / 2;
        const y = e.clientY - rect.top - size / 2;

        ripple.style.width = ripple.style.height = size + 'px';
        ripple.style.left = x + 'px';
        ripple.style.top = y + 'px';
        ripple.style.position = 'absolute';
        ripple.style.background = 'rgba(255, 255, 255, 0.5)';
        ripple.style.borderRadius = '50%';
        ripple.style.transform = 'scale(0)';
        ripple.style.animation = 'rippleEffect 0.6s ease-out';
        ripple.style.pointerEvents = 'none';

        if (this.style.position !== 'relative' && this.style.position !== 'absolute') {
            this.style.position = 'relative';
        }
        this.style.overflow = 'hidden';
        this.appendChild(ripple);

        setTimeout(() => ripple.remove(), 600);
    });
});

// Add ripple animation
const styleSheet = document.createElement('style');
styleSheet.textContent = `
    @keyframes rippleEffect {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(styleSheet);

// ========================================
// Console Welcome Message
// ========================================
console.log('%c🔬 LiveStock AI', 'font-size: 20px; font-weight: bold; color: #00d4ff;');
console.log('%cAdvanced Livestock Breed Detection System', 'font-size: 12px; color: #7c3aed;');
