import React, { useState, useEffect } from 'react';
import PessoaForm from './PessoaForm'; // Importe o novo componente

function PessoasList() {
  const [pessoas, setPessoas] = useState([]);
  const [showForm, setShowForm] = useState(false); // Estado para controlar a visibilidade do formulário

  const fetchPessoas = () => {
    fetch('http://127.0.0.1:5000/pessoas')
      .then((response) => response.json())
      .then((data) => setPessoas(data))
      .catch((error) => console.error('Erro ao buscar pessoas:', error));
  };

  useEffect(() => {
    fetchPessoas();
  }, []);

  const handlePessoaCreated = (novaPessoa) => {
    setPessoas([...pessoas, novaPessoa]); // Adiciona a nova pessoa à lista existente
    setShowForm(false); // Esconde o formulário após a criação
  };

  const buttonStyle = {
    padding: '10px 20px',
    backgroundColor: '#28a745',
    color: 'white',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
    marginBottom: '20px',
  };

  return (
    <div>
      <h2>Lista de Pessoas</h2>
      <button onClick={() => setShowForm(!showForm)} style={buttonStyle}>
        {showForm ? 'Cancelar' : 'Adicionar Pessoa'}
      </button>

      {showForm && <PessoaForm onPessoaCreated={handlePessoaCreated} />}

      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr style={{ backgroundColor: '#f2f2f2' }}>
            <th style={{ padding: '8px', border: '1px solid #ddd', textAlign: 'left' }}>Nome</th>
            <th style={{ padding: '8px', border: '1px solid #ddd', textAlign: 'left' }}>Email</th>
            <th style={{ padding: '8px', border: '1px solid #ddd', textAlign: 'left' }}>CPF</th>
            <th style={{ padding: '8px', border: '1px solid #ddd', textAlign: 'left' }}>Tipo</th>
          </tr>
        </thead>
        <tbody>
          {pessoas.map((pessoa) => (
            <tr key={pessoa.id}>
              <td style={{ padding: '8px', border: '1px solid #ddd' }}>{pessoa.nome}</td>
              <td style={{ padding: '8px', border: '1px solid #ddd' }}>{pessoa.email}</td>
              <td style={{ padding: '8px', border: '1px solid #ddd' }}>{pessoa.cpf}</td>
              <td style={{ padding: '8px', border: '1px solid #ddd' }}>{pessoa.tipo}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default PessoasList;