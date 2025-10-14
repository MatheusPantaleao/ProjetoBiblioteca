import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import PessoasList from "./components/PessoasList";
import LivrosList from "./components/LivrosList";
import EmprestimosList from "./components/EmprestimosList";

function App() {
  return (
    <Router>
      <div style={{ fontFamily: 'Arial, sans-serif' }}>
        <nav style={{ 
          margin: "20px", 
          padding: "10px", 
          borderBottom: "2px solid #ccc" 
        }}>
          <Link to="/" style={{ marginRight: "15px", textDecoration: "none", fontSize: "18px" }}>Página Inicial</Link>
          <Link to="/pessoas" style={{ marginRight: "15px", textDecoration: "none", fontSize: "18px" }}>Pessoas</Link>
          <Link to="/livros" style={{ marginRight: "15px", textDecoration: "none", fontSize: "18px" }}>Livros</Link>
          <Link to="/emprestimos" style={{ textDecoration: "none", fontSize: "18px" }}>Empréstimos</Link>
        </nav>
        <div style={{ padding: "20px" }}>
          <Routes>
            <Route path="/" element={<h2>Bem-vindo ao Sistema da Biblioteca</h2>} />
            <Route path="/pessoas" element={<PessoasList />} />
            <Route path="/livros" element={<LivrosList />} />
            <Route path="/emprestimos" element={<EmprestimosList />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;