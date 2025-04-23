// Arquivo JavaScript para integração de recursos visuais e iconografia

document.addEventListener('DOMContentLoaded', function() {
    // Inicialização de ícones SVG inline
    replaceIconsWithSVG();
    
    // Inicialização de gráficos com animações
    initializeCharts();
    
    // Adicionar efeitos visuais aos cards
    initializeCardEffects();
    
    // Inicializar tooltips para ícones
    initializeTooltips();
    
    // Inicializar modo escuro
    initializeDarkMode();
});

// Função para substituir ícones Bootstrap por SVG inline para melhor personalização
function replaceIconsWithSVG() {
    // Esta é uma versão simplificada. Em produção, você pode usar bibliotecas como Feather Icons
    document.querySelectorAll('.icon-replace').forEach(function(icon) {
        const iconName = icon.getAttribute('data-icon');
        if (!iconName) return;
        
        // Aqui você pode implementar a lógica para substituir por SVGs específicos
        // Este é apenas um exemplo simplificado
        icon.innerHTML = getIconSVG(iconName);
        icon.classList.add('icon-svg');
    });
}

// Função para obter SVG de ícone (exemplo simplificado)
function getIconSVG(iconName) {
    const icons = {
        'dashboard': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>',
        'finance': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>',
        'inventory': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg>',
        'sales': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>',
        'hr': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>'
    };
    
    return icons[iconName] || '';
}

// Inicialização de gráficos com animações
function initializeCharts() {
    const chartElements = document.querySelectorAll('.chart-container');
    chartElements.forEach(function(container) {
        const canvas = container.querySelector('canvas');
        if (!canvas || typeof Chart === 'undefined') return;
        
        const chartType = container.getAttribute('data-chart-type') || 'bar';
        const chartData = JSON.parse(container.getAttribute('data-chart-data') || '{}');
        
        // Adicionar animações aos gráficos
        const options = {
            responsive: true,
            maintainAspectRatio: false,
            animation: {
                duration: 2000,
                easing: 'easeOutQuart'
            },
            plugins: {
                legend: {
                    position: 'top',
                    labels: {
                        boxWidth: 15,
                        usePointStyle: true,
                        pointStyle: 'circle'
                    }
                },
                tooltip: {
                    backgroundColor: 'rgba(0, 0, 0, 0.7)',
                    titleFont: {
                        size: 13
                    },
                    bodyFont: {
                        size: 12
                    },
                    padding: 10,
                    cornerRadius: 5,
                    displayColors: true
                }
            }
        };
        
        // Personalizar opções com base no tipo de gráfico
        if (chartType === 'line') {
            options.elements = {
                line: {
                    tension: 0.4 // Curva suave para linhas
                },
                point: {
                    radius: 4,
                    hoverRadius: 6
                }
            };
        } else if (chartType === 'doughnut' || chartType === 'pie') {
            options.cutout = '60%';
            options.plugins.tooltip = {
                ...options.plugins.tooltip,
                callbacks: {
                    label: function(context) {
                        const label = context.label || '';
                        const value = context.formattedValue;
                        const total = context.dataset.data.reduce((a, b) => a + b, 0);
                        const percentage = Math.round((context.raw / total) * 100);
                        return `${label}: ${value} (${percentage}%)`;
                    }
                }
            };
        }
        
        new Chart(canvas, {
            type: chartType,
            data: chartData,
            options: options
        });
    });
}

// Adicionar efeitos visuais aos cards
function initializeCardEffects() {
    // Efeito de elevação ao passar o mouse
    document.querySelectorAll('.card').forEach(function(card) {
        card.addEventListener('mouseenter', function() {
            if (window.matchMedia('(prefers-reduced-motion: no-preference)').matches) {
                this.style.transform = 'translateY(-5px)';
                this.style.boxShadow = '0 10px 20px rgba(0,0,0,0.1)';
            }
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = '';
            this.style.boxShadow = '';
        });
    });
    
    // Efeito de destaque para cards estatísticos
    document.querySelectorAll('.stat-card').forEach(function(card) {
        card.addEventListener('mouseenter', function() {
            if (window.matchMedia('(prefers-reduced-motion: no-preference)').matches) {
                const icon = this.querySelector('.stat-icon');
                if (icon) {
                    icon.style.transform = 'scale(1.2)';
                }
            }
        });
        
        card.addEventListener('mouseleave', function() {
            const icon = this.querySelector('.stat-icon');
            if (icon) {
                icon.style.transform = '';
            }
        });
    });
}

// Inicializar tooltips para ícones
function initializeTooltips() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl, {
            delay: { show: 500, hide: 100 },
            boundary: document.body
        });
    });
}

// Inicializar modo escuro
function initializeDarkMode() {
    const darkModeToggle = document.getElementById('darkModeToggle');
    if (!darkModeToggle) return;
    
    // Verificar preferência do sistema
    const prefersDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    // Verificar configuração salva
    const savedMode = localStorage.getItem('darkMode');
    
    // Aplicar modo escuro se necessário
    if (savedMode === 'dark' || (savedMode === null && prefersDarkMode)) {
        document.body.classList.add('dark-mode');
        darkModeToggle.checked = true;
    }
    
    // Alternar modo escuro ao clicar no toggle
    darkModeToggle.addEventListener('change', function() {
        if (this.checked) {
            document.body.classList.add('dark-mode');
            localStorage.setItem('darkMode', 'dark');
        } else {
            document.body.classList.remove('dark-mode');
            localStorage.setItem('darkMode', 'light');
        }
    });
}

// Função para criar gráficos de progresso circular
function createCircularProgress(elementId, percentage, color) {
    const element = document.getElementById(elementId);
    if (!element) return;
    
    const radius = 40;
    const circumference = 2 * Math.PI * radius;
    const dashoffset = circumference * (1 - percentage / 100);
    
    element.innerHTML = `
        <svg class="circular-progress" width="120" height="120" viewBox="0 0 120 120">
            <circle class="circular-progress-bg" cx="60" cy="60" r="${radius}" stroke="#e6e6e6" stroke-width="8" fill="none" />
            <circle class="circular-progress-bar" cx="60" cy="60" r="${radius}" stroke="${color}" stroke-width="8" fill="none" 
                    stroke-dasharray="${circumference}" stroke-dashoffset="${dashoffset}" 
                    transform="rotate(-90 60 60)" />
            <text x="60" y="65" text-anchor="middle" fill="currentColor" font-size="20" font-weight="bold">${percentage}%</text>
        </svg>
    `;
    
    // Animar o progresso
    if (window.matchMedia('(prefers-reduced-motion: no-preference)').matches) {
        const progressBar = element.querySelector('.circular-progress-bar');
        progressBar.style.transition = 'stroke-dashoffset 1.5s ease-in-out';
        progressBar.style.strokeDashoffset = circumference;
        
        setTimeout(() => {
            progressBar.style.strokeDashoffset = dashoffset;
        }, 100);
    }
}

// Função para criar gráficos de progresso linear
function createLinearProgress(elementId, percentage, color) {
    const element = document.getElementById(elementId);
    if (!element) return;
    
    element.innerHTML = `
        <div class="linear-progress-container">
            <div class="linear-progress-label">${percentage}%</div>
            <div class="linear-progress-bar-bg">
                <div class="linear-progress-bar" style="width: 0%; background-color: ${color};"></div>
            </div>
        </div>
    `;
    
    // Animar o progresso
    if (window.matchMedia('(prefers-reduced-motion: no-preference)').matches) {
        const progressBar = element.querySelector('.linear-progress-bar');
        progressBar.style.transition = 'width 1s ease-in-out';
        
        setTimeout(() => {
            progressBar.style.width = `${percentage}%`;
        }, 100);
    } else {
        element.querySelector('.linear-progress-bar').style.width = `${percentage}%`;
    }
}

// Função para adicionar contador animado
function createAnimatedCounter(elementId, targetValue, prefix = '', suffix = '', duration = 2000) {
    const element = document.getElementById(elementId);
    if (!element) return;
    
    let startTime;
    const startValue = 0;
    
    function updateCounter(timestamp) {
        if (!startTime) startTime = timestamp;
        
        const progress = Math.min((timestamp - startTime) / duration, 1);
        const currentValue = Math.floor(progress * (targetValue - startValue) + startValue);
        
        element.textContent = `${prefix}${currentValue.toLocaleString()}${suffix}`;
        
        if (progress < 1) {
            requestAnimationFrame(updateCounter);
        } else {
            element.textContent = `${prefix}${targetValue.toLocaleString()}${suffix}`;
        }
    }
    
    if (window.matchMedia('(prefers-reduced-motion: no-preference)').matches) {
        requestAnimationFrame(updateCounter);
    } else {
        element.textContent = `${prefix}${targetValue.toLocaleString()}${suffix}`;
    }
}

// Exportar funções para uso global
window.ERP = {
    createCircularProgress,
    createLinearProgress,
    createAnimatedCounter
};
