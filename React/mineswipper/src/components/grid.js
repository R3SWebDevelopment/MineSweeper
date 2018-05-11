import React, { Component } from 'react';
import { connect } from 'react-redux';
import '../css/offcanvas.css';
import '../css/grid.css';
import Loading from './loading';
import { accessCheck } from '../utils/system';
import { fetchGame, revealCell, markCell, unmarkCell, restartGame, resumeGame, pauseGame } from '../controllers/system';
import ListItem from './list_item';

class Grid extends Component{

  constructor(props){
    super(props)
    this.state = {
      isViewReady: false,
      game: null,
    }
    accessCheck(this.props.state, this.props.history);
  }

  componentDidMount(){
    fetchGame(this.props.match.params.key,
      this.props.state,
      this.props.dispatch,
      this.fetchCallBack.bind(this),
      this.errorFetchCallBack.bind(this));
  }

  fetchCallBack = (data) => {
    const state = this;
    setTimeout(function(){
      state.setState({
        isViewReady: true,
        game: data
      })
    }, 500);
  }

  errorFetchCallBack = (data) => {

  }

  onClickAction = (evt) => {
    const valid = (evt.target.innerHTML === "*") ? true : (evt.target.innerHTML === "?" && evt.shiftKey) ? true : false;
    const mark = (evt.target.innerHTML === "*") ? true : false;
    if(valid){
      const id = this.state.game.id;
      const x = evt.target.dataset.x;
      const y = evt.target.dataset.y;
      const state = this.props.state;
      const dispatch = this.props.dispatch;
      const callback = this.fetchCallBack.bind(this);
      const errorCallBack = this.errorFetchCallBack.bind(this);
      let action = null;
      if(evt.shiftKey){ // Mark or Unmark
        if(mark){
          action = markCell.bind(this);
        }else{
          action = unmarkCell.bind(this);
        }
      }else{ // Reveal
        action = revealCell.bind(this);
      }
      this.setState({
        isViewReady: false
      },() => {
        const data = JSON.stringify({
          x: x,
          y: y
        })
        action(id, data, state, dispatch, callback, errorCallBack)
      })
    }else{
      alert("Action no available")
    }
  }

  goBack = () => {
    this.props.history.push(this.props.state.System.pages.LIST)
  }

  pauseGame = () => {
    const id = this.state.game.id;
    const state = this.props.state;
    const dispatch = this.props.dispatch;
    const callback = this.fetchCallBack.bind(this);
    const errorCallBack = this.errorFetchCallBack.bind(this);
    const action = pauseGame.bind(this);
    this.setState({
      isViewReady: false
    },() => {
      action(id, state, dispatch, callback, errorCallBack)
    })
  }

  resumeGame = () => {
    const id = this.state.game.id;
    const state = this.props.state;
    const dispatch = this.props.dispatch;
    const callback = this.fetchCallBack.bind(this);
    const errorCallBack = this.errorFetchCallBack.bind(this);
    const action = resumeGame.bind(this);
    this.setState({
      isViewReady: false
    },() => {
      action(id, state, dispatch, callback, errorCallBack)
    })
  }

  restartGame = () => {
    const id = this.state.game.id;
    const state = this.props.state;
    const dispatch = this.props.dispatch;
    const callback = this.fetchCallBack.bind(this);
    const errorCallBack = this.errorFetchCallBack.bind(this);
    const action = restartGame.bind(this);
    this.setState({
      isViewReady: false
    },() => {
      action(id, state, dispatch, callback, errorCallBack)
    })
  }

  render(){
    if(!this.state.isViewReady){
      return (
        <Loading />
      )
    }
    const no_input = (this.state.game.status === 1) ? false : true;
    const no_action = this.state.game.is_your_turn && no_input;
    const can_restart = this.state.game.is_your_turn;
    const state = this.state
    const onClickAction = this.onClickAction.bind(this)
    return(
      <div>
        <div class="my-3 p-3 bg-white rounded box-shadow">
            <h1>
                Mine Swipper
            </h1>
            <h6 class="border-bottom border-gray pb-2 mb-0">Board</h6>
            <ListItem game={this.state.game} others={false}/>
        </div>
        <div class="my-3 p-3 bg-white rounded box-shadow">
          {
            Array(this.state.game.rows).fill(1).map(function(value, index){
              const y = index;
              return (
                <div class="row justify-content-center">
                    <div class="col">
                      {
                        Array(state.game.columns).fill(1).map(function(value, index){
                          const label = state.game.cells[index + "_" + y]
                          return (
                            <button
                              className="cell"
                              data-x={index}
                              data-y={y}
                              onClick={onClickAction}
                              disabled={no_input}
                            >
                                {label}
                            </button>
                          )
                        })
                      }
                    </div>
                </div>
              )
            })
          }
        </div>
        <div class="my-3 p-3 bg-white rounded box-shadow">
            <div class="media text-muted pt-3">
                <button type="button" class="btn btn-primary" onClick={this.goBack.bind(this)}>
                    Go Back
                </button>
                    &nbsp;
                    &nbsp;
                <button type="button" class="btn btn-danger" onClick={this.pauseGame.bind(this)} disabled={no_action}>
                    Pause
                </button>
                    &nbsp;
                    &nbsp;
                <button type="button" class="btn btn-success" onClick={this.resumeGame.bind(this)} disabled={no_action}>
                    Resume
                </button>
                    &nbsp;
                    &nbsp;
                <button type="button" class="btn btn-info" onClick={this.restartGame.bind(this)} disabled={!can_restart}>
                    Restart
                </button>
            </div>
        </div>
        <p>
            <strong>Actions</strong><br />
            Left Click     : Reveal Cell<br />
            Left Click + Shift Key    : Mark or Unmark Cell<br />
        </p>
        <p>
            <strong>Nomenclature</strong><br />
            *     : None Revealed Cell<br />
            _ : Revealed Cell<br />
            ?     : Flaged Cell<br />
            B     : Boom<br />
            [1-8] : Adjacents Count
        </p>
      </div>
    )
  }
}

const mapStateToProps = state => ({
  state: state,
  dispatch: state,
});

export default connect(mapStateToProps)(Grid);
