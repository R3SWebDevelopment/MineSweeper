import { ACTIONS_TYPES } from '../actionsTypes/system'

export const defineDomain = domain => {
  return {
    type: ACTIONS_TYPES.DEFINE_DOMAIN,
    domain: domain
  }
}

export const accessGame = token => {
  return {
    type: ACTIONS_TYPES.ACCESS_GAME,
    token: token
  }
}

export const listGame = (yours, others) => {
  return {
    type: ACTIONS_TYPES.LIST_GAMES,
    yours: yours,
    others: others
  }
}

export const createGame = (yours, others) => {
  return {
    type: ACTIONS_TYPES.CREATE_GAME,
    yours: yours,
    others: others
  }
}

export const joinGame = (yours, others) => {
  return {
    type: ACTIONS_TYPES.JOIN_GAME,
    yours: yours,
    others: others
  }
}

export const leaveGame = (yours, others) => {
  return {
    type: ACTIONS_TYPES.LEAVE_GAME,
    yours: yours,
    others: others
  }
}

export const retriveGame = game => {
  return {
    type: ACTIONS_TYPES.RETRIVE_GAME,
    game: game
  }
}

export const pauseGame = game => {
  return {
    type: ACTIONS_TYPES.PAUSE_GAME,
    game: game
  }
}

export const resumeGame = game => {
  return {
    type: ACTIONS_TYPES.RESUME_GAME,
    game: game
  }
}

export const restartGame = game => {
  return {
    type: ACTIONS_TYPES.RESTART_GAME,
    game: game
  }
}

export const revealCell = game => {
  return {
    type: ACTIONS_TYPES.REVEAL_CELL,
    game: game
  }
}

export const markCell = game => {
  return {
    type: ACTIONS_TYPES.MARK_CELL,
    game: game
  }
}

export const unmarkCell = game => {
  return {
    type: ACTIONS_TYPES.UNMARK_CELL,
    game: game
  }
}
