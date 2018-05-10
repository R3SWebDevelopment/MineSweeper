import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { Provider } from 'react-redux';
import { createStore, combineReducers } from 'redux';
//import { loadState, saveState } from './utils/localStorage';

//const persistedState = loadState();

const store = createStore(
  combineReducers(
    {

    }
  ),
  //persistedState
);
/*
store.subscribe(() => {
  saveState(store.getState());
});
*/
ReactDOM.render(
  <Provider store={store}>
    <App domain={document.getElementById('root').getAttribute('data-domain')} />
  </Provider>, document.getElementById('root'));
