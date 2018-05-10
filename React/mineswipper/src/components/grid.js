import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import '../css/offcanvas.css';

class Grid extends Component{

  constructor(props){
    super(props)
    this.state = {
      username: '',
      password: ''
    }
  }

  render(){
    return(
      <div>
        <div class="my-3 p-3 bg-white rounded box-shadow">
            <h1>
                Mine Swipper
            </h1>
            <h6 class="border-bottom border-gray pb-2 mb-0">Board</h6>
            <div class="media text-muted pt-3">
                <p class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
                    <strong class="d-block text-gray-dark">
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
        <div class="my-3 p-3 bg-white rounded box-shadow">
            <div class="row justify-content-center">
                <div class="col">
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col">
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col">
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col">
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col">
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col">
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                    <button>*</button>
                </div>
            </div>
        </div>
        <div class="my-3 p-3 bg-white rounded box-shadow">
            <div class="media text-muted pt-3">
                <button type="button" class="btn btn-primary">
                    Go Back
                </button>
                    &nbsp;
                    &nbsp;
                <button type="button" class="btn btn-danger">
                    Pause
                </button>
                    &nbsp;
                    &nbsp;
                <button type="button" class="btn btn-success">
                    Resume
                </button>
                    &nbsp;
                    &nbsp;
                <button type="button" class="btn btn-info">
                    Restart
                </button>
            </div>
        </div>
        <p>
            Nomenclature<br />
            *     : None Revealed Cell<br />
            (White Space) : Revealed Cell<br />
            F     : Flaged Cell<br />
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
