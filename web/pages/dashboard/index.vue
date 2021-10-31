<template>
    <div>
        <active-request-widget/>
        <br>
        <br>
        <past-requests/>
    </div>
</template>

<script>
import ActiveRequestWidget from '../../components/ActiveRequestWidget.vue'
import PastRequests from '../../components/PastRequests.vue'
export default {
  components: { PastRequests, ActiveRequestWidget },
    layout: 'dashboard'
}
</script>

<style>

</style>