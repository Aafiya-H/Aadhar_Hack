export const state = () => {
    const tokenNew = localStorage.getItem("token")
    const username = localStorage.getItem("username")
    const type = localStorage.getItem("type")
    var isLoggedIn = false;
    if(tokenNew) isLoggedIn = true;
    return {
        isLoggedIn: isLoggedIn,
        token: tokenNew,
        username: username,
        type: type
    }
}

export const mutations = {
    SET_TOKEN(state, token){
        state.token = token
        state.isLoggedIn = true
    },
    REM_TOKEN(state){
        state.token = undefined
        state.isLoggedIn = false
    },
    SET_USERNAME(state, username){
        state.username = username;
    },
    SET_TYPE(state, type){
        state.type = type;
    },
}

export const actions = {
    setToken(context, token){
        localStorage.setItem("token", token)
        context.commit('SET_TOKEN', token)
    },
    setUsername(context, username) {
        localStorage.setItem("username", username);
        context.commit('SET_USERNAME', username);
    },
    setType(context, type) {
        localStorage.setItem("type", type);
        context.commit('SET_TYPE', type);
    },
    logout(context){
        localStorage.removeItem("token")
        context.commit('REM_TOKEN')
    }
}