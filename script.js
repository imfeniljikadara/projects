document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('theme-toggle');
    const themeIcon = themeToggle.querySelector('i');
    const navToggle = document.getElementById('nav-toggle');
    const navLinks = document.getElementById('nav-links');

    /* ---------------------------------------------------------------- theme */

    const setTheme = (dark) => {
        document.body.classList.toggle('dark-theme', dark);
        themeIcon.classList.toggle('ph-moon-stars', !dark);
        themeIcon.classList.toggle('ph-sun-dim', dark);
        themeToggle.setAttribute('title', dark ? 'Switch to light mode' : 'Switch to dark mode');
    };

    /* Light is the default; dark only when the visitor has asked for it here. */
    setTheme(localStorage.getItem('theme') === 'dark');

    themeToggle.addEventListener('click', () => {
        const dark = !document.body.classList.contains('dark-theme');
        setTheme(dark);
        localStorage.setItem('theme', dark ? 'dark' : 'light');
    });

    /* ----------------------------------------------------------- mobile nav */

    const closeNav = () => {
        navLinks.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
        navToggle.querySelector('i').className = 'ph ph-list';
    };

    navToggle.addEventListener('click', () => {
        const open = navLinks.classList.toggle('open');
        navToggle.setAttribute('aria-expanded', String(open));
        navToggle.querySelector('i').className = open ? 'ph ph-x' : 'ph ph-list';
    });

    navLinks.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeNav));
    window.addEventListener('resize', () => {
        if (window.innerWidth > 860) closeNav();
    });

    /* ------------------------------------------------------ reveal on scroll */

    const revealTargets = document.querySelectorAll(
        '.section-head, .about-text, .about-grid, .stats, .experience-item, .project-item, .contribution-item, .leadership-item, .achievements-list, .contact .frame > *'
    );

    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (!entry.isIntersecting) return;
            entry.target.classList.add('is-visible');
            revealObserver.unobserve(entry.target);
        });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });

    revealTargets.forEach((el, i) => {
        el.classList.add('reveal');
        el.style.transitionDelay = `${Math.min(i % 6, 5) * 60}ms`;
        revealObserver.observe(el);
    });

    /* --------------------------------------------------------- nav scrollspy */

    const links = [...navLinks.querySelectorAll('a')];
    const sections = links
        .map((link) => document.querySelector(link.getAttribute('href')))
        .filter(Boolean);

    const spy = () => {
        const marker = window.scrollY + window.innerHeight * 0.3;
        let current = null;

        sections.forEach((section) => {
            if (section.offsetTop <= marker) current = section;
        });

        links.forEach((link) => {
            link.classList.toggle('active', current !== null && link.getAttribute('href') === `#${current.id}`);
        });
    };

    let ticking = false;
    window.addEventListener('scroll', () => {
        if (ticking) return;
        ticking = true;
        window.requestAnimationFrame(() => {
            spy();
            ticking = false;
        });
    }, { passive: true });

    spy();
});
