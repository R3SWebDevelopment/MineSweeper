import React, { Component } from 'react';
import { connect } from 'react-redux';
import Container from './components/container';
import PropTypes from 'prop-types'
import './css/style.css';
import { defineDomain } from './actions/system';


class App extends Component {

  static propTypes = {
    state: PropTypes.object.isRequired,
    domain: PropTypes.string.isRequired,
  }

  componentDidMount(){
  }

  constructor(props){
    super(props)
    this.dispatch = this.props.dispatch
    this.dispatch(defineDomain(this.props.domain))
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
