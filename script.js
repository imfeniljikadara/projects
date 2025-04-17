document.addEventListener('DOMContentLoaded', () => {
    // Theme toggle functionality with improved visual feedback
    const themeToggle = document.getElementById('theme-toggle');
    const themeIcon = themeToggle.querySelector('i');
    const navbar = document.querySelector('nav');
    const nameElement = document.querySelector('.hero h1');
    const navLinks = document.querySelector('.nav-links');
    
    // Mobile navigation functionality
    function setupMobileNav() {
        // Create mobile nav toggle button
        const mobileNavToggle = document.createElement('button');
        mobileNavToggle.className = 'mobile-nav-toggle';
        mobileNavToggle.innerHTML = '<i class="fas fa-bars"></i>';
        mobileNavToggle.setAttribute('aria-label', 'Toggle navigation menu');
        
        // Create a container for the toggle buttons on the right side
        const toggleContainer = document.createElement('div');
        toggleContainer.className = 'toggle-container';
        
        // Move the theme toggle into the container
        const parentNode = themeToggle.parentNode;
        parentNode.removeChild(themeToggle);
        toggleContainer.appendChild(themeToggle);
        toggleContainer.appendChild(mobileNavToggle);
        
        // Add the container to the navbar
        navbar.appendChild(toggleContainer);
        
        // Hide nav links by default on mobile
        if (window.innerWidth <= 768) {
            navLinks.style.display = 'none';
        }
        
        // Toggle nav links visibility
        mobileNavToggle.addEventListener('click', function() {
            if (navLinks.style.display === 'none' || navLinks.style.display === '') {
                navLinks.style.display = 'flex';
                document.body.classList.add('nav-open');
                mobileNavToggle.innerHTML = '<i class="fas fa-times"></i>';
            } else {
                navLinks.style.display = 'none';
                document.body.classList.remove('nav-open');
                mobileNavToggle.innerHTML = '<i class="fas fa-bars"></i>';
            }
        });
        
        // Close menu when a link is clicked
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth <= 768) {
                    navLinks.style.display = 'none';
                    document.body.classList.remove('nav-open');
                    mobileNavToggle.innerHTML = '<i class="fas fa-bars"></i>';
                }
            });
        });
        
        // Adjust display on resize
        window.addEventListener('resize', () => {
            if (window.innerWidth > 768) {
                navLinks.style.display = 'flex';
                document.body.classList.remove('nav-open');
            } else if (navLinks.style.display !== 'flex') {
                navLinks.style.display = 'none';
                document.body.classList.remove('nav-open');
            }
        });
    }
    
    setupMobileNav();
    
    // Add screen reader only class if not present
    if (!document.querySelector('.sr-only')) {
        const style = document.createElement('style');
        style.textContent = '.sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0, 0, 0, 0); white-space: nowrap; border-width: 0; }';
        document.head.appendChild(style);
    }
    
    // Check for saved theme preference or use preferred color scheme
    const savedTheme = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    // Apply theme based on saved preference or system preference
    if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
        document.body.classList.add('dark-theme');
        themeIcon.classList.remove('fa-moon');
        themeIcon.classList.add('fa-sun');
        themeToggle.setAttribute('title', 'Switch to light mode');
    } else {
        themeToggle.setAttribute('title', 'Switch to dark mode');
    }
    
    // Add a ripple effect to the theme toggle button
    themeToggle.addEventListener('click', function(e) {
        // Create ripple effect
        const ripple = document.createElement('span');
        ripple.classList.add('ripple');
        this.appendChild(ripple);
        
        // Position the ripple
        const rect = this.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        ripple.style.width = ripple.style.height = `${size}px`;
        ripple.style.left = `${e.clientX - rect.left - size/2}px`;
        ripple.style.top = `${e.clientY - rect.top - size/2}px`;
        
        // Toggle theme
        document.body.classList.toggle('dark-theme');
        
        // Update icon and title
        if (document.body.classList.contains('dark-theme')) {
            themeIcon.classList.remove('fa-moon');
            themeIcon.classList.add('fa-sun');
            localStorage.setItem('theme', 'dark');
            themeToggle.setAttribute('title', 'Switch to light mode');
        } else {
            themeIcon.classList.remove('fa-sun');
            themeIcon.classList.add('fa-moon');
            localStorage.setItem('theme', 'light');
            themeToggle.setAttribute('title', 'Switch to dark mode');
        }
        
        // Remove ripple after animation completes
        setTimeout(() => {
            ripple.remove();
        }, 600);
    });
    
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Add animation to sections when they come into view
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = 1;
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Apply initial styles and observe all sections
    document.querySelectorAll('.section').forEach(section => {
        section.style.opacity = 0;
        section.style.transform = 'translateY(20px)';
        section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(section);
    });
    
    // Apply similar animation to experience and project items
    const itemsToAnimate = document.querySelectorAll('.experience-item, .project-item, .contribution-item, .leadership-item');
    itemsToAnimate.forEach((item, index) => {
        item.style.opacity = 0;
        item.style.transform = 'translateY(20px)';
        item.style.transition = `opacity 0.6s ease ${index * 0.1}s, transform 0.6s ease ${index * 0.1}s`;
        observer.observe(item);
    });
    
    // Navbar scroll behavior
    window.addEventListener('scroll', () => {
        if (window.scrollY > 100) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
});
