import React, { useState, Fragment } from 'react';
import Navbar from '../../common/components/Navbar/Navbar';
import './Romaneio.css';

const Romaneio = () => {
  const [rows, setRows] = useState([
    { artigo: '', tingimento: '', valorUnitario: '', peso: '', detailsVisible: false, details: [{ pesoCru: '', pesoAcabado: '' }] },
  ]);

  const handleInputChange = (index, event) => {
    const { name, value } = event.target;
    const newRows = [...rows];
    newRows[index][name] = value;
    setRows(newRows);
  };

  const handleDetailsInputChange = (mainIndex, detailIndex, event) => {
    const { name, value } = event.target;
    const newRows = [...rows];
    newRows[mainIndex].details[detailIndex][name] = value;
    setRows(newRows);
  };

  const addRow = () => {
    setRows([...rows, { artigo: '', tingimento: '', valorUnitario: '', peso: '', detailsVisible: false, details: [{ pesoCru: '', pesoAcabado: '' }] }]);
  };

  const removeLastRow = () => {
    if (rows.length > 1) {
      const newRows = [...rows];
      newRows.pop();
      setRows(newRows);
    }
  };

  const addDetailRow = (mainIndex) => {
    const newRows = [...rows];
    newRows[mainIndex].details.push({ pesoCru: '', pesoAcabado: '' });
    setRows(newRows);
  };

  const removeDetailRow = (mainIndex, detailIndex) => {
    const newRows = [...rows];
    if (newRows[mainIndex].details.length > 1) {
        newRows[mainIndex].details.splice(detailIndex, 1);
        setRows(newRows);
    }
  };

  const handleDetailsClick = (index) => {
    const newRows = [...rows];
    newRows[index].detailsVisible = !newRows[index].detailsVisible;
    setRows(newRows);
  };

  const calculatePesoLiquido = (details) => {
    const pesoCru = parseFloat(details.pesoCru);
    const pesoAcabado = parseFloat(details.pesoAcabado);
    return (pesoCru && pesoAcabado) ? (pesoCru - pesoAcabado).toFixed(2) : '0.00';
  };

  return (
    <div>
      <Navbar />
      <div className="content-container">
        <table className="romaneio-table">
          <thead>
            <tr>
              <th>Detalhes</th>
              <th>Artigo</th>
              <th>Tingimento</th>
              <th>Valor Unitário (R$ / Kg)</th>
              <th>Peso (Kg)</th>
              <th>Subtotal</th>
            </tr>
          </thead>
          <tbody>
            {rows.map((row, mainIndex) => (
              <Fragment key={mainIndex}>
                <tr>
                  <td><button onClick={() => handleDetailsClick(mainIndex)} className="details-button">detalhes</button></td>
                  <td><input type="text" name="artigo" value={row.artigo} onChange={(e) => handleInputChange(mainIndex, e)} /></td>
                  <td><input type="text" name="tingimento" value={row.tingimento} onChange={(e) => handleInputChange(mainIndex, e)} /></td>
                  <td><input type="number" name="valorUnitario" value={row.valorUnitario} onChange={(e) => handleInputChange(mainIndex, e)} /></td>
                  <td><input type="number" name="peso" value={row.peso} onChange={(e) => handleInputChange(mainIndex, e)} /></td>
                  <td>R$ {((row.valorUnitario && row.peso) ? (row.valorUnitario * row.peso).toFixed(2) : '0.00')}</td>
                </tr>
                {row.detailsVisible && (
                  <tr className="details-row">
                    <td colSpan="6">
                      <table className="details-table">
                        <thead>
                          <tr>
                            <th></th>
                            <th>Peso Cru</th>
                            <th>Peso Acabado</th>
                            <th>Peso Líquido</th>
                          </tr>
                        </thead>
                        <tbody>
                          {row.details.map((detail, detailIndex) => (
                            <tr key={detailIndex}>
                              <td>
                                <button onClick={() => addDetailRow(mainIndex)} className="detail-action-button">+</button>
                                <button onClick={() => removeDetailRow(mainIndex, detailIndex)} className="detail-action-button">-</button>
                              </td>
                              <td><input type="number" name="pesoCru" value={detail.pesoCru} onChange={(e) => handleDetailsInputChange(mainIndex, detailIndex, e)} /></td>
                              <td><input type="number" name="pesoAcabado" value={detail.pesoAcabado} onChange={(e) => handleDetailsInputChange(mainIndex, detailIndex, e)} /></td>
                              <td>{calculatePesoLiquido(detail)}</td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </td>
                  </tr>
                )}
              </Fragment>
            ))}
          </tbody>
        </table>
        <div className="table-buttons">
          <button onClick={addRow} className="add-row-button">Adicionar Linha</button>
          <button onClick={removeLastRow} className="remove-row-button">Remover linha</button>
        </div>
      </div>
    </div>
  );
};

export default Romaneio;