<template>
    <div v-if="isLoaded">
        <active-request-widget :requestObj="currentRequest" v-if="currentRequest"/>
        <br>
        <br>
        <past-requests/>
    </div>
    <div v-else>
        <h4>Loading... Please Wait...</h4>
    </div>
</template>

<script>
import ActiveRequestWidget from '../../components/ActiveRequestWidget.vue'
import PastRequests from '../../components/PastRequests.vue'
import fetchAllRequests from '@/functions/fetchAllRequests.js'
export default {
    data() {
        return {
            currentRequest: {
                landlord: "991*-****2*696*",
                date_of_request: "3 days ago"
            },
            previousRequests: [],
            isLoaded: true
        }
    },
    components: { PastRequests, ActiveRequestWidget },
    layout: 'dashboard',
    async mounted() {
        // const [status, response] = await fetchAllRequests(this);
        // if(!status) alert(response);
        // else {
        //     this.currentRequest = (response.current_request?.length == 1) ? response.current_request[0] : false;
        //     this.previousRequests = response.previous_requests;
        // }
        // this.isLoaded = true;
    }
}
</script>

<style>

</style>