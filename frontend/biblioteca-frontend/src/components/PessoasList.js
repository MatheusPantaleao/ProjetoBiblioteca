import React, { useEffect, useState } from "react";

function PessoasList() {
  const [pessoas, setPessoas] = useState([]);
  const [erro, setErro] = useState(null);

  useEffect(() => {
    fetch("http://localhost:5000/pessoas")
      .then((res) => {
        if (!res.ok) {
          throw new Error("Erro ao buscar pessoas: " + res.status);
        }
        return res.json();
      })
      .then((data) => setPessoas(data))
      .catch((err) => setErro(err.message));
  }, []);

  return (
    <div style={{ margin: "20px" }}>
      <h2>Lista de Pessoas</h2>
      {erro && <p style={{ color: "red" }}>{erro}</p>}
      {pessoas.length > 0 ? (
        <ul>
          {pessoas.map((p) => (
            <li key={p.id}>
              {p.nome} - {p.cpf} - {p.email} - {p.numero}
            </li>
          ))}
        </ul>
      ) : (
        !erro && <p>Nenhuma pessoa encontrada.</p>
      )}
    </div>
  );
}

export default PessoasList;
