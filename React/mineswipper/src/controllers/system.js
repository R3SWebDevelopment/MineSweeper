import { accessGame } from '../actions/system';


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
