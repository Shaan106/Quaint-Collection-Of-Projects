import React, { useState } from 'react';
import { GameState, Piece, PieceType } from '../types/game';
import { initializeGame, movePiece, placePiece, BOARD_SIZE } from '../services/gameService';
import './GameBoard.css';

const GameBoard: React.FC = () => {
    const [gameState, setGameState] = useState<GameState>(initializeGame());
    const [selectedPiece, setSelectedPiece] = useState<Piece | null>(null);
    const [selectedUnitType, setSelectedUnitType] = useState<PieceType | null>(null);

    const handleCellClick = (x: number, y: number) => {
        if (gameState.board.phase === 'PLACING') {
            if (selectedUnitType) {
                setGameState(placePiece(gameState, selectedUnitType, [x, y]));
                setSelectedUnitType(null);
            }
        } else {
            if (selectedPiece) {
                setGameState(movePiece(gameState, selectedPiece, [x, y]));
                setSelectedPiece(null);
            } else {
                const piece = gameState.board.pieces.find(
                    p => p.position[0] === x && p.position[1] === y
                );
                if (piece && piece.team === gameState.board.currentTurn) {
                    setSelectedPiece(piece);
                }
            }
        }
    };

    const renderCell = (x: number, y: number) => {
        const piece = gameState.board.pieces.find(
            p => p.position[0] === x && p.position[1] === y
        );

        const isSelected = selectedPiece && 
            selectedPiece.position[0] === x && 
            selectedPiece.position[1] === y;

        const isValidPlacement = gameState.board.phase === 'PLACING' && 
            ((gameState.board.currentTurn === 'BLUE' && y === 0) ||
             (gameState.board.currentTurn === 'RED' && y === BOARD_SIZE[1] - 1));

        return (
            <div
                key={`${x}-${y}`}
                className={`cell ${piece ? piece.team.toLowerCase() : ''} ${isSelected ? 'selected' : ''} ${isValidPlacement ? 'valid-placement' : ''}`}
                onClick={() => handleCellClick(x, y)}
            >
                {piece && (
                    <div className="piece">
                        {piece.type.charAt(0)}
                    </div>
                )}
            </div>
        );
    };

    const renderUnitButtons = () => {
        if (gameState.board.phase !== 'PLACING') return null;

        const currentTeam = gameState.board.currentTurn;
        const availableUnits = gameState.board.availableUnits[currentTeam];

        return (
            <div className="unit-buttons">
                {Object.entries(availableUnits).map(([type, count]) => (
                    count > 0 && (
                        <button
                            key={type}
                            className={`unit-button ${type.toLowerCase()} ${selectedUnitType === type ? 'selected' : ''}`}
                            onClick={() => setSelectedUnitType(type as PieceType)}
                        >
                            {type} ({count})
                        </button>
                    )
                ))}
            </div>
        );
    };

    return (
        <div className="game-container">
            <div className="game-info">
                <h2>Current Turn: {gameState.board.currentTurn}</h2>
                <h3>Phase: {gameState.board.phase}</h3>
                {renderUnitButtons()}
            </div>
            <div 
                className="board"
                style={{
                    gridTemplateColumns: `repeat(${BOARD_SIZE[0]}, 1fr)`,
                    gridTemplateRows: `repeat(${BOARD_SIZE[1]}, 1fr)`,
                }}
            >
                {Array.from({ length: BOARD_SIZE[1] }).map((_, y) =>
                    Array.from({ length: BOARD_SIZE[0] }).map((_, x) =>
                        renderCell(x, y)
                    )
                )}
            </div>
        </div>
    );
};

export default GameBoard; 