<template>
  <div>
      <div class="container-scroller">
        <div class="container-fluid page-body-wrapper full-page-wrapper">
        <div class="content-wrapper d-flex align-items-center auth px-0">
            <div class="row w-100 mx-0">
            <div class="col-lg-4 mx-auto">
                <div class="auth-form-light text-left py-5 px-4 px-sm-5">
                <div class="brand-logo">
                    <!-- <img src="../../images/logo.svg" alt="logo"> -->
                </div>
                <h4>Hello! let's get started</h4>
                <h6 class="fw-light">Sign in to continue.</h6>
                <form class="pt-3">
                    <div class="form-group">
                    <input type="email" class="form-control form-control-lg" id="exampleInputEmail1" placeholder="Email">
                    </div>
                    <div class="form-group">
                    <input type="password" class="form-control form-control-lg" id="exampleInputPassword1" placeholder="Password">
                    </div>
                    <div class="mt-3">
                    <a class="d-flex justify-content-center btn btn-block btn-primary btn-lg font-weight-medium auth-form-btn" href="../../index.html">SIGN IN</a>
                    </div>
                    <hr>
                    <a class="d-flex justify-content-center btn btn-block btn-outline-primary btn-lg font-weight-medium auth-form-btn">Login as Landlord</a>
                    <div class="text-center mt-4 fw-light">
                    Don't have an account? <a href="register.html" class="text-primary">Create</a>
                    </div>
                </form>
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
import LoginUser from '../components/LoginUser.vue'
export default {
  components: { LoginUser },

}
</script>

<style>

</style>