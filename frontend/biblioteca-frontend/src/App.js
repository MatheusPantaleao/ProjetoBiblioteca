import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import PessoasList from "./components/PessoasList";

function App() {
  return (
    <Router>
      <nav style={{ margin: "20px" }}>
        <Link to="/" style={{ marginRight: "10px" }}>Página Inicial</Link>
        <Link to="/pessoas">Pessoas</Link>
      </nav>
      <Routes>
        <Route path="/" element={<h2>Página inicial</h2>} />
        <Route path="/pessoas" element={<PessoasList />} />
      </Routes>
    </Router>
  );
}

export default App;
