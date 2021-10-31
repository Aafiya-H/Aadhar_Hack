<template>
  <div>
      <approved-address-single/>
      <br>
      <approved-address-single/>
      <br>
      <approved-address-single/>
  </div>
</template>

<script>
import ApprovedAddressSingle from '../../components/ApprovedAddressSingle.vue'
export default {
    layout: 'dashboard',
    components: { ApprovedAddressSingle },
}
</script>

<style>

</style>