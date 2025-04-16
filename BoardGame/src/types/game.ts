export type Team = 'BLUE' | 'RED';

export type PieceType = 'RUNNER' | 'SCOUT' | 'SNIPER';

export interface Piece {
    type: PieceType;
    team: Team;
    position: [number, number];
}

export interface BoardState {
    pieces: Piece[];
    currentTurn: Team;
    boardSize: [number, number];
    phase: 'PLACING' | 'MOVING';
    availableUnits: {
        [key in Team]: {
            [key in PieceType]: number;
        };
    };
}

export interface GameState {
    board: BoardState;
    gameOver: boolean;
    winner: Team | null;
} 