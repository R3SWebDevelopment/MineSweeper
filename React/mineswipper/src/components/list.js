import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import { accessCheck } from '../utils/system';
import '../css/offcanvas.css';
import Loading from './loading';
import ListItem from './list_item';
import { fetchGames } from '../controllers/system';

class List extends Component{

  constructor(props){
    super(props)
    this.state = {
      isViewReady: false,
    }
    accessCheck(this.props.state, this.props.history);
  }

  componentDidMount(){
    fetchGames(this.props.state, this.props.dispatch, this.fetchCallBack.bind(this), this.errorFetchCallBack.bind(this));
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

  render(){
    if(!this.state.isViewReady){
      return (
        <Loading />
      )
    }
    return(
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
                    <select type="text" className="form-control">
                        <option>Select an Option</option>
                    </select>
                    <div className="input-group-prepend">
                      <span className="input-group-text" id="">Rows</span>
                    </div>
                    <select type="text" className="form-control">
                        <option>Select an Option</option>
                    </select>
                    <div className="input-group-prepend">
                      <span className="input-group-text" id="">Mines</span>
                    </div>
                    <select type="text" className="form-control">
                        <option>Select an Option</option>
                    </select>
                    <div className="input-group-append">
                      <button className="btn btn-success" type="button">Create</button>
                    </div>
                  </div>
              </div>
          </div>
          <br />
          <h6 className="border-bottom border-gray pb-2 mb-0">Your Games</h6>
          {
            this.props.state.System.games.map(function(game, index, games){
              return (<ListItem game={game}/>);
            })
          }
      </div>
    )
  }
}

const mapStateToProps = state => ({
  state: state,
  dispatch: state,
});

export default connect(mapStateToProps)(List);
