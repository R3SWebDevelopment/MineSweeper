import React, { Component } from 'react';
import { connect } from 'react-redux';
import '../css/signin.css';
import { onChangeInput } from '../utils/inputs';
import { accessGameRequest } from '../controllers/system';


class SignIn extends Component{

  constructor(props){
    super(props)
    this.state = {
      email: '',
    }
  }

  onChangeInput = (evt) => {
    onChangeInput(evt, this);
  }

  accessGranted = (data) => {
    this.setState({
      email: ''
    })
    this.props.history.push(this.props.state.System.pages.LIST)
  }

  accessDenied = (data) => {
    alert("There was an error please try again later")
    this.setState({
      email: ''
    })
  }

  submit = (evt) => {
    evt.preventDefault();
    if(this.state.email.trim().length === 0){
      alert("You need to input your email address");
    }else{
      const data = JSON.stringify({
        email: this.state.email
      })
      accessGameRequest(data,
      this.props.state, this.props.dispatch,
      this.accessGranted.bind(this),
      this.accessDenied.bind(this));
    }
  }

  render(){
    return(
      <div className="row justify-content-md-center">
          <div className="col col-lg-4">
              <form className="form-signin text-center" onSubmit={this.submit.bind(this)}>
                  <img className="mb-4" src="http://a1722.phobos.apple.com/us/r30/Purple3/v4/30/ec/c2/30ecc294-7cb4-3b02-6c35-3151bef5b5f7/mzl.tobbabbx.png" alt="" width="200" height="200" />
                  <h1 className="h3 mb-3 font-weight-normal text-center">
                      Please Access Game
                  </h1>
                  <label htmlFor="inputEmail" className="sr-only">Email address</label>
                  <input type="email" id="email" name="email" className="form-control" placeholder="Email address" required autoFocus value={this.state.email} onChange={this.onChangeInput.bind(this)}/>
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
