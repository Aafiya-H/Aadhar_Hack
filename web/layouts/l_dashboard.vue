<template>
  <div class="container-scroller">
      <nav class="navbar default-layout col-lg-12 col-12 p-0 fixed-top d-flex align-items-top flex-row">
        <div class="text-center navbar-brand-wrapper d-flex align-items-center justify-content-start">
            <div class="me-3">
                <button class="navbar-toggler navbar-toggler align-self-center" type="button" data-bs-toggle="minimize">
                    <span class="icon-menu"></span>
                </button>
            </div>
        </div>
        <div class="navbar-menu-wrapper d-flex align-items-top"> 
            <ul class="navbar-nav">
            <li class="nav-item font-weight-semibold d-none d-lg-block ms-0">
                <h1 class="welcome-text">Hey, <span class="text-black fw-bold">Bipin Rawat</span></h1>
            </li>
            </ul>
            <button class="navbar-toggler navbar-toggler-right d-lg-none align-self-center" type="button" data-bs-toggle="offcanvas">
            <span class="mdi mdi-menu"></span>
            </button>
        </div>
        </nav>
        <div class="container-fluid page-body-wrapper">
            <nav class="sidebar sidebar-offcanvas" id="sidebar">
        <ul class="nav active">
          <li class="nav-item">
            <nuxt-link class="nav-link" :active-class="'active'" :to="'/landlord'">
              <i class="menu-icon mdi mdi-floor-plan"></i>
              <span class="menu-title">Home</span>
            </nuxt-link>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="../../index.html">
              <i class="mdi mdi-grid-large menu-icon"></i>
              <span class="menu-title">Logout</span>
            </a>
          </li>
        </ul>
      </nav>
      <div class="main-panel">
          <div class="content-wrapper">
              <nuxt/>
          </div>
      </div>
        </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>