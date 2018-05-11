import { ACTIONS_TYPES }  from '../actionsTypes/system';
import React from 'react';

export const generateOptions = (min, max) => {
  return Array(max + 1).fill(1).map(function(value, index){
    return index
  }).slice(min, max + 1).map(function(value, index){
    return (<option value={value} keys={index}>{value}</option>)
  });
}

const initialState = {
  domain: '',
  token: null,
  games: [],
  others: [],
  game: null,
  pages: {
    HOME: '/',
    LIST: '/list/',
    GAME: '/game/:key/',
  },
}

const END_POINT = {
  ACCESS: '/users/access/',
  LIST: '/mineswipper/games/board/',
  CREATE: '/mineswipper/games/',
  RETRIVE: '/mineswipper/games/[GAME]/',
  REVEAL: '/mineswipper/games/[GAME]/reveals/',
  MARK: '/mineswipper/games/[GAME]/mark/',
  UNMARK: '/mineswipper/games/[GAME]/unmark/',
  PAUSE: '/mineswipper/games/[GAME]/pause/',
  RESUME: '/mineswipper/games/[GAME]/resume/',
  RESTART: '/mineswipper/games/[GAME]/restart/',
}

function generate_end_points(domain){
  var ep = {};
  for(var key in END_POINT){
    ep[key] = domain + END_POINT[key]
  }
  return ep
}

export function System(state=initialState, action){
  switch(action.type){
    case ACTIONS_TYPES.DEFINE_DOMAIN:
      return {
        ...state,
        domain: action.domain,
        end_points: generate_end_points(action.domain),
      }
    case ACTIONS_TYPES.ACCESS_GAME:
      return {
        ...state,
        token: action.token,
      }
    case ACTIONS_TYPES.LIST_GAMES:
      return {
        ...state,
        games: action.yous,
        othes: action.others,
      }
    case ACTIONS_TYPES.CREATE_GAME:
      return {
        ...state,
        game: action.game,
      }
    case ACTIONS_TYPES.RETRIVE_GAME:
      return {
        ...state,
        game: action.game,
      }
    case ACTIONS_TYPES.PAUSE_GAME:
      return {
        ...state,
        game: action.game,
      }
    case ACTIONS_TYPES.RESUME_GAME:
      return {
        ...state,
        game: action.game,
      }
    case ACTIONS_TYPES.RESTART_GAME:
      return {
        ...state,
        game: action.game,
      }
    case ACTIONS_TYPES.REVEAL_CELL:
      return {
        ...state,
        game: action.game,
      }
    case ACTIONS_TYPES.MARK_CELL:
      return {
        ...state,
        game: action.game,
      }
    case ACTIONS_TYPES.UNMARK_CELL:
      return {
        ...state,
        game: action.game,
      }
    default:
      return state
  }
}
