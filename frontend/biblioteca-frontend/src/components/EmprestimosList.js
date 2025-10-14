import React, { useState, useEffect } from "react";

function EmprestimosList() {
  const [emprestimos, setEmprestimos] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/emprestimos")
      .then((response) => response.json())
      .then((data) => setEmprestimos(data))
      .catch((error) => console.error("Erro ao buscar empréstimos:", error));
  }, []);

  return (
    <div>
      <h2>Lista de Empréstimos</h2>
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr style={{ backgroundColor: '#5d5aeeff' }}>
            <th style={{ padding: '8px', border: '1px solid #ddd' }}>Pessoa</th>
            <th style={{ padding: '8px', border: '1px solid #ddd' }}>Livro</th>
            <th style={{ padding: '8px', border: '1px solid #ddd' }}>Data do Empréstimo</th>
          </tr>
        </thead>
        <tbody>
          {emprestimos.map((emprestimo) => (
            <tr key={emprestimo.id}>
              <td style={{ padding: '8px', border: '1px solid #ddd' }}>{emprestimo.pessoa.nome}</td>
              <td style={{ padding: '8px', border: '1px solid #ddd' }}>{emprestimo.livro.nome}</td>
              <td style={{ padding: '8px', border: '1px solid #ddd' }}>{emprestimo.data_emprestimo}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default EmprestimosList;