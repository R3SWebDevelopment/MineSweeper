import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { connect } from 'react-redux';
import SignIn from './signin';
import NotFound from './404';
import Grid from './grid';
import List from './list';

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
          <Switch>
            <Route exact path="/" component={SignIn} />
            <Route exact path="/list/" component={List} />
            <Route exact path="/game/:key/" component={Grid} />
            <Route component={NotFound} />
          </Switch>
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
