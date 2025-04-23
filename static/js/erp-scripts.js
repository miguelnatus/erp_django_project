// Arquivo JavaScript principal para o Sistema ERP

document.addEventListener('DOMContentLoaded', function() {
    // Toggle para o menu lateral em dispositivos móveis
    const sidebarToggle = document.getElementById('sidebarToggle');
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('mainContent');
    
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function() {
            sidebar.classList.toggle('show');
            mainContent.classList.toggle('sidebar-open');
        });
    }
    
    // Inicialização de tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Inicialização de popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
    
    // Animação para elementos com classe fade-in
    const fadeElements = document.querySelectorAll('.fade-in');
    fadeElements.forEach(function(element, index) {
        setTimeout(function() {
            element.classList.add('show');
        }, 100 * index);
    });
    
    // Dropdown menus na sidebar
    const dropdownItems = document.querySelectorAll('.sidebar .nav-item.dropdown');
    dropdownItems.forEach(function(item) {
        const link = item.querySelector('.dropdown-toggle');
        const menu = item.querySelector('.dropdown-menu');
        
        link.addEventListener('click', function(e) {
            e.preventDefault();
            menu.classList.toggle('show');
        });
    });
    
    // Fechar alertas automaticamente após 5 segundos
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const closeButton = alert.querySelector('.btn-close');
            if (closeButton) {
                closeButton.click();
            } else {
                alert.classList.add('fade-out');
                setTimeout(function() {
                    alert.remove();
                }, 500);
            }
        }, 5000);
    });
    
    // Tabelas com ordenação
    const sortableTables = document.querySelectorAll('.table-sortable');
    sortableTables.forEach(function(table) {
        const headers = table.querySelectorAll('th.sortable');
        headers.forEach(function(header) {
            header.addEventListener('click', function() {
                const isAscending = !header.classList.contains('sort-asc');
                
                // Remover classes de ordenação de todos os cabeçalhos
                headers.forEach(h => {
                    h.classList.remove('sort-asc', 'sort-desc');
                });
                
                // Adicionar classe de ordenação ao cabeçalho clicado
                header.classList.add(isAscending ? 'sort-asc' : 'sort-desc');
                
                // Ordenar a tabela
                const columnIndex = Array.from(header.parentNode.children).indexOf(header);
                sortTable(table, columnIndex, isAscending);
            });
        });
    });
    
    // Função para ordenar tabela
    function sortTable(table, columnIndex, ascending) {
        const tbody = table.querySelector('tbody');
        const rows = Array.from(tbody.querySelectorAll('tr'));
        
        rows.sort(function(a, b) {
            const aValue = a.children[columnIndex].textContent.trim();
            const bValue = b.children[columnIndex].textContent.trim();
            
            // Verificar se os valores são números
            const aNum = parseFloat(aValue);
            const bNum = parseFloat(bValue);
            
            if (!isNaN(aNum) && !isNaN(bNum)) {
                return ascending ? aNum - bNum : bNum - aNum;
            }
            
            // Ordenação de texto
            return ascending 
                ? aValue.localeCompare(bValue) 
                : bValue.localeCompare(aValue);
        });
        
        // Reordenar as linhas na tabela
        rows.forEach(function(row) {
            tbody.appendChild(row);
        });
    }
    
    // Inicialização de datepickers
    const datepickers = document.querySelectorAll('.datepicker');
    datepickers.forEach(function(input) {
        // Aqui você pode adicionar a inicialização de um plugin de datepicker
        // Por exemplo, se estiver usando Flatpickr:
        // flatpickr(input, {
        //     dateFormat: "d/m/Y",
        //     locale: "pt"
        // });
    });
    
    // Máscaras para inputs
    const maskedInputs = document.querySelectorAll('[data-mask]');
    maskedInputs.forEach(function(input) {
        const maskType = input.getAttribute('data-mask');
        
        // Aqui você pode adicionar a inicialização de um plugin de máscara
        // Por exemplo, se estiver usando IMask:
        // let maskOptions;
        // switch(maskType) {
        //     case 'cpf':
        //         maskOptions = {mask: '000.000.000-00'};
        //         break;
        //     case 'cnpj':
        //         maskOptions = {mask: '00.000.000/0000-00'};
        //         break;
        //     case 'phone':
        //         maskOptions = {mask: '(00) 00000-0000'};
        //         break;
        //     case 'cep':
        //         maskOptions = {mask: '00000-000'};
        //         break;
        // }
        // if (maskOptions) {
        //     IMask(input, maskOptions);
        // }
    });
    
    // Confirmação para ações de exclusão
    const deleteButtons = document.querySelectorAll('[data-confirm]');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            const message = button.getAttribute('data-confirm') || 'Tem certeza que deseja excluir este item?';
            if (!confirm(message)) {
                e.preventDefault();
            }
        });
    });
    
    // Inicialização de select2 para selects avançados
    const select2Elements = document.querySelectorAll('.select2');
    if (typeof $.fn.select2 !== 'undefined') {
        $(select2Elements).select2({
            theme: 'bootstrap-5',
            width: '100%'
        });
    }
    
    // Gráficos de dashboard (exemplo com Chart.js)
    const chartElements = document.querySelectorAll('.chart-container');
    chartElements.forEach(function(container) {
        const canvas = container.querySelector('canvas');
        if (!canvas || typeof Chart === 'undefined') return;
        
        const chartType = container.getAttribute('data-chart-type') || 'bar';
        const chartData = JSON.parse(container.getAttribute('data-chart-data') || '{}');
        
        new Chart(canvas, {
            type: chartType,
            data: chartData,
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        });
    });
});

// Funções utilitárias
function formatCurrency(value) {
    return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    }).format(value);
}

function formatDate(dateString) {
    const date = new Date(dateString);
    return new Intl.DateTimeFormat('pt-BR').format(date);
}

function formatDateTime(dateTimeString) {
    const date = new Date(dateTimeString);
    return new Intl.DateTimeFormat('pt-BR', {
        dateStyle: 'short',
        timeStyle: 'short'
    }).format(date);
}

// Função para mostrar/esconder loader
function toggleLoader(show = true) {
    const loader = document.getElementById('pageLoader');
    if (!loader) return;
    
    if (show) {
        loader.classList.remove('d-none');
    } else {
        loader.classList.add('d-none');
    }
}

// Função para mostrar notificações toast
function showToast(message, type = 'success') {
    const toastContainer = document.getElementById('toastContainer');
    if (!toastContainer) return;
    
    const toast = document.createElement('div');
    toast.className = `toast toast-${type} fade-in`;
    toast.setAttribute('role', 'alert');
    toast.setAttribute('aria-live', 'assertive');
    toast.setAttribute('aria-atomic', 'true');
    
    toast.innerHTML = `
        <div class="toast-header">
            <strong class="me-auto">${type.charAt(0).toUpperCase() + type.slice(1)}</strong>
            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
        <div class="toast-body">
            ${message}
        </div>
    `;
    
    toastContainer.appendChild(toast);
    
    const bsToast = new bootstrap.Toast(toast);
    bsToast.show();
    
    toast.addEventListener('hidden.bs.toast', function() {
        toast.remove();
    });
}
