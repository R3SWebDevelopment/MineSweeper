import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';


class List extends Component{

  constructor(props){
    super(props)
    this.state = {
      username: '',
      password: ''
    }
  }

  render(){
    return(
      <div />
    )
  }
}

const mapStateToProps = state => ({
  state: state,
  dispatch: state,
});

export default connect(mapStateToProps)(List);
