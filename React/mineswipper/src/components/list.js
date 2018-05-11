import React, { Component } from 'react';
import { connect } from 'react-redux';
import { accessCheck } from '../utils/system';
import { onChangeInput } from '../utils/inputs';
import '../css/offcanvas.css';
import Loading from './loading';
import ListItem from './list_item';
import { fetchGames, createGame } from '../controllers/system';
import { generateOptions } from '../reducers/system';

class List extends Component{

  constructor(props){
    super(props)
    this.state = {
      isViewReady: false,
      rows: null,
      columns: null,
      mines: null,
    }
    accessCheck(this.props.state, this.props.history);
  }

  componentDidMount(){
    fetchGames(this.props.state,
      this.props.dispatch,
      this.fetchCallBack.bind(this),
      this.errorFetchCallBack.bind(this)
    );
  }

  fetchCallBack = (data) => {
    const state = this;
    setTimeout(function(){
      state.setState({
        isViewReady: true
      })
    }, 500);
  }

  errorFetchCallBack = (data) => {

  }

  changeOptions = (evt) => {
    onChangeInput(evt, this);
  }

  createGame = (evt) => {
    const payload = JSON.stringify({
      columns: this.state.columns,
      rows: this.state.rows,
      mines: this.state.mines,
    })

    createGame(payload,
      this.props.state,
      this.props.dispatch,
      this.fetchCallBack.bind(this),
      this.errorFetchCallBack.bind(this)
    );
  }

  render(){
    if(!this.state.isViewReady){
      return (
        <Loading />
      )
    }
    const columns = generateOptions(10, 30);
    const rows = generateOptions(10, 30);
    const mines = generateOptions(10, 30);
    const history = this.props.history;
    return(
          <div>
            <div className="my-3 p-3 bg-white rounded box-shadow">
                <h1>
                    Mine Swipper
                </h1>
                <br />
                <div className="row">
                    <div className="col-lg-12">
                        <h6>
                            <strong>
                                Create new Game
                            </strong>
                        </h6>
                        <div className="input-group">
                          <div className="input-group-prepend">
                            <span className="input-group-text" id="">Columns</span>
                          </div>
                          <select type="text" className="form-control" name="columns" onChange={this.changeOptions.bind(this)}>
                              <option value="null">Random</option>
                              {columns}
                          </select>
                          <div className="input-group-prepend">
                            <span className="input-group-text" id="">Rows</span>
                          </div>
                          <select type="text" className="form-control" name="rows" onChange={this.changeOptions.bind(this)}>
                              <option value="null">Random</option>
                              {rows}
                          </select>
                          <div className="input-group-prepend">
                            <span className="input-group-text" id="">Mines</span>
                          </div>
                          <select type="text" className="form-control" name="mines" onChange={this.changeOptions.bind(this)}>
                              <option value="null">Random</option>
                              {mines}
                          </select>
                          <div className="input-group-append">
                            <button className="btn btn-success" type="button" onClick={this.createGame.bind(this)}>Create</button>
                          </div>
                        </div>
                    </div>
                </div>
                <br />
                <h6 className="border-bottom border-gray pb-2 mb-0">Your Games</h6>
                {
                  this.props.state.System.yours.map(function(game, index, games){
                    return (<ListItem game={game} others={false} history={history}/>);
                  })
                }
            </div>
            <div className="my-3 p-3 bg-white rounded box-shadow">
                <br />
                <h6 className="border-bottom border-gray pb-2 mb-0">Other Games</h6>
                {
                  this.props.state.System.others.map(function(game, index, games){
                    return (<ListItem game={game} others={true} history={history}/>);
                  })
                }
            </div>
          </div>
    )
  }
}

const mapStateToProps = state => ({
  state: state,
  dispatch: state,
});

export default connect(mapStateToProps)(List);
