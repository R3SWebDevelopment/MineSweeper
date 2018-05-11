import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import { joingGame, leavingGame } from '../controllers/system';

class ListItem extends Component{

  joinGame = (evt) => {
    joingGame(this.props.game.id,
      this.props.state,
      this.props.dispatch,
      this.successCallBack.bind(this),
      this.errorCallBack.bind(this))
  }

  leaveGame = (evt) => {
    leavingGame(this.props.game.id,
      this.props.state,
      this.props.dispatch,
      this.successCallBack.bind(this),
      this.errorCallBack.bind(this))
  }

  successCallBack = (data) => {
    window.location = this.props.state.System.pages.LIST
    this.props.history.push(this.props.state.System.pages.LIST)
  }

  errorCallBack = (data) => {
    window.location = this.props.state.System.pages.LIST
    this.props.history.push(this.props.state.System.pages.LIST)
  }

  render(){
    const status = (this.props.game.status === 1) ? 'Started' : (this.props.game.status === 2) ? "Paused" : (this.props.game.status === 3) ? "Finished" : "Finished";
    const url = this.props.state.System.pages.GAME.replace(":key", this.props.game.id);
    const statu_text = (this.props.game.is_your_turn) ? "Waiting your move" : (this.props.game.status === 1) ? ("Waiting for " + this.props.game.turn.email) : (this.props.game.status === 2) ? ("Game on pause by " + this.props.game.turn.email) : (this.props.game.status === 3) ? "Finished" : "Finished";
    return(
          <div className="media text-muted pt-3">
            <p className="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
                <strong className="d-block text-gray-dark">
                    <Link to={(this.props.others) ? "#" : url}>
                      Player {this.props.game.turn.email} has the turn
                    </Link>
                </strong>
                Columns: <strong>{this.props.game.columns}</strong>
                X
                Rows: <strong>{this.props.game.rows}</strong>
                &nbsp;
                &mdash;
                &nbsp;
                Mines: <strong>{this.props.game.mines_count}</strong>
                &nbsp;
                &mdash;
                &nbsp;
                Flag Left: <strong>{this.props.game.marks_left}</strong>
                &nbsp;
                &mdash;
                &nbsp;
                Status: <strong>{status}</strong>
                &nbsp;
                &mdash;
                &nbsp;
                Elapsed Time: <strong>{this.props.game.time_elapsed}</strong>
                &nbsp;
                &mdash;
                &nbsp;
                Users: <strong>{this.props.game.players.length}</strong>
                <br />
                Result: <strong>{this.props.game.result}</strong>
                <br />
                Status: <strong>{statu_text}</strong>
                <br />
                {(this.props.others) ? <button className="btn btn-success" onClick={this.joinGame.bind(this)}>Join</button> : <button className="btn btn-danger" onClick={this.leaveGame.bind(this)}>Leave</button>}
            </p>
        </div>
    )
  }
}

const mapStateToProps = state => ({
  state: state,
  dispatch: state,
});

export default connect(mapStateToProps)(ListItem);
