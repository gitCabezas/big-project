document.addEventListener('DOMContentLoaded', () => {
    const unitPriceInput = document.getElementById('shipping-unit-price');
    const weightInput = document.getElementById('shipping-weight');
    const subtotalInput = document.getElementById('shipping-subtotal');

    const calculateSubtotal = () => {
        const unitPrice = parseFloat(unitPriceInput.value) || 0;
        const weight = parseFloat(weightInput.value) || 0;
        const subtotal = (unitPrice * weight).toFixed(2);
        subtotalInput.value = `R$ ${subtotal}`;
    };

    // Only add event listeners if the elements exist
    if (unitPriceInput && weightInput && subtotalInput) {
        unitPriceInput.addEventListener('input', calculateSubtotal);
        weightInput.addEventListener('input', calculateSubtotal);
    }

    // Handle details button click
    const detailsButton = document.querySelector('.details-button');
    const detailsRow = document.querySelector('.details-row');
    const addDetailRowButton = document.querySelector('.add-detail-row-button');

    if (detailsButton && detailsRow) {
        detailsButton.addEventListener('click', () => {
            detailsRow.classList.toggle('hidden-row');
        });
    }

    if (addDetailRowButton && detailsRow) {
        const detailsTableBody = detailsRow.querySelector('.details-table-container tbody');
        if (detailsTableBody) {
            if (addDetailRowButton) {
            addDetailRowButton.addEventListener('click', () => {
                const newRow = document.createElement('tr');
                newRow.innerHTML = `
                    <td><input type="number" class="raw-weight-input" step="0.01" min="0"></td>
                    <td><input type="number" class="finished-weight-input" step="0.01" min="0"></td>
                    <td><input type="number" class="net-weight-input" step="0.01" min="0"></td>
                `;
                detailsTableBody.appendChild(newRow);
            });
        }

        const removeDetailRowButton = document.querySelector('.remove-detail-row-button');
        if (removeDetailRowButton && detailsRow) {
            const detailsTableBody = detailsRow.querySelector('.details-table-container tbody');
            if (detailsTableBody) {
                removeDetailRowButton.addEventListener('click', () => {
                    const rows = detailsTableBody.querySelectorAll('tr');
                    if (rows.length > 1) { // Ensure we don't remove the initial row
                        detailsTableBody.removeChild(rows[rows.length - 1]);
                    }
                });
            }
        }
        }
    }
});