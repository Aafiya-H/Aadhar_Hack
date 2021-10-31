<template>
  <div class="card">
    <div class="card-body">
      <h4 class="card-title">Login as User</h4>
      <form class="forms-sample">
        <div class="form-group">
          <label for="exampleInputEmail1">Email address</label>
          <input type="email" class="form-control" id="exampleInputEmail1" placeholder="Email" v-model="email">
        </div>
        <div class="form-group">
          <label for="exampleInputPassword1">Password</label>
          <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password" v-model="password">
        </div>
        <button type="submit" class="btn btn-primary me-2" v-on:click.prevent = "login()">Submit</button>
      </form>
    </div>
  </div>
</template>

<script>
import login from '@/functions/login.js'

export default {
  data() {
    return {
      email: "",
      password: "",
      isLoading: ""
    }
  },
  methods: {
    async login() {
      if(this.isLoading) return;
      this.isLoading = true;
      const [status, message] = await login(this.email, this.password, this);
      if(!status) alert(message)
      else {
        this.$router.push('/dashboard')
      }
      this.isLoading = false;
    }
  }
}
</script>

<style>

</style>