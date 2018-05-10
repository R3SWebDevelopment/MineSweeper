import { accessGame, listGame } from '../actions/system';


export const accessGameRequest = (payload, state, dispatch, callback, errorCallBack) => {
    fetch(state.System.end_points.ACCESS, {
      method: "POST",
      body: payload,
      headers: {
        'Content-Type': 'application/json',
      },
    })
    .then(result => {
      return result.json()
    })
    .then(data => {
      callback(data);
      dispatch(accessGame(data.token))
    })
    .catch(error => {
      errorCallBack(error);
      dispatch(accessGame(""))
    })
}

export const fetchGames = (state, dispatch, callback, errorCallBack) => {
  fetch(state.System.end_points.LIST, {
    method: "GET",
    body: {},
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Token ' + state.System.token,
    },
  })
  .then(result => {
    return result.json()
  })
  .then(data => {
    dispatch(listGame(data))
    callback(data);
  })
  .catch(error => {
    dispatch(listGame([]))
    errorCallBack(error);
  })
}
