import React, { useState, useEffect } from "react";

function LivrosList() {
  const [livros, setLivros] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/livros")
      .then((response) => response.json())
      .then((data) => setLivros(data))
      .catch((error) => console.error("Erro ao buscar livros:", error));
  }, []);

  return (
    <div>
      <h2>Lista de Livros</h2>
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr style={{ backgroundColor: '#86eb6dff' }}>
            <th style={{ padding: '8px', border: '1px solid #ddd' }}>Título</th>
            <th style={{ padding: '8px', border: '1px solid #ddd' }}>Autor</th>
            <th style={{ padding: '8px', border: '1px solid #ddd' }}>ISBN</th>
            <th style={{ padding: '8px', border: '1px solid #ddd' }}>Categoria</th>
          </tr>
        </thead>
        <tbody>
          {livros.map((livro) => (
            <tr key={livro.id}>
              <td style={{ padding: '8px', border: '1px solid #ddd' }}>{livro.nome}</td>
              <td style={{ padding: '8px', border: '1px solid #ddd' }}>{livro.autor}</td>
              <td style={{ padding: '8px', border: '1px solid #ddd' }}>{livro.isbn}</td>
              <td style={{ padding: '8px', border: '1px solid #ddd' }}>{livro.categoria}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default LivrosList;