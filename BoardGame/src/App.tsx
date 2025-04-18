import React from 'react';
import GameBoard from './components/GameBoard';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Board Game</h1>
      </header>
      <main>
        <GameBoard />
      </main>
    </div>
  );
}

export default App; 