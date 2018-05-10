import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import { accessCheck } from '../utils/system';
import '../css/offcanvas.css';

class List extends Component{

  constructor(props){
    super(props)
    this.state = {
    }

    accessCheck(this.props.state, this.props.history);
  }

  render(){
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
          <div className="media text-muted pt-3">
              <p className="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
                  <strong className="d-block text-gray-dark">
                      <a href="#">
                          Player ricardo.tercero@r3s.com.mx has the turn
                      </a>
                  </strong>
                  Columns: <strong>48</strong>
                  X
                  Rows: <strong>24</strong>
                  &nbsp;
                  &mdash;
                  &nbsp;
                  Mines: <strong>21</strong>
                  &nbsp;
                  &mdash;
                  &nbsp;
                  Flag Left: <strong>10</strong>
                  &nbsp;
                  &mdash;
                  &nbsp;
                  Status: <strong>Started</strong>
                  &nbsp;
                  &mdash;
                  &nbsp;
                  Elapsed Time: <strong>Days (1) Hours (10) Minutes (2) Seconds (1)</strong>
              </p>
          </div>
          <div className="media text-muted pt-3">
              <p className="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
                  <strong className="d-block text-gray-dark">
                      <a href="#">
                          Player ricardo.tercero@r3s.com.mx has the turn
                      </a>
                  </strong>
                  Columns: <strong>48</strong>
                  X
                  Rows: <strong>24</strong>
                  &nbsp;
                  &mdash;
                  &nbsp;
                  Mines: <strong>21</strong>
                  &nbsp;
                  &mdash;
                  &nbsp;
                  Flag Left: <strong>10</strong>
                  &nbsp;
                  &mdash;
                  &nbsp;
                  Status: <strong>Started</strong>
                  &nbsp;
                  &mdash;
                  &nbsp;
                  Elapsed Time: <strong>Days (1) Hours (10) Minutes (2) Seconds (1)</strong>
              </p>
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
