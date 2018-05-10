import React, { Component } from 'react';
import { BrowserRouter, Route } from 'react-router-dom';
import { connect } from 'react-redux';

class Container extends Component {

  constructor(props){
    super(props)
    this.state = {
    }
  }

  componentDidMount(){
  }

  render() {
    return (
      <BrowserRouter>
        <div id="container">

        </div>
      </BrowserRouter>
    )
  }
}

const mapStateToProps = state => ({
  state: state,
  dispatch: state,
});

export default connect(mapStateToProps)(Container);
