<template>
  <div>
    <div class="container-scroller">
    <div class="container-fluid page-body-wrapper full-page-wrapper">
      <div class="content-wrapper d-flex align-items-center auth px-0">
        <div class="row w-100 mx-0">
          <div class="col-lg-4 mx-auto">
            <login-user v-if="loginAs == 'U'"/>
            <login-landlord v-else/>
            <hr>
            <div class="card">
              <div class="card-body">
                <center>
                <button type="button" class="btn btn-outline-primary btn-block" v-on:click.prevent="loginAs = (loginAs == 'L') ? 'U' : 'L'">
                  <span v-if="loginAs == 'U'">Login as Landlord</span>
                  <span v-else>Login as User</span>
                </button>
                </center>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- content-wrapper ends -->
    </div>
    <!-- page-body-wrapper ends -->
  </div>
  </div>
</template>

<script>
import LoginLandlord from '../components/LoginLandlord.vue'
import LoginUser from '../components/LoginUser.vue'
export default {
  components: { LoginUser, LoginLandlord },
  data(){
    return {
      loginAs: "U"
    }
  }

}
</script>

<style>

</style>