(function () {
    function initMobileNavigation() {
        const headerContainer = document.querySelector('.main-header .header-container');
        const nav = document.querySelector('.main-nav');

        if (!headerContainer || !nav) {
            return;
        }

        let toggle = headerContainer.querySelector('.mobile-nav-toggle');
        if (!toggle) {
            toggle = document.createElement('button');
            toggle.className = 'mobile-nav-toggle';
            toggle.type = 'button';
            toggle.setAttribute('aria-label', 'Открыть меню');
            toggle.setAttribute('aria-expanded', 'false');
            toggle.innerHTML = '<span></span><span></span><span></span>';
            headerContainer.appendChild(toggle);
        }

        let overlay = document.querySelector('.nav-overlay');
        if (!overlay) {
            overlay = document.createElement('div');
            overlay.className = 'nav-overlay';
            document.body.appendChild(overlay);
        }

        const closeNav = () => {
            if (!document.body.classList.contains('nav-open')) {
                return;
            }
            document.body.classList.remove('nav-open');
            toggle.setAttribute('aria-expanded', 'false');
        };

        const openNav = () => {
            if (document.body.classList.contains('nav-open')) {
                return;
            }
            document.body.classList.add('nav-open');
            toggle.setAttribute('aria-expanded', 'true');
        };

        toggle.addEventListener('click', () => {
            if (document.body.classList.contains('nav-open')) {
                closeNav();
            } else {
                openNav();
            }
        });

        overlay.addEventListener('click', closeNav);

        document.addEventListener('keydown', (event) => {
            if (event.key === 'Escape') {
                closeNav();
            }
        });

        nav.querySelectorAll('a').forEach((link) => {
            link.addEventListener('click', closeNav);
        });

        nav.querySelectorAll('.dropdown > a').forEach((trigger) => {
            trigger.addEventListener('click', (event) => {
                if (window.innerWidth > 1024) {
                    return;
                }
                event.preventDefault();
                const dropdown = trigger.closest('.dropdown');
                dropdown.classList.toggle('dropdown-open');
            });
        });

        window.addEventListener('resize', () => {
            if (window.innerWidth > 1024) {
                closeNav();
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initMobileNavigation);
    } else {
        initMobileNavigation();
    }
})();


