import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import '../css/signin.css';


class Loading extends Component{

  constructor(props){
    super(props)
    this.state = {
    }
  }

  render(){
    return(
      <div class="row justify-content-md-center">
          <div class="col col-lg-4">
              <img src="https://www.musicfreelancer.net/assets/images/ajaxloader.gif" />
          </div>
      </div>
    )
  }
}

const mapStateToProps = state => ({
  state: state,
  dispatch: state,
});

export default connect(mapStateToProps)(Loading);
