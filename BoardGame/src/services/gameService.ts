import { BoardState, GameState, Piece, Team, PieceType } from '../types/game';

export const BOARD_SIZE: [number, number] = [30, 10];
const INITIAL_UNITS = {
    RUNNER: 3,
    SCOUT: 3,
    SNIPER: 3
};

export const initializeGame = (): GameState => {
    const board: BoardState = {
        pieces: [],
        currentTurn: 'BLUE',
        boardSize: BOARD_SIZE,
        phase: 'PLACING',
        availableUnits: {
            BLUE: { ...INITIAL_UNITS },
            RED: { ...INITIAL_UNITS }
        }
    };

    return {
        board,
        gameOver: false,
        winner: null,
    };
};

export const placePiece = (
    gameState: GameState,
    pieceType: PieceType,
    position: [number, number]
): GameState => {
    if (gameState.gameOver) return gameState;
    if (gameState.board.phase !== 'PLACING') return gameState;
    
    const currentTeam = gameState.board.currentTurn;
    const availableUnits = gameState.board.availableUnits[currentTeam][pieceType];
    
    if (availableUnits <= 0) return gameState;

    // Check if position is valid (within first/last row for respective teams)
    const isValidPosition = currentTeam === 'BLUE' 
        ? position[1] === 0 
        : position[1] === BOARD_SIZE[1] - 1;

    if (!isValidPosition) return gameState;

    // Check if position is already occupied
    const isOccupied = gameState.board.pieces.some(
        p => p.position[0] === position[0] && p.position[1] === position[1]
    );

    if (isOccupied) return gameState;

    const newPiece: Piece = {
        type: pieceType,
        team: currentTeam,
        position: position
    };

    const newPieces = [...gameState.board.pieces, newPiece];
    const newAvailableUnits = {
        ...gameState.board.availableUnits,
        [currentTeam]: {
            ...gameState.board.availableUnits[currentTeam],
            [pieceType]: availableUnits - 1
        }
    };

    // Check if all units are placed for current team
    const allUnitsPlaced = Object.values(newAvailableUnits[currentTeam]).every(count => count === 0);
    const otherTeam = currentTeam === 'BLUE' ? 'RED' : 'BLUE';
    const otherTeamAllPlaced = Object.values(newAvailableUnits[otherTeam]).every(count => count === 0);

    return {
        ...gameState,
        board: {
            ...gameState.board,
            pieces: newPieces,
            availableUnits: newAvailableUnits,
            currentTurn: allUnitsPlaced ? otherTeam : currentTeam,
            phase: allUnitsPlaced && otherTeamAllPlaced ? 'MOVING' : 'PLACING'
        }
    };
};

export const movePiece = (
    gameState: GameState,
    piece: Piece,
    newPosition: [number, number]
): GameState => {
    if (gameState.gameOver) return gameState;
    if (gameState.board.phase !== 'MOVING') return gameState;
    if (piece.team !== gameState.board.currentTurn) return gameState;

    const moveDistance = getMoveDistance(piece.type);
    const currentPosition = piece.position;
    const distance = Math.abs(newPosition[0] - currentPosition[0]) + 
                    Math.abs(newPosition[1] - currentPosition[1]);

    if (distance > moveDistance) return gameState;

    const newPieces = gameState.board.pieces.map(p => {
        if (p === piece) {
            return { ...p, position: newPosition };
        }
        return p;
    });

    return {
        ...gameState,
        board: {
            ...gameState.board,
            pieces: newPieces,
            currentTurn: gameState.board.currentTurn === 'BLUE' ? 'RED' : 'BLUE',
        },
    };
};

const getMoveDistance = (pieceType: string): number => {
    switch (pieceType) {
        case 'RUNNER':
        case 'SNIPER':
            return 1;
        case 'SCOUT':
            return 2;
        default:
            return 0;
    }
}; 