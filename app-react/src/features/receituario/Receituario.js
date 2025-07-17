import React, { useState } from 'react';
import Navbar from '../../common/components/Navbar/Navbar';
import './Receituario.css';
import RecipeModal from './RecipeModal';

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

const Receituario = () => {
    const [showCost, setShowCost] = useState(false);
    const [totalCost, setTotalCost] = useState(0);
    const [costPerKg, setCostPerKg] = useState(0);
    const [weight, setWeight] = useState(1);
    const [modalInfo, setModalInfo] = useState({ show: false, recipeType: '' });

    const handleCostClick = () => {
        if (showCost) {
            setShowCost(false);
        } else {
            const randomCost = (Math.random() * 1000).toFixed(2);
            setTotalCost(randomCost);
            setCostPerKg((randomCost / weight).toFixed(2));
            setShowCost(true);
        }
    };

    const handleRecipeButtonClick = (recipeType) => {
        setModalInfo({ show: true, recipeType });
    };

    const closeModal = () => {
        setModalInfo({ show: false, recipeType: '' });
    };

    return (
        <main>
            <Navbar />
            <div className="recipe-container">
                
                <form>
                    <div className="form-grid">
                        <div className="input-group">
                            <label htmlFor="recipe-name">Nome da Receita</label>
                            <input type="text" id="recipe-name" name="recipe-name" />
                        </div>
                        <div className="input-group">
                            <label htmlFor="client">Cliente</label>
                            <input type="text" id="client" name="client" />
                        </div>
                        <div className="input-group">
                            <label htmlFor="article">Artigo</label>
                            <input type="text" id="article" name="article" />
                        </div>
                        <div className="input-group">
                            <label htmlFor="processo">Processo</label>
                            <input type="text" id="processo" name="processo" />
                        </div>
                        <div className="input-group">
                            <label htmlFor="substrato">Substrato</label>
                            <input type="text" id="substrato" name="substrato" />
                        </div>
                        <div className="input-group">
                            <label htmlFor="maquina">Máquina</label>
                            <select id="maquina" name="maquina">
                                <option value="">Selecione</option>
                                <option value="maquina1">Máquina 1</option>
                                <option value="maquina2">Máquina 2</option>
                                <option value="maquina3">Máquina 3</option>
                            </select>
                        </div>
                        <div className="input-group">
                            <label htmlFor="weight">Peso (kg)</label>
                            <input
                                type="number"
                                id="weight"
                                name="weight"
                                value={weight}
                                onChange={(e) => setWeight(parseFloat(e.target.value))}
                            />
                        </div>
                    </div>
                    <div className="button-group">
                        <div className="cost-section">
                            <button type="button" id="cost-button" onClick={handleCostClick}>
                                Custo Químico
                            </button>
                            {showCost && (
                                <div id="cost-details" className="cost-details">
                                    <p>Custo Total: R$ <span>{totalCost}</span></p>
                                    <p>R$ / KG: <span>{costPerKg}</span></p>
                                </div>
                            )}
                        </div>
                        <div className="recipe-buttons">
                            <button type="button" className="recipe-type-button" onClick={() => handleRecipeButtonClick('lavagem')}>
                                Lavagem
                            </button>
                            <button type="button" className="recipe-type-button" onClick={() => handleRecipeButtonClick('preparacao')}>
                                Preparação
                            </button>
                            <button type="button" className="recipe-type-button" onClick={() => handleRecipeButtonClick('tingimento')}>
                                Tingimento
                            </button>
                        </div>
                    </div>
                </form>
            </div>
            <RecipeModal
                recipeType={modalInfo.recipeType}
                show={modalInfo.show}
                onClose={closeModal}
            />
        </main>
    );
};

export default Receituario;
