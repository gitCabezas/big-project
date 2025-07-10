document.addEventListener('DOMContentLoaded', () => {
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
});