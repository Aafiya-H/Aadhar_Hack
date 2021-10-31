import baseURL from "./baseURL";

export default async function(aadhar, context) {
    context.$axios.setHeader('Content-Type', 'application/json')
    const response = await context.$axios.$post(
        `${baseURL}/api/aadhar-user/dashboard/getOTP`,
        {
            aadhar_no: aadhar
        }
    );
    if (response.txnID) {
        return [true, response.txnID]
    }
    return [false, "Problem. Contact Developers."]
}