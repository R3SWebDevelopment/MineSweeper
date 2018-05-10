import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import '../css/signin.css';

class NotFound extends Component{

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
          <div className="col col-lg-8">
            <main role="main" className="container">
              <h1 className="mt-5">
                  Page Not Found
              </h1>
              <p className="lead">
                  Please check the url you try to visit
              </p>
            </main>
            <p className="mt-5 mb-3 text-muted text-center">
                ricardo.tercero@r3s.com.mx - &copy; 2018
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

export default connect(mapStateToProps)(NotFound);
