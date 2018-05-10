import React, { Component } from 'react';
import { connect } from 'react-redux';
//import Header from './components/header';
import Container from './components/container';
//import LoadingApp from './components/loading_app';
import PropTypes from 'prop-types'
/*
import './css/style.css';
import './css/form.css';
import { defineDomain } from './actions/system';
import { fetchCagalog, fetchAPIValid, setAPITimeStamp } from './controllers/system';
*/

class App extends Component {

  static propTypes = {
    state: PropTypes.object.isRequired,
    domain: PropTypes.string.isRequired,
  }

  componentDidMount(){
  }

  constructor(props){
    super(props)
    this.state = {
    }
  }


  render() {
    return (
      <div id="app">
        <Container/>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  state: state,
});

export default connect(mapStateToProps)(App);
