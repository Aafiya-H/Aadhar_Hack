import baseURL from "./baseURL";

export default async function(context) {
    context.$axios.setHeader('Content-Type', 'application/json')
    context.$axios.setHeader('Authorization', context.$store.state.token)
    const response = await context.$axios.$get(
        `${baseURL}/api/user/dashboard/home`
    );
    if (response.previous_requests) {
        return [true, response]
    }
    else if (response.Message) {
        return [false, response.Message]
    }
    return [false, "Problem. Contact Developers."]
}