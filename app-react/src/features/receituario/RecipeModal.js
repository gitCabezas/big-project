import React from 'react';

const RecipeModal = ({ recipeType, show, onClose }) => {
    if (!show) {
        return null;
    }

    const data = [
        { codigo: 'INS001', concentracao: '10%', insumo: 'Insumo A', quantidade: '100g', observacoes: 'Obs A' },
        { codigo: 'INS002', concentracao: '5%', insumo: 'Insumo B', quantidade: '50ml', observacoes: 'Obs B' },
        { codigo: 'INS003', concentracao: '20%', insumo: 'Insumo C', quantidade: '200g', observacoes: 'Obs C' },
    ];

    let recipeTypeText = recipeType;
    if (recipeType === 'preparacao') {
        recipeTypeText = 'preparação';
    } else if (recipeType === 'tingimento') {
        recipeTypeText = 'tingimento';
    }

    return (
        <div className="modal">
            <div className="modal-content">
                <div className="modal-header">
                    <button className="alter-recipe-button">Alterar receita de {recipeTypeText}</button>
                    <span className="close-button" onClick={onClose}>&times;</span>
                </div>
                <h3>Receita de {recipeType.charAt(0).toUpperCase() + recipeType.slice(1)}</h3>
                <div className="modal-body">
                    <table>
                        <thead>
                            <tr>
                                <th>Código de insumo</th>
                                <th>Concentração</th>
                                <th>Insumo</th>
                                <th>Quantidade</th>
                                <th>Observações</th>
                            </tr>
                        </thead>
                        <tbody>
                            {data.map((item, index) => (
                                <tr key={index}>
                                    <td>{item.codigo}</td>
                                    <td>{item.concentracao}</td>
                                    <td>{item.insumo}</td>
                                    <td>{item.quantidade}</td>
                                    <td>{item.observacoes}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    );
};

export default RecipeModal;