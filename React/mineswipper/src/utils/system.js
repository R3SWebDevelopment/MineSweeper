export const accessCheck = (state, history) => {
  if(state.System.token === null){
    takeMeOut(state, history);
  }
}

export const takeMeOut = (state, history) => {
  history.push(state.System.pages.HOME)
}
