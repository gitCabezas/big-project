document.addEventListener('DOMContentLoaded', () => {
    // --- Login Page --- //
    const loginForm = document.querySelector('form');
    if (window.location.pathname.endsWith('index.html') || window.location.pathname.endsWith('/')) {
        if(loginForm) {
            loginForm.addEventListener('submit', (event) => {
                event.preventDefault();
                window.location.href = 'perfil.html';
            });
        }
    }

    // --- Receituário Page --- //
    if (window.location.pathname.endsWith('receituario.html')) {
        const recipeModal = document.getElementById('recipe-modal');
        const recipeButtons = document.querySelectorAll('.recipe-type-button');
        const closeButton = recipeModal.querySelector('.close-button');
        const alterRecipeButton = document.getElementById('alter-recipe-button');

        const costButton = document.getElementById('cost-button');
        const costDetails = document.getElementById('cost-details');
        const totalCostSpan = document.getElementById('total-cost');
        const costPerKgSpan = document.getElementById('cost-per-kg');

        if (costButton) {
            costButton.addEventListener('click', () => {
                if (costDetails.style.display === 'block') {
                    costDetails.style.display = 'none';
                } else {
                    // Simulate calculation
                    const totalCost = (Math.random() * 1000).toFixed(2);
                    const weight = parseFloat(document.getElementById('weight').value) || 1;
                    const costPerKg = (totalCost / weight).toFixed(2);

                    totalCostSpan.textContent = totalCost;
                    costPerKgSpan.textContent = costPerKg;
                    costDetails.style.display = 'block';
                }
            });
        }

        // Recipe Modals
        recipeButtons.forEach(button => {
            button.onclick = () => {
                const recipeType = button.dataset.recipe;
                const modalTitle = document.getElementById('recipe-modal-title');
                const modalBody = document.getElementById('recipe-modal-body');
                const tableBody = modalBody.querySelector('tbody');

                modalTitle.textContent = `Receita de ${recipeType.charAt(0).toUpperCase() + recipeType.slice(1)}`;
                let recipeTypeText = recipeType;
                if (recipeType === 'preparacao') {
                    recipeTypeText = 'preparação';
                } else if (recipeType === 'tingimento') {
                    recipeTypeText = 'tingimento';
                }
                alterRecipeButton.textContent = `Alterar receita de ${recipeTypeText}`; // Update button text

                // Clear previous table data
                tableBody.innerHTML = '';

                // Example data - replace with actual data fetching
                const data = [
                    { codigo: 'INS001', concentracao: '10%', insumo: 'Insumo A', quantidade: '100g', observacoes: 'Obs A' },
                    { codigo: 'INS002', concentracao: '5%', insumo: 'Insumo B', quantidade: '50ml', observacoes: 'Obs B' },
                    { codigo: 'INS003', concentracao: '20%', insumo: 'Insumo C', quantidade: '200g', observacoes: 'Obs C' },
                ];

                data.forEach(item => {
                    const row = tableBody.insertRow();
                    row.insertCell().textContent = item.codigo;
                    row.insertCell().textContent = item.concentracao;
                    row.insertCell().textContent = item.insumo;
                    row.insertCell().textContent = item.quantidade;
                    row.insertCell().textContent = item.observacoes;
                });

                recipeModal.style.display = 'block';
            };
        });

        // Close Modal
        if (closeButton) {
            closeButton.onclick = () => {
                recipeModal.style.display = 'none';
            };
        }

        // Close modals if user clicks outside of them
        window.onclick = (event) => {
            if (event.target == recipeModal) {
                recipeModal.style.display = 'none';
            }
        };
    }

    // --- Romaneio Page --- //
    if (window.location.pathname.endsWith('romaneio.html')) {
        const unitPriceInput = document.getElementById('shipping-unit-price');
        const weightInput = document.getElementById('shipping-weight');
        const subtotalInput = document.getElementById('shipping-subtotal');

        const calculateSubtotal = () => {
            const unitPrice = parseFloat(unitPriceInput.value) || 0;
            const weight = parseFloat(weightInput.value) || 0;
            const subtotal = (unitPrice * weight).toFixed(2);
            subtotalInput.value = `R$ ${subtotal}`;
        };

        unitPriceInput.addEventListener('input', calculateSubtotal);
        weightInput.addEventListener('input', calculateSubtotal);

        // Handle details button click
        const detailsButton = document.querySelector('.details-button');
        const detailsRow = document.querySelector('.details-row');

        if (detailsButton) {
            detailsButton.addEventListener('click', () => {
                if (detailsRow.style.display === 'none') {
                    detailsRow.style.display = 'table-row';
                } else {
                    detailsRow.style.display = 'none';
                }
            });
        }

        // Handle add buttons for weights
        const addFinishedWeightButton = document.querySelector('.add-finished-weight-button');
        const addNetWeightButton = document.querySelector('.add-net-weight-button');

        if (addFinishedWeightButton) {
            addFinishedWeightButton.addEventListener('click', () => {
                const newFinishedWeightInput = document.createElement('input');
                newFinishedWeightInput.type = 'number';
                newFinishedWeightInput.step = '0.01';
                newFinishedWeightInput.min = '0';
                newFinishedWeightInput.classList.add('finished-weight-input');
                const finishedWeightColumn = addFinishedWeightButton.closest('th').nextElementSibling.querySelector('td');
                finishedWeightColumn.appendChild(document.createElement('br'));
                finishedWeightColumn.appendChild(newFinishedWeightInput);
            });
        }

        if (addNetWeightButton) {
            addNetWeightButton.addEventListener('click', () => {
                const newNetWeightInput = document.createElement('input');
                newNetWeightInput.type = 'number';
                newNetWeightInput.step = '0.01';
                newNetWeightInput.min = '0';
                newNetWeightInput.classList.add('net-weight-input');
                const netWeightColumn = addNetWeightButton.closest('th').nextElementSibling.nextElementSibling.querySelector('td');
                netWeightColumn.appendChild(document.createElement('br'));
                netWeightColumn.appendChild(newNetWeightInput);
            });
        }
    }
});