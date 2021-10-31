import baseURL from "./baseURL";

export default async function(email, password, context) {
    context.$axios.setHeader('Content-Type', 'application/json')
    const response = await context.$axios.$post(
        `${baseURL}/api/login`,
        {
            email_id: email,
            password: password
        }
    );
    if (response.status == 'ok') {
        context.$store.dispatch('setToken', response.token)
        context.$store.dispatch('setUsername', response.user[0].username)
        context.$store.dispatch('setType', "user")
        return [true, undefined]
    }
    else if (response.status == "fail") {
        return [false, response.Message]
    }
    return [false, "Problem with API call. Contact Developers."]
}