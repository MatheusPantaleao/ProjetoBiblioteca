import React, { useState } from 'react';

function PessoaForm({ onPessoaCreated }) {
  const [nome, setNome] = useState('');
  const [cpf, setCpf] = useState('');
  const [idade, setIdade] = useState('');
  const [email, setEmail] = useState('');
  const [numero, setNumero] = useState('');
  const [tipo, setTipo] = useState('cliente'); // Valor padrão

  const handleSubmit = (e) => {
    e.preventDefault();

    const novaPessoa = {
      nome,
      cpf,
      idade: parseInt(idade), // Garante que idade seja um número
      email,
      numero,
      tipo,
    };

    fetch('http://127.0.0.1:5000/pessoas', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(novaPessoa),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.error) {
          alert('Erro: ' + data.error);
        } else {
          alert('Pessoa adicionada com sucesso!');
          onPessoaCreated(data); // Chama a função do componente pai para atualizar a lista
          // Limpa o formulário
          setNome('');
          setCpf('');
          setIdade('');
          setEmail('');
          setNumero('');
          setTipo('cliente');
        }
      })
      .catch((error) => console.error('Erro ao criar pessoa:', error));
  };

  const formStyle = {
    margin: '20px 0',
    padding: '20px',
    border: '1px solid #ccc',
    borderRadius: '8px',
  };

  const inputStyle = {
    display: 'block',
    width: 'calc(100% - 16px)',
    padding: '8px',
    margin: '10px 0',
    borderRadius: '4px',
    border: '1px solid #ccc',
  };

  const buttonStyle = {
    padding: '10px 20px',
    backgroundColor: '#007BFF',
    color: 'white',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
  };

  return (
    <form onSubmit={handleSubmit} style={formStyle}>
      <h3>Adicionar Nova Pessoa</h3>
      <input type="text" value={nome} onChange={(e) => setNome(e.target.value)} placeholder="Nome" required style={inputStyle} />
      <input type="text" value={cpf} onChange={(e) => setCpf(e.target.value)} placeholder="CPF" required style={inputStyle} />
      <input type="number" value={idade} onChange={(e) => setIdade(e.target.value)} placeholder="Idade" required style={inputStyle} />
      <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" required style={inputStyle} />
      <input type="text" value={numero} onChange={(e) => setNumero(e.target.value)} placeholder="Número de Telefone" required style={inputStyle} />
      <select value={tipo} onChange={(e) => setTipo(e.target.value)} required style={inputStyle}>
        <option value="cliente">Cliente</option>
        <option value="professor">Professor</option>
        <option value="funcionario">Funcionário</option>
      </select>
      <button type="submit" style={buttonStyle}>Salvar</button>
    </form>
  );
}

export default PessoaForm;