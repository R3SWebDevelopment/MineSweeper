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
    dispatch(listGame(data.results))
    callback(data);
  })
  .catch(error => {
    dispatch(listGame([]))
    errorCallBack(error);
  })
}

export const fetchGame = (id, state, dispatch, callback, errorCallBack) => {
  fetch(state.System.end_points.RETRIVE.replace("[GAME]", id), {
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
    dispatch(listGame(data.results))
    callback(data);
  })
  .catch(error => {
    dispatch(listGame([]))
    errorCallBack(error);
  })
}

export const revealCell = (id, payload, state, dispatch, callback, errorCallBack) => {
  fetch(state.System.end_points.REVEAL.replace("[GAME]", id), {
    method: "POST",
    body: payload,
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Token ' + state.System.token,
    },
  })
  .then(result => {
    return result.json()
  })
  .then(data => {
    dispatch(listGame(data.results))
    callback(data);
  })
  .catch(error => {
    dispatch(listGame([]))
    errorCallBack(error);
  })
}

export const markCell = (id, x, y, state, dispatch, callback, errorCallBack) => {
  fetch(state.System.end_points.MARK.replace("[GAME]", id), {
    method: "POST",
    body: JSON.stringify({
      x: x,
      y: y
    }),
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Token ' + state.System.token,
    },
  })
  .then(result => {
    return result.json()
  })
  .then(data => {
    dispatch(listGame(data.results))
    callback(data);
  })
  .catch(error => {
    dispatch(listGame([]))
    errorCallBack(error);
  })
}

export const unmarkCell = (id, x, y, state, dispatch, callback, errorCallBack) => {
  fetch(state.System.end_points.UNMARK.replace("[GAME]", id), {
    method: "POST",
    body: JSON.stringify({
      x: x,
      y: y
    }),
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Token ' + state.System.token,
    },
  })
  .then(result => {
    return result.json()
  })
  .then(data => {
    dispatch(listGame(data.results))
    callback(data);
  })
  .catch(error => {
    dispatch(listGame([]))
    errorCallBack(error);
  })
}
