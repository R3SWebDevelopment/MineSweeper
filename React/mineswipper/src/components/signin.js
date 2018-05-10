import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import '../css/signin.css';


class SignIn extends Component{

  constructor(props){
    super(props)
    this.state = {
      username: '',
      password: ''
    }
  }

  render(){
    return(
      <div className="row justify-content-md-center">
          <div className="col col-lg-4">
              <form className="form-signin text-center">
                  <img className="mb-4" src="http://a1722.phobos.apple.com/us/r30/Purple3/v4/30/ec/c2/30ecc294-7cb4-3b02-6c35-3151bef5b5f7/mzl.tobbabbx.png" alt="" width="200" height="200" />
                  <h1 className="h3 mb-3 font-weight-normal text-center">
                      Please Access Game
                  </h1>
                  <label for="inputEmail" className="sr-only">Email address</label>
                  <input type="email" id="inputEmail" className="form-control" placeholder="Email address" required autofocus />
                  <br />
                  <button className="btn btn-lg btn-primary btn-block" type="submit">Access Game</button>
                  <p className="mt-5 mb-3 text-muted text-center">
                      ricardo.tercero@r3s.com.mx - &copy; 2018
                  </p>
              </form>
          </div>
      </div>
    )
  }
}

const mapStateToProps = state => ({
  state: state,
  dispatch: state,
});

export default connect(mapStateToProps)(SignIn);
