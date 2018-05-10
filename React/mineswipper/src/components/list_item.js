import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';

class ListItem extends Component{

  render(){
    const status = 'Started';
    return(
          <div className="media text-muted pt-3">
            <p className="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
                <strong className="d-block text-gray-dark">
                    <a href="#">
                        Player {this.props.game.turn.email} has the turn
                    </a>
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
