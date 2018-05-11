import { accessGame, listGame, joinGame, leaveGame } from '../actions/system';


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
    dispatch(listGame(data.yours, data.others))
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

export const joingGame = (id, state, dispatch, callback, errorCallBack) => {
  fetch(state.System.end_points.JOIN.replace("[GAME]", id), {
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
    dispatch(joinGame(data.yours, data.others))
    callback(data);
  })
  .catch(error => {
    dispatch(joinGame([], []))
    errorCallBack(error);
  })
}

export const leavingGame = (id, state, dispatch, callback, errorCallBack) => {
  fetch(state.System.end_points.LEAVE.replace("[GAME]", id), {
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
    dispatch(leaveGame(data.yours, data.others))
    callback(data);
  })
  .catch(error => {
    dispatch(leaveGame([], []))
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

export const markCell = (id, payload, state, dispatch, callback, errorCallBack) => {
  fetch(state.System.end_points.MARK.replace("[GAME]", id), {
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

export const unmarkCell = (id, payload, state, dispatch, callback, errorCallBack) => {
  fetch(state.System.end_points.UNMARK.replace("[GAME]", id), {
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

export const pauseGame = (id, state, dispatch, callback, errorCallBack) => {
  fetch(state.System.end_points.PAUSE.replace("[GAME]", id), {
    method: "POST",
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

export const resumeGame = (id, state, dispatch, callback, errorCallBack) => {
  fetch(state.System.end_points.RESUME.replace("[GAME]", id), {
    method: "POST",
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

export const restartGame = (id, state, dispatch, callback, errorCallBack) => {
  fetch(state.System.end_points.RESTART.replace("[GAME]", id), {
    method: "POST",
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
