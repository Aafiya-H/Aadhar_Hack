import baseURL from "./baseURL";

export default async function(txnId, aadhar, otp, context) {
    context.$axios.setHeader('Content-Type', 'application/json')
    const response = await context.$axios.$post(
        `${baseURL}/api/aadhar-user/dashboard/validate_OTP`,
        {
            txn_id: txnId,
            uid: aadhar,
            otp: otp
        }
    );
    if (response.token) {
        context.$store.dispatch('setToken', response.token)
        context.$store.dispatch('setUsername', response.name)
        context.$store.dispatch('setType', "landlord")
        return [true, undefined]
    }
    return [false, "Problem. Contact Developers."]
}