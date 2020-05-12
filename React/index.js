import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

//Square is a function for the square component of the grid. It only renders and therefore a function.
function Square(props) {
    return (
      //onClick is passed in by Board component. 
      <button className="square" onClick={props.onClick}>
        {props.value}
      </button>
    );
  }

//Board is a class because it contains a renderSquare method in order to create the board.
class Board extends React.Component {
// renders the square and passes in the squares position on the board and the onClick function that was passed by the game method.
  renderSquare(i) {
    return (<Square 
      value={this.props.squares[i]}
      onClick={() => this.props.onClick(i)}
  />);
  }
  //Rendering of the board in order to be visible in browser
  render() {
    return (
      <div>
        <div className="board-row">
          {this.renderSquare(0)}{this.renderSquare(1)}{this.renderSquare(2)}
        </div>
        <div className="board-row">
          {this.renderSquare(3)}{this.renderSquare(4)}{this.renderSquare(5)}
        </div>
        <div className="board-row">
          {this.renderSquare(6)}{this.renderSquare(7)}{this.renderSquare(8)}
        </div>
      </div>
    );
  }
}
//Game class that does all the heavy lifting and state memory storage. All the children are just visual.
class Game extends React.Component {

  //Constructor for the state values it can have. History is the past states of board. xIsNext denotes whether whos turn it is. stepNum is a counter for past states.
  constructor(props){
    super(props);
    this.state = {
      history: [{
        squares: Array(9).fill(null),
      }],
      xIsNext: true,
      stepNum: 0, 
    };
  }
//handleClick is the handler for the onClick event that was passed down to Board and then Square.
//Three varaible history is a slice of the board states. current is the current board state. squares is the values of all the squares
  handleClick(i){
    const history = this.state.history.slice(0, this.state.stepNum + 1);
    const current = history[history.length - 1];
    const squares = current.squares.slice();
    //Each trigger checks for a winner
    if(calculateWinner(squares) || squares[i]){
      return;
    }
    //Logic handler for alternating turns
    squares[i] = this.state.xIsNext ? 'X' : 'O'
    //Update the state for the next usage of the information
    this.setState({
      history: history.concat([{
        squares: squares
      }]),
      xIsNext: !this.state.xIsNext,
      stepNum : history.length,
    });
  }
  //jumpTo will jump to the state that was chosen from the list of previous states. xIsNext: (step % 2)===0 will decide which turn it is in that state
  jumpTo(step){
    this.setState({
      stepNum: step,
      xIsNext: (step % 2) ===0,
    });
  }
  //history and current are passed in from the constructor while winner is calculated upon render
  render() {
    const history = this.state.history;
    const current = history[this.state.stepNum];
    const winner = calculateWinner(current.squares);
//This will create the catalog of past moves
    const moves = history.map((step,move)=>{
      const desc = move ?
      "Go to move #" + move :
      "Go to game start";
      return(
        <li key={move}>
          <button onClick={() => this.jumpTo(move)}>{desc}</button>
        </li>
      )
    });
    //Decides if there was winner or not
    let status;
    if (winner){
      status = "Winner: " + winner;
    } else{
      status = "Next player: " + (this.state.xIsNext ? "X" : "O");
    }
// returns the output for the webapp.
// Board gets passed the current squares values. And the onClick function which gets passed down to squares.
    return (
      <div className="game">
        <div className="game-board">
          <Board
          squares = {current.squares}
          onClick={(i) => this.handleClick(i)} />
        </div>
        <div className="game-info">
          <div>{status}</div>
          <ol>{moves}</ol>
        </div>
      </div>
    );
  }
}
//calculate winner has an array for all possible lines in a 3x3 grid for determining a winner
function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}
// ========================================

ReactDOM.render(
  <React.StrictMode>
    
    <Game />
  </React.StrictMode>,
  
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change <App />
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
