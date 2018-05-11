import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';

class ListItem extends Component{

  render(){
    const status = (this.props.game.status === 1) ? 'Started' : (this.props.game.status === 2) ? "Paused" : (this.props.game.status === 3) ? "Finished" : "Finished";
    const url = this.props.state.System.pages.GAME.replace(":key", this.props.game.id);
    return(
          <div className="media text-muted pt-3">
            <p className="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
                <strong className="d-block text-gray-dark">
                    <Link to={url}>
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
